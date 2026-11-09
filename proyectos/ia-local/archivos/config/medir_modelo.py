#!/usr/bin/env python3
"""medir_modelo.py - Linea 2 (IA local)

Mide un modelo de LM Studio siempre con los mismos prompts, para poder comparar
modelos entre si. Solo usa la libreria estandar de Python.

Que mide:
  - Carga (s): cuanto tarda el modelo en pasar del disco a la memoria.
  - TTFT (s): "time to first token", tiempo hasta la primera palabra.
  - tok/s: tokens por segundo mientras escribe (sin contar la espera inicial).
  - Memoria: cuanta memoria del Mac se ocupo de mas respecto a antes de cargarlo.

Como correrlo (con el servidor de LM Studio encendido: lms server start):
  python3 config/medir_modelo.py <clave-del-modelo> --cuantizacion 4bit --motor MLX
La clave sale de: lms ls
Para juzgar calidad (respuestas completas), agrega: --repeticiones 1 --max-tokens 4096
"""
import argparse
import csv
import datetime as dt
import json
import pathlib
import re
import statistics
import subprocess
import threading
import time
import urllib.request

BASE = pathlib.Path(__file__).resolve().parent.parent
URL = "http://localhost:1234/v1/chat/completions"
LMS = pathlib.Path.home() / ".lmstudio/bin/lms"
REPETICIONES = 3
MAX_TOKENS = 512
CONTEXTO = 16384  # igual para todos los modelos, para que sea comparable

# Texto largo y siempre identico: simula pasarle un archivo grande desde el editor.
CODIGO_LARGO = "\n".join(
    f"def paso_{i}(t, q={i}):\n    \"\"\"Actualiza la temperatura en el nodo {i}.\"\"\"\n"
    f"    return t + q * 0.{(i % 9) + 1} - t / {i + 2}\n"
    for i in range(150)
)

PROMPTS = {
    "explicar_codigo": (
        "Explica en espanol, paso a paso, que hace este codigo y que error tiene:\n\n"
        "def promedio(lista):\n    total = 0\n    for i in range(len(lista) + 1):\n"
        "        total += lista[i]\n    return total / len(lista)\n"
    ),
    "escribir_codigo": (
        "Escribe una funcion en Python que resuelva la conduccion de calor 1D "
        "transitoria en una placa con diferencias finitas explicitas. Comenta "
        "cada paso y verifica la condicion de estabilidad."
    ),
    "razonar_fisica": (
        "Un eje de acero de 40 mm de diametro transmite 15 kW a 300 rpm. Calcula "
        "el esfuerzo cortante maximo y explica el porque fisico de cada paso."
    ),
    "contexto_largo": (
        "Este es un modulo de un simulador termico:\n\n" + CODIGO_LARGO +
        "\n\nResume en espanol que hace el modulo y propone como simplificarlo."
    ),
}


def memoria_usada_gb():
    """Memoria ocupada del Mac segun vm_stat (activa + wired + comprimida)."""
    salida = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    pagina = int(re.search(r"page size of (\d+)", salida).group(1))
    leer = lambda nombre: int(re.search(rf"{nombre}:\s+(\d+)", salida).group(1))
    paginas = (leer("Pages active") + leer("Pages wired down")
               + leer("Pages occupied by compressor"))
    return paginas * pagina / 1e9


class VigiaMemoria(threading.Thread):
    """Mira la memoria cada 0.5 s y guarda el maximo."""

    def __init__(self):
        super().__init__(daemon=True)
        self.maximo = 0.0
        self.parar = threading.Event()

    def run(self):
        while not self.parar.is_set():
            self.maximo = max(self.maximo, memoria_usada_gb())
            self.parar.wait(0.5)


def generar(modelo, prompt, max_tokens):
    """Pide una respuesta en streaming y cronometra cada token que llega."""
    cuerpo = json.dumps({
        "model": modelo,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.2,
        "stream": True,
        "stream_options": {"include_usage": True},
    }).encode()
    pedido = urllib.request.Request(
        URL, data=cuerpo, headers={"Content-Type": "application/json"})

    inicio = time.perf_counter()
    primero = ultimo = None
    texto, razonamiento = [], []
    uso = {}
    fin = None  # "stop" = termino solo; "length" = lo corto el limite de tokens
    with urllib.request.urlopen(pedido, timeout=1800) as respuesta:
        for linea in respuesta:
            linea = linea.decode().strip()
            if not linea.startswith("data: ") or linea == "data: [DONE]":
                continue
            dato = json.loads(linea[6:])
            uso = dato.get("usage") or uso
            if not dato.get("choices"):
                continue
            fin = dato["choices"][0].get("finish_reason") or fin
            delta = dato["choices"][0].get("delta", {})
            pensado = delta.get("reasoning_content") or delta.get("reasoning") or ""
            contenido = delta.get("content") or ""
            if pensado or contenido:
                ultimo = time.perf_counter()
                primero = primero or ultimo
                razonamiento.append(pensado)
                texto.append(contenido)

    if primero is None or not uso.get("completion_tokens"):
        raise RuntimeError(f"El servidor no devolvio tokens ni conteo: {uso}")
    tokens = uso["completion_tokens"]
    return {
        "ttft_s": primero - inicio,
        # (tokens - 1) porque el cronometro de escritura arranca en el primer token.
        "tok_s": (tokens - 1) / (ultimo - primero) if ultimo > primero else 0.0,
        "tokens_salida": tokens,
        "fin": fin,
        "tokens_entrada": uso.get("prompt_tokens"),
        "texto": "".join(texto),
        "razonamiento": "".join(razonamiento),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("modelo", help="clave del modelo, ver: lms ls")
    # Se piden a mano porque la regla 5 de CLAUDE.md exige anotarlos en cada prueba.
    parser.add_argument("--cuantizacion", required=True, help="por ejemplo 4bit")
    parser.add_argument("--motor", required=True, choices=["MLX", "GGUF"])
    parser.add_argument("--repeticiones", type=int, default=REPETICIONES)
    parser.add_argument("--max-tokens", type=int, default=MAX_TOKENS)
    args = parser.parse_args()

    base_memoria = memoria_usada_gb()
    subprocess.run([str(LMS), "unload", "--all"], capture_output=True)
    t0 = time.perf_counter()
    subprocess.run(
        [str(LMS), "load", args.modelo, "--gpu", "max", "--context-length",
         str(CONTEXTO), "--identifier", "medicion", "-y"],
        check=True)
    carga_s = time.perf_counter() - t0

    vigia = VigiaMemoria()
    vigia.start()
    filas, respuestas = [], []
    for nombre, prompt in PROMPTS.items():
        for rep in range(1, args.repeticiones + 1):
            r = generar("medicion", prompt, args.max_tokens)
            print(f"{nombre} #{rep}: TTFT {r['ttft_s']:.2f} s, "
                  f"{r['tok_s']:.1f} tok/s, {r['tokens_salida']} tokens, fin={r['fin']}")
            filas.append({"prompt": nombre, "rep": rep,
                          **{k: r[k] for k in ("ttft_s", "tok_s", "tokens_entrada", "tokens_salida", "fin")}})
            if rep == 1:
                respuestas.append((nombre, r))
    vigia.parar.set()
    vigia.join()

    fecha = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    seguro = re.sub(r"[^A-Za-z0-9._-]", "_", args.modelo)
    destino = BASE / "pruebas"
    with open(destino / f"{fecha}_{seguro}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)

    lineas = [
        f"# Medicion de {args.modelo}", "",
        f"- Fecha: {fecha}",
        f"- Cuantizacion: {args.cuantizacion}",
        f"- Motor: {args.motor}",
        f"- Carga: {carga_s:.1f} s",
        f"- Memoria extra maxima (vm_stat, incluye al resto del Mac): "
        f"{vigia.maximo - base_memoria:.1f} GB",
        f"- Contexto: {CONTEXTO} tokens; salida maxima: {args.max_tokens} tokens", "",
        "La repeticion 1 es la unica sin cache del prompt; por eso su TTFT va aparte.", "",
        "| Prompt | Tokens entrada | TTFT rep. 1 (s) | TTFT mediana (s) | tok/s mediana | tok/s min-max |",
        "|---|---|---|---|---|---|",
    ]
    for nombre in PROMPTS:
        g = [x for x in filas if x["prompt"] == nombre]
        v = [x["tok_s"] for x in g]
        lineas.append(
            f"| {nombre} | {g[0]['tokens_entrada']} | {g[0]['ttft_s']:.2f} | "
            f"{statistics.median(x['ttft_s'] for x in g):.2f} | "
            f"{statistics.median(v):.1f} | {min(v):.1f}-{max(v):.1f} |")
    lineas += ["", "## Respuestas de la repeticion 1 (para juzgar calidad)", ""]
    for nombre, r in respuestas:
        lineas += [f"### {nombre}", ""]
        if r["razonamiento"]:
            lineas += ["**Razonamiento:**", "", r["razonamiento"], ""]
        lineas += ["**Respuesta:**", "", r["texto"] or "(no llego a responder dentro del limite de tokens)", ""]

    informe = destino / f"{fecha}_{seguro}.md"
    informe.write_text("\n".join(lineas))
    print(f"\nCarga: {carga_s:.1f} s | Memoria extra: {vigia.maximo - base_memoria:.1f} GB")
    print(f"Informe: {informe}")


if __name__ == "__main__":
    main()

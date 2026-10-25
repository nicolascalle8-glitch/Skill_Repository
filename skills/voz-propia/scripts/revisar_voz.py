#!/usr/bin/env python3
"""Marca en un texto lo que no suena a ella (lista de references/perfil.md).

Uso:
    python revisar_voz.py <archivo.txt|.md>   (o el texto por stdin con "-")

Imprime cada hallazgo con su línea. Sale con código 1 si encontró algo.
Solo busca lo que se puede buscar con reglas (palabras, guiones largos, cierres, tríos de
adjetivos sencillos). El juicio de si "suena a ella" sigue siendo de quien revisa.
"""
import re
import sys

REGLAS = [
    ("lenguaje inflado", r"\b(de vanguardia|de primer nivel|referente|se ha erigido|consolida(?:r|do)?|"
                         r"esperanza tangible|ecosistemas?|escalables?|robust[oa]s?|"
                         r"jueg(?:a|an) un papel (?:fundamental|clave|crucial)|clave para el éxito|"
                         r"sin precedentes|revolucionari[oa]|innovador[a]?|potenciar|sinergia)\b"),
    ("muletilla", r"\b(cabe destacar|es importante (?:mencionar|destacar|resaltar|señalar)|"
                  r"es fundamental subrayar|a continuación se presenta|en este sentido|"
                  r"vale la pena (?:resaltar|destacar|mencionar)|no es menos importante)\b"),
    ("cierre tipo eslogan", r"(ese es el verdadero poder|en definitiva|en conclusión|en resumen|"
                            r"en última instancia)"),
    ("guion largo", r"—"),
    ("pregunta u oferta al lector al final", r"(¿te gustaría|¿quieres que|si necesitas|no dudes en|"
                                             r"espero que (?:esto|te))"),
]
TRIO = re.compile(r"\b(\w+(?:o|a|e|es|os|as|al|ble|nte|ivo|iva))\s*,\s*(\w+(?:o|a|e|es|os|as|al|ble|nte|ivo|iva))"
                  r"\s*y\s*(\w+(?:o|a|e|es|os|as|al|ble|nte|ivo|iva))\b", re.I)


def revisar(texto):
    hall = []
    for n, linea in enumerate(texto.splitlines(), 1):
        for nombre, patron in REGLAS:
            for m in re.finditer(patron, linea, re.I):
                hall.append((n, nombre, m.group(0)))
        for m in TRIO.finditer(linea):
            hall.append((n, "posible trío de adjetivos", m.group(0)))
        if re.search(r"\*\*[^*]{60,}\*\*", linea):
            hall.append((n, "negrita en frase entera", re.search(r"\*\*[^*]{60,}\*\*", linea).group(0)[:40] + "…"))
        if not linea.lstrip().startswith(("|", "-", "*")):
            for frase in re.split(r"(?<=[.?!;])\s+", linea):
                if len(frase.split()) > 35:
                    hall.append((n, "frase muy larga (partir)", f"{len(frase.split())} palabras: {frase[:40]}…"))
    return hall


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    texto = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    hall = revisar(texto)
    for n, nombre, frag in hall:
        print(f"línea {n}: [{nombre}] {frag}")
    print(f"\n{len(hall)} hallazgo(s)." if hall else "Sin hallazgos de la lista.")
    sys.exit(1 if hall else 0)


if __name__ == "__main__":
    main()

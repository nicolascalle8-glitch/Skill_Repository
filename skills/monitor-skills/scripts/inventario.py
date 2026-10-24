#!/usr/bin/env python3
"""Inventario y chequeos automáticos de las skills de Nick.

Uso:
    python inventario.py <ruta-repo> [--instaladas /mnt/skills/plugins] [--json]

Revisa lo que se puede revisar sin criterio humano:
- Skills en el repo vs. instaladas en Claude (falta en un lado, cuerpo distinto).
- Encabezado: name válido, description presente y su largo.
- Archivos que el SKILL.md nombra (references/, scripts/, shared/, registry/) y no existen.
- Skills nombradas entre comillas `x` que no existen ni están registradas.
- Coherencia con registry/CAPACIDADES.yml y el catálogo del router.
- Tamaño del SKILL.md (líneas y palabras) y fecha del último commit que lo tocó.

No juzga si una skill sobra o sirve: eso lo hace el monitor con criterio.
"""
import argparse
import json
import os
import re
import subprocess
import sys

import yaml

NOMBRE_OK = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Skills de Anthropic que vienen con Claude; no son de Nick.
SKILLS_SISTEMA = {
    "artifact-emulator", "built-in-browser", "chrome-browser", "computer-use",
    "deep-research", "docs", "docx", "google-workspace", "import-memory", "morning",
    "pdf", "pdf-reading", "pptx", "xlsx", "skill-creator", "file-reading",
    "frontend-design", "product-self-knowledge", "setup-claude", "artifact-design",
    "artifact-capabilities",
}


def leer_skill(ruta_md):
    with open(ruta_md, encoding="utf-8") as f:
        texto = f.read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
    if not m:
        return None, texto, "sin encabezado YAML"
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return None, m.group(2), f"YAML inválido: {e}"
    return meta, m.group(2), None


def skills_en(carpeta):
    res = {}
    if not os.path.isdir(carpeta):
        return res
    for nombre in sorted(os.listdir(carpeta)):
        md = os.path.join(carpeta, nombre, "SKILL.md")
        if os.path.isfile(md):
            res[nombre] = md
    return res


def ultimo_commit(repo, ruta):
    try:
        out = subprocess.run(
            ["git", "-C", repo, "log", "-1", "--format=%cs", "--", ruta],
            capture_output=True, text=True, timeout=20,
        ).stdout.strip()
        return out or None
    except Exception:
        return None


def normalizar(cuerpo):
    return "\n".join(l.rstrip() for l in cuerpo.strip().splitlines())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--instaladas", default="/mnt/skills/plugins")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    repo = os.path.abspath(a.repo)
    en_repo = skills_en(os.path.join(repo, "skills"))
    instaladas = {k: v for k, v in skills_en(a.instaladas).items() if k not in SKILLS_SISTEMA}

    cap_path = os.path.join(repo, "registry", "CAPACIDADES.yml")
    capacidades = {}
    if os.path.isfile(cap_path):
        with open(cap_path, encoding="utf-8") as f:
            capacidades = (yaml.safe_load(f) or {}).get("capacidades", {}) or {}
    registradas = {v.get("skill"): {"capacidad": k, **v} for k, v in capacidades.items() if v.get("skill")}

    cat_path = os.path.join(repo, "skills", "router-ing", "references", "catalogo.md")
    catalogo = set()
    if os.path.isfile(cat_path):
        with open(cat_path, encoding="utf-8") as f:
            for l in f:
                m = re.match(r"^\|\s*`([a-z0-9-]+)`", l)
                if m:
                    catalogo.add(m.group(1))

    conocidas = set(en_repo) | set(instaladas) | set(registradas) | catalogo | SKILLS_SISTEMA
    todas = sorted(set(en_repo) | set(instaladas))
    filas, hallazgos = [], []

    for s in todas:
        fuente = en_repo.get(s) or instaladas.get(s)
        meta, cuerpo, err = leer_skill(fuente)
        f = {"skill": s, "en_repo": s in en_repo, "instalada": s in instaladas}
        if err:
            hallazgos.append({"skill": s, "tipo": "encabezado", "detalle": err})
            meta = {}
        nombre = str(meta.get("name", "")).strip('"')
        desc = str(meta.get("description", "") or "")
        f["lineas"] = len(cuerpo.splitlines())
        f["palabras"] = len(cuerpo.split())
        f["largo_descripcion"] = len(desc)
        f["ultimo_commit"] = ultimo_commit(repo, os.path.join("skills", s)) if s in en_repo else None
        reg = registradas.get(s)
        f["estado"] = reg.get("estado") if reg else None
        f["ultima_revision"] = str(reg.get("ultima_revision")) if reg and reg.get("ultima_revision") else None
        filas.append(f)

        if nombre != s:
            hallazgos.append({"skill": s, "tipo": "encabezado", "detalle": f"name '{nombre}' no coincide con la carpeta"})
        if not NOMBRE_OK.match(s):
            hallazgos.append({"skill": s, "tipo": "encabezado", "detalle": "nombre no está en kebab-case"})
        if not desc:
            hallazgos.append({"skill": s, "tipo": "encabezado", "detalle": "sin description"})
        elif len(desc) > 1024:
            hallazgos.append({"skill": s, "tipo": "encabezado", "detalle": f"description de {len(desc)} caracteres (límite 1024)"})
        if f["lineas"] > 500:
            hallazgos.append({"skill": s, "tipo": "tamaño", "detalle": f"SKILL.md con {f['lineas']} líneas (>500)"})

        if s not in en_repo:
            hallazgos.append({"skill": s, "tipo": "sincronía", "detalle": "instalada en Claude pero no está en el repo"})
        elif s not in instaladas:
            hallazgos.append({"skill": s, "tipo": "sincronía", "detalle": "está en el repo pero no instalada en Claude"})
        else:
            _, c_repo, _ = leer_skill(en_repo[s])
            _, c_inst, _ = leer_skill(instaladas[s])
            if normalizar(c_repo) != normalizar(c_inst):
                hallazgos.append({"skill": s, "tipo": "sincronía", "detalle": "el texto instalado es distinto al del repo (reinstalar o subir cambios)"})
            # referencias del repo vs instaladas
            for sub in ("references", "scripts"):
                r = os.path.join(os.path.dirname(en_repo[s]), sub)
                i = os.path.join(os.path.dirname(instaladas[s]), sub)
                ra = set(os.listdir(r)) if os.path.isdir(r) else set()
                ia = set(os.listdir(i)) if os.path.isdir(i) else set()
                if ra != ia:
                    hallazgos.append({"skill": s, "tipo": "sincronía", "detalle": f"{sub}/ distinto: solo repo {sorted(ra - ia)}, solo instalada {sorted(ia - ra)}"})

        if s not in registradas:
            hallazgos.append({"skill": s, "tipo": "registro", "detalle": "no está en registry/CAPACIDADES.yml"})
        if s not in catalogo:
            hallazgos.append({"skill": s, "tipo": "registro", "detalle": "no está en el catálogo del router"})

        base = os.path.dirname(fuente)
        for ref in sorted(set(re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", cuerpo))):
            if not os.path.exists(os.path.join(base, ref)):
                hallazgos.append({"skill": s, "tipo": "archivo faltante", "detalle": ref})
        for ref in sorted(set(re.findall(r"`((?:shared|registry)/[^`\s]+)`", cuerpo))):
            if not os.path.exists(os.path.join(repo, ref)):
                hallazgos.append({"skill": s, "tipo": "archivo faltante", "detalle": ref})
        # Solo cuenta como skill si la línea habla de skills o de usar/remitir a algo.
        contexto = re.compile(r"skill|\busa\b|\busar\b|úsala|remite|recomienda|pasa(?:le)? el trabajo", re.I)
        nombradas = set()
        for linea in cuerpo.splitlines():
            if contexto.search(linea):
                nombradas |= set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", linea))
        for otra in sorted(nombradas - {"en-prueba", "kebab-case"}):
            if otra in conocidas or otra == s:
                continue
            hallazgos.append({"skill": s, "tipo": "nombra skill inexistente", "detalle": otra})

    for sk, reg in registradas.items():
        if reg.get("estado") in ("activa", "en-prueba") and sk not in en_repo and sk not in instaladas:
            hallazgos.append({"skill": sk, "tipo": "registro", "detalle": f"CAPACIDADES dice '{reg.get('estado')}' pero no existe"})

    salida = {"skills": filas, "hallazgos": hallazgos,
              "pendientes": sorted(k for k, v in registradas.items() if v.get("estado") == "pendiente")}
    if a.json:
        json.dump(salida, sys.stdout, ensure_ascii=False, indent=2)
        return
    print("| Skill | Repo | Instalada | Estado | Últ. revisión | Últ. commit | Líneas | Palabras | Desc. |")
    print("|---|---|---|---|---|---|---|---|---|")
    for f in filas:
        print(f"| {f['skill']} | {'sí' if f['en_repo'] else 'NO'} | {'sí' if f['instalada'] else 'NO'} | "
              f"{f['estado'] or '—'} | {f['ultima_revision'] or '—'} | {f['ultimo_commit'] or '—'} | "
              f"{f['lineas']} | {f['palabras']} | {f['largo_descripcion']} |")
    print(f"\nPendientes registradas (no existen aún): {', '.join(salida['pendientes']) or 'ninguna'}")
    print(f"\nHallazgos automáticos ({len(hallazgos)}):")
    for h in hallazgos:
        print(f"- [{h['tipo']}] {h['skill']}: {h['detalle']}")


if __name__ == "__main__":
    main()

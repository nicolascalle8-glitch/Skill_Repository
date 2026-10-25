#!/usr/bin/env python3
"""Sube al repo las skills que Nick creó o cambió en Claude.

Uso:
    python sincronizar.py <ruta-repo> [--instaladas <carpeta>] [--aplicar] [--json]

La carpeta de skills instaladas se busca sola (ver comun.CANDIDATAS); --instaladas solo
hace falta si no la encuentra.

Sin --aplicar solo dice qué haría. Con --aplicar copia los archivos al repo y registra las
skills nuevas en CAPACIDADES.yml y en el catálogo del router (no hace commit).

Antes de correrlo, trae historia al clon: git fetch --depth=200 origin main

Cómo decide, archivo por archivo (comparando con el historial de git del repo):
- igual          -> lo instalado es lo mismo que el repo. Nada que hacer.
- cambio-claude  -> lo instalado no coincide con ninguna versión que haya tenido el repo:
                    Nick lo cambió en Claude. Se sube.
- repo-adelante  -> lo instalado coincide con una versión VIEJA del repo: el repo es más
                    nuevo y Nick no ha reinstalado. No se toca; se avisa.
Por skill:
- nueva          -> instalada y no está en el repo. Se sube completa y se registra.
- cambiada       -> algún archivo es cambio-claude y ninguno es repo-adelante. Se sube.
- reinstalar     -> algún archivo es repo-adelante y ninguno es cambio-claude. No se toca.
- conflicto      -> hay de los dos. No se toca; lo decide Nick.
- solo-repo      -> está en el repo y no instalada. No se borra nada; se avisa.
- igual          -> nada que hacer.
Nunca borra archivos del repo. Si un archivo parece tener una clave o contraseña, la skill
no se sube y se avisa (contrato: nada de secretos en el repo).
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import buscar_instaladas, catalogos, hoy_bogota, router_de  # noqa: E402

SKILLS_SISTEMA = {
    "artifact-emulator", "built-in-browser", "chrome-browser", "computer-use",
    "deep-research", "docs", "docx", "google-workspace", "import-memory", "morning",
    "pdf", "pdf-reading", "pptx", "xlsx", "skill-creator", "file-reading",
    "frontend-design", "product-self-knowledge", "setup-claude", "artifact-design",
    "artifact-capabilities",
}
IGNORAR = {"__pycache__", ".DS_Store", "LICENSE.txt"}
SECRETOS = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-ant-[A-Za-z0-9-]{10,}|"
    r"sk-[A-Za-z0-9]{32,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|xox[bp]-[A-Za-z0-9-]{10,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:password|contraseña|api[_-]?key|token)\s*[:=]\s*['\"][^'\"\s]{8,})",
    re.I,
)


def skills_propias(instaladas):
    """Nombres de las skills de Nick. Usa manifest.json (source == plugin) si existe."""
    man = os.path.join(instaladas, "manifest.json")
    if os.path.isfile(man):
        try:
            data = json.load(open(man, encoding="utf-8"))
            return {s["name"]: s.get("updatedAt") for s in data.get("skills", [])
                    if s.get("source") == "plugin"}
        except Exception:
            pass
    return {d: None for d in os.listdir(instaladas)
            if os.path.isfile(os.path.join(instaladas, d, "SKILL.md")) and d not in SKILLS_SISTEMA}


def archivos(carpeta):
    res = {}
    for raiz, dirs, files in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in IGNORAR]
        for f in files:
            if f in IGNORAR or f.endswith(".pyc"):
                continue
            p = os.path.join(raiz, f)
            res[os.path.relpath(p, carpeta)] = p
    return res


def partir_skill(texto):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
    if not m:
        return None, None, texto
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = None
    return m.group(1), meta, m.group(2)


def clave(rel, contenido):
    """Huella del contenido. En SKILL.md ignora el formato del encabezado (comillas, >-)."""
    if rel == "SKILL.md":
        try:
            texto = contenido.decode("utf-8")
        except UnicodeDecodeError:
            return hashlib.sha1(contenido).hexdigest()
        _, meta, cuerpo = partir_skill(texto)
        meta = meta or {}
        norm = json.dumps({"name": str(meta.get("name", "")).strip(),
                           "description": " ".join(str(meta.get("description", "")).split())},
                          ensure_ascii=False)
        cuerpo = "\n".join(l.rstrip() for l in cuerpo.strip().splitlines())
        return hashlib.sha1((norm + "\n" + cuerpo).encode("utf-8")).hexdigest()
    if not rel.endswith((".png", ".jpg", ".woff2", ".pdf", ".xlsx")):
        try:
            t = contenido.decode("utf-8")
            return hashlib.sha1("\n".join(l.rstrip() for l in t.strip().splitlines()).encode()).hexdigest()
        except UnicodeDecodeError:
            pass
    return hashlib.sha1(contenido).hexdigest()


def git(repo, *args, binario=False):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, timeout=60)
    return r.stdout if binario else r.stdout.decode("utf-8", "replace")


def versiones_viejas(repo, ruta_repo):
    """Huellas de todas las versiones que ha tenido un archivo en el historial."""
    rel = os.path.basename(ruta_repo) if ruta_repo.endswith("SKILL.md") else ruta_repo
    huellas = set()
    for h in git(repo, "log", "--format=%H", "--", ruta_repo).split():
        c = git(repo, "show", f"{h}:{ruta_repo}", binario=True)
        if c:
            huellas.add(clave("SKILL.md" if rel == "SKILL.md" else ruta_repo, c))
    return huellas


def comparar(repo, skill, inst_dir):
    repo_dir = os.path.join(repo, "skills", skill)
    inst = archivos(inst_dir)
    if not os.path.isdir(repo_dir):
        return "nueva", {r: "nuevo" for r in inst}, []
    en_repo = archivos(repo_dir)
    estado_arch, faltan_en_claude = {}, sorted(set(en_repo) - set(inst))
    for rel, p in inst.items():
        c_inst = open(p, "rb").read()
        k = clave(rel, c_inst)
        if rel in en_repo and k == clave(rel, open(en_repo[rel], "rb").read()):
            continue
        ruta_repo = f"skills/{skill}/{rel}"
        viejas = versiones_viejas(repo, ruta_repo)
        if rel in en_repo or viejas:
            estado_arch[rel] = "repo-adelante" if k in viejas else "cambio-claude"
        else:
            estado_arch[rel] = "cambio-claude"  # archivo nuevo creado en Claude
    tipos = set(estado_arch.values())
    if not tipos:
        # Archivos que el repo tiene y Claude no: casi siempre el repo es más nuevo.
        estado = "reinstalar" if faltan_en_claude else "igual"
    elif tipos == {"cambio-claude"}:
        estado = "cambiada"
    elif tipos == {"repo-adelante"}:
        estado = "reinstalar"
    else:
        estado = "conflicto"
    return estado, estado_arch, faltan_en_claude


def tiene_secretos(inst_dir):
    hallados = []
    for rel, p in archivos(inst_dir).items():
        try:
            t = open(p, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        for m in SECRETOS.finditer(t):
            hallados.append(f"{rel}: {m.group(0)[:12]}…")
    return hallados


def escribir(repo, skill, inst_dir, cambios):
    repo_dir = os.path.join(repo, "skills", skill)
    for rel in cambios:
        src = os.path.join(inst_dir, rel)
        dst = os.path.join(repo_dir, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        data = open(src, "rb").read()
        if rel == "SKILL.md" and os.path.isfile(dst):
            # Si el encabezado solo cambió de formato, se conserva el del repo.
            fm_r, meta_r, _ = partir_skill(open(dst, encoding="utf-8").read())
            fm_i, meta_i, cuerpo_i = partir_skill(data.decode("utf-8"))
            mismo = meta_r and meta_i and str(meta_r.get("name")).strip() == str(meta_i.get("name")).strip() \
                and " ".join(str(meta_r.get("description")).split()) == " ".join(str(meta_i.get("description")).split())
            if mismo:
                data = f"---\n{fm_r}\n---\n{cuerpo_i}".encode("utf-8")
        elif rel == "SKILL.md":
            fm_i, meta_i, cuerpo_i = partir_skill(data.decode("utf-8"))
            if meta_i and fm_i and re.match(r'^name:\s*"', fm_i):
                fm_i = re.sub(r'^name:\s*"([^"]+)"', r"name: \1", fm_i, flags=re.M)
                data = f"---\n{fm_i}\n---\n{cuerpo_i}".encode("utf-8")
        open(dst, "wb").write(data)


def registrar(repo, skill, inst_dir, hoy):
    """Agrega la skill nueva a CAPACIDADES.yml y al catálogo de SU router, si no está.

    Si la skill es de otra familia (tiene su propio router-x), no se toca el catálogo de
    router-ing: se agrega al de ese router si existe, o se deja anotado.
    """
    texto = open(os.path.join(inst_dir, "SKILL.md"), encoding="utf-8").read()
    _, meta, _ = partir_skill(texto)
    router = router_de(repo, skill, texto)
    desc = " ".join(str((meta or {}).get("description", "")).split())
    uso = re.split(r"(?<=[.:])\s", desc, maxsplit=1)[0].rstrip(".:")
    cap = os.path.join(repo, "registry", "CAPACIDADES.yml")
    t = open(cap, encoding="utf-8").read()
    if f"skill: {skill}\n" not in t:
        clave = skill
        n = 2
        while re.search(rf"^  {re.escape(clave)}:\s*$", t, re.M):
            clave = f"{skill}-{n}"  # ese nombre ya lo usa otra capacidad
            n += 1
        linea_router = f"    router: {router}\n" if router != "router-ing" else ""
        bloque = (f"\n  {clave}:\n    skill: {skill}\n    etapa: por-definir\n{linea_router}    estado: en-prueba\n"
                  f"    ultima_revision: {hoy}\n    nota: Subida automáticamente por monitor-skills desde lo "
                  f"instalado en Claude. Falta revisar etapa y caso de prueba.\n")
        t = t.replace("\n  enmarcar-problema:", bloque + "\n  enmarcar-problema:", 1) \
            if "\n  enmarcar-problema:" in t else t.rstrip("\n") + "\n" + bloque
        open(cap, "w", encoding="utf-8").write(t)
        yaml.safe_load(open(cap, encoding="utf-8"))
    if router == skill:
        return  # es un router: no se lista en el catálogo de otro router
    cats = catalogos(repo)
    if router not in cats:
        return  # su router todavía no tiene catálogo en el repo
    cat, listadas = cats[router]
    if skill in listadas:
        return
    if router != "router-ing":
        c = open(cat, encoding="utf-8").read().rstrip("\n")
        filas = [l for l in c.splitlines() if l.startswith("| `")]
        fila = f"| `{skill}` | en-prueba | {uso}. | Ver su SKILL.md. |"
        if filas and filas[-1].count("|") == fila.count("|"):
            c = c.replace(filas[-1], filas[-1] + "\n" + fila, 1)
            open(cat, "w", encoding="utf-8").write(c + "\n")
        return
    if os.path.isfile(cat):
        c = open(cat, encoding="utf-8").read()
        if f"| `{skill}` |" not in c:
            fila = f"| `{skill}` | por definir | {uso}. | Ver su SKILL.md. | en-prueba |\n"
            ancla = "| `marco-problema-ing` |"
            c = c.replace(ancla, fila + ancla, 1) if ancla in c else c.replace("\n## Rutas", fila + "\n## Rutas", 1)
            open(cat, "w", encoding="utf-8").write(c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--instaladas", default=None)
    ap.add_argument("--aplicar", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--hoy", default=None)
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    hoy = a.hoy or hoy_bogota()
    a.instaladas = buscar_instaladas(a.instaladas)

    propias = skills_propias(a.instaladas)
    en_repo = {d for d in os.listdir(os.path.join(repo, "skills"))
               if os.path.isfile(os.path.join(repo, "skills", d, "SKILL.md"))}
    res = []
    for s in sorted(set(propias) | en_repo):
        inst_dir = os.path.join(a.instaladas, s)
        if s not in propias or not os.path.isdir(inst_dir):
            res.append({"skill": s, "estado": "solo-repo"})
            continue
        estado, arch, faltan = comparar(repo, s, inst_dir)
        fila = {"skill": s, "estado": estado, "instalada_el": propias.get(s),
                "archivos": arch, "en_repo_no_en_claude": faltan}
        if estado in ("nueva", "cambiada"):
            sec = tiene_secretos(inst_dir)
            if sec:
                fila["estado"], fila["secretos"] = "bloqueada", sec
            elif a.aplicar:
                escribir(repo, s, inst_dir, [r for r, e in arch.items() if e in ("nuevo", "cambio-claude")])
                if estado == "nueva":
                    registrar(repo, s, inst_dir, hoy)
                fila["aplicado"] = True
        res.append(fila)

    if a.json:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=2)
        return
    nombres = {"nueva": "NUEVA → se sube", "cambiada": "CAMBIADA en Claude → se sube",
               "reinstalar": "repo más nuevo → Nick debe reinstalar", "conflicto": "CONFLICTO → decide Nick",
               "solo-repo": "solo en el repo (no instalada)", "igual": "igual", "bloqueada": "BLOQUEADA (posible secreto)"}
    for f in res:
        extra = ""
        if f.get("archivos"):
            extra = " — " + ", ".join(f"{r} ({e})" for r, e in f["archivos"].items())
        if f.get("secretos"):
            extra += " — " + "; ".join(f["secretos"])
        if f.get("aplicado"):
            extra += " [aplicado]"
        print(f"- {f['skill']}: {nombres[f['estado']]}{extra}")
    if not a.aplicar and any(f["estado"] in ("nueva", "cambiada") for f in res):
        print("\n(Simulación. Corre con --aplicar para subirlas.)")


if __name__ == "__main__":
    main()

"""Funciones que usan inventario.py y sincronizar.py."""
import glob
import json
import os
import re
from datetime import datetime, timedelta, timezone

# Dónde puede estar la carpeta de skills instaladas, según cómo arranque la sesión.
CANDIDATAS = [
    "/mnt/skills/plugins",
    "/mnt/skills/user",
    "/mnt/skills/private",
    "/mnt/skills/organization",
    "/root/.claude/skills/synced/*",
    os.path.expanduser("~/.claude/skills/synced/*"),
    "/mnt/user-data/skills/*",
]


def _propias_en(carpeta):
    man = os.path.join(carpeta, "manifest.json")
    if not os.path.isfile(man):
        return None
    try:
        data = json.load(open(man, encoding="utf-8"))
    except Exception:
        return None
    return {s["name"] for s in data.get("skills", []) if s.get("source") == "plugin"}


def buscar_instaladas(pedida=None):
    """Devuelve la carpeta de skills instaladas.

    Si se pasa una ruta, se usa esa. Si no, se busca la primera candidata con un
    manifest.json que tenga skills propias (origen plugin) y sus carpetas.
    """
    if pedida:
        return pedida
    vistas = []
    for patron in CANDIDATAS:
        for c in sorted(glob.glob(patron)):
            real = os.path.realpath(c)
            if real in vistas or not os.path.isdir(real):
                continue
            vistas.append(real)
            propias = _propias_en(real)
            if propias and any(os.path.isfile(os.path.join(real, p, "SKILL.md")) for p in propias):
                return c
    raise SystemExit(
        "No encontré la carpeta de skills instaladas (busqué: " + ", ".join(CANDIDATAS) +
        "). Búscala con: find / -name manifest.json -path '*skills*' 2>/dev/null, "
        "y pásala con --instaladas.")


def hoy_bogota():
    return (datetime.now(timezone.utc) - timedelta(hours=5)).strftime("%Y-%m-%d")


def catalogos(repo):
    """{router: (ruta_catalogo, set de skills listadas)} para cada skills/router-*/references/catalogo.md."""
    res = {}
    for ruta in sorted(glob.glob(os.path.join(repo, "skills", "router-*", "references", "catalogo.md"))):
        router = ruta.split(os.sep)[-3]
        listadas = set()
        for linea in open(ruta, encoding="utf-8"):
            m = re.match(r"^\|\s*`([a-z0-9-]+)`", linea)
            if m:
                listadas.add(m.group(1))
        res[router] = (ruta, listadas)
    return res


def router_de(repo, skill, texto_skill=""):
    """Qué router le corresponde a una skill.

    - Si un catálogo de router-* ya la lista, ese router (router-ing solo si es el único).
    - Si la skill es un router (router-x), su propio router.
    - Si su SKILL.md nombra un router-x distinto de router-ing, ese.
    - Si no, router-ing.
    """
    cats = catalogos(repo)
    otros = [r for r, (_, s) in cats.items() if skill in s and r != "router-ing"]
    if otros:
        return otros[0]
    if skill.startswith("router-"):
        return skill
    for r in re.findall(r"router-[a-z0-9]+", texto_skill):
        if r != "router-ing" and r in cats:
            return r
    # Familia por nombre: optica-fisica -> router-fisica.
    for r in cats:
        fam = r[len("router-"):]
        if r != "router-ing" and fam and re.search(rf"(^|-){re.escape(fam)}($|-)", skill):
            return r
    # Familia por vecinos: nombra skills de otro router y ninguna de router-ing.
    nombradas = set(re.findall(r"(?<![\w/.-])[a-z0-9]+(?:-[a-z0-9]+)+(?![\w/.-])", texto_skill)) - {skill}
    ing = cats.get("router-ing", (None, set()))[1]
    if not (nombradas & ing):
        for r, (_, listadas) in cats.items():
            if r != "router-ing" and nombradas & listadas:
                return r
    return "router-ing"

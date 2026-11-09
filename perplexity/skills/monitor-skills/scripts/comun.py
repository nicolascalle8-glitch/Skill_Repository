"""Funciones que usan inventario.py y sincronizar.py."""
import glob
import json
import os
import re
from datetime import datetime, timedelta, timezone

# Dónde puede estar la carpeta de skills instaladas, según dónde corra.
# Perplexity Computer: las skills guardadas aparecen en ~/.perplexity/skills/<nombre>/ después
# de cargarlas por nombre (sin manifest.json). Las rutas de Claude quedan por si se corre allá.
CANDIDATAS_PERPLEXITY = [
    "/home/user/.perplexity/skills",
    os.path.expanduser("~/.perplexity/skills"),
]
CANDIDATAS = CANDIDATAS_PERPLEXITY + [
    "/mnt/skills/plugins",
    "/mnt/skills/user",
    "/mnt/skills/private",
    "/mnt/skills/organization",
    "/root/.claude/skills/synced/*",
    os.path.expanduser("~/.claude/skills/synced/*"),
    "/mnt/user-data/skills/*",
]


# Skills que no son de Nick: las integradas de Perplexity y las que trae Claude.
SKILLS_SISTEMA = {
    # Perplexity Computer
    "create-skill", "office", "media", "search", "website-building", "about-computer",
    "onboarding", "perplexity-platform", "automations", "browser-use", "custom-credentials",
    "business-playbooks", "finance", "gws-best-practices",
    # Claude
    "artifact-emulator", "built-in-browser", "chrome-browser", "computer-use",
    "deep-research", "docs", "docx", "google-workspace", "import-memory", "morning",
    "pdf", "pdf-reading", "pptx", "xlsx", "skill-creator", "file-reading",
    "frontend-design", "product-self-knowledge", "setup-claude", "artifact-design",
    "artifact-capabilities",
}


def excluidas(extra=None):
    """SKILLS_SISTEMA más las que se pasen con --excluir (separadas por coma)."""
    res = set(SKILLS_SISTEMA)
    for e in extra or []:
        res |= {x.strip() for x in e.split(",") if x.strip()}
    return res


def propias_en(carpeta, excluir=None):
    """{nombre: updatedAt o None} de las skills de Nick en una carpeta.

    Con manifest.json (Claude): las de origen plugin. Sin manifest (Perplexity o carpeta
    simple): toda subcarpeta con SKILL.md que no esté en la lista de excluidas.
    """
    excl = excluidas(excluir)
    man = os.path.join(carpeta, "manifest.json")
    if os.path.isfile(man):
        try:
            data = json.load(open(man, encoding="utf-8"))
            return {s["name"]: s.get("updatedAt") for s in data.get("skills", [])
                    if s.get("source") == "plugin" and s["name"] not in excl}
        except Exception:
            pass
    if not os.path.isdir(carpeta):
        return {}
    return {d: None for d in sorted(os.listdir(carpeta))
            if os.path.isfile(os.path.join(carpeta, d, "SKILL.md")) and d not in excl}


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

    Si se pasa una ruta, se usa esa. Si no, la de Perplexity (~/.perplexity/skills) si
    existe; si no, la primera candidata de Claude con un manifest.json que tenga skills
    propias (origen plugin) y sus carpetas.
    """
    if pedida:
        return pedida
    # Perplexity: la carpeta existe aunque no tenga manifest.json.
    for c in CANDIDATAS_PERPLEXITY:
        if os.path.isdir(c):
            return c
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
        "). En Perplexity, carga por nombre las skills de Nick (quedan en "
        "/home/user/.perplexity/skills/<nombre>) y pasa esa carpeta con --instaladas.")


# Carpeta del repo donde viven las versiones de Perplexity. Las de Claude están en skills/
# y esta skill nunca las toca.
CARPETA_SKILLS = os.path.join("perplexity", "skills")


def hoy_bogota():
    return (datetime.now(timezone.utc) - timedelta(hours=5)).strftime("%Y-%m-%d")


def catalogos(repo):
    """{router: (ruta_catalogo, set de skills listadas)} para cada perplexity/skills/router-*/references/catalogo.md."""
    res = {}
    for ruta in sorted(glob.glob(os.path.join(repo, CARPETA_SKILLS, "router-*", "references", "catalogo.md"))):
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


# ---------- Varios repos: qué skill va a qué repo (registry/REPOS.yml) ----------

def ruta_mapa(repo=None):
    """REPOS.yml vive en el repo central (Skill_Repository).

    Busca junto a este script (si corre desde el clon de Skill_Repository) y, si no está
    ahí (por ejemplo, la copia guardada en Perplexity), en <repo>/registry/REPOS.yml."""
    aqui = os.path.dirname(os.path.abspath(__file__))
    junto = os.path.normpath(os.path.join(aqui, "..", "..", "..", "registry", "REPOS.yml"))
    if os.path.isfile(junto) or not repo:
        return junto
    return os.path.join(repo, "registry", "REPOS.yml")


def cargar_mapa(ruta=None, repo=None):
    import yaml
    ruta = ruta or ruta_mapa(repo)
    if not os.path.isfile(ruta):
        return []
    return [r for r in (yaml.safe_load(open(ruta, encoding="utf-8")) or {}).get("repos", [])
            if r.get("estado", "activo") != "cerrado"]


def repo_de_skill(mapa, nombre, descripcion=""):
    """Nombre del repo que guarda esta skill."""
    for r in mapa:
        if nombre in (r.get("skills") or []):
            return r["nombre"]
    for r in mapa:
        for patron in r.get("reconocer") or []:
            if re.search(patron, nombre) or re.search(patron, descripcion or ""):
                return r["nombre"]
    for r in mapa:
        if r.get("por_defecto"):
            return r["nombre"]
    return None


def repo_de_ruta(mapa, ruta):
    """Qué repo del mapa es el clon que está en esta ruta (por su remote de git)."""
    import subprocess
    url = subprocess.run(["git", "-C", ruta, "remote", "get-url", "origin"],
                         capture_output=True, text=True).stdout.strip().lower()
    for r in mapa:
        if r.get("github", "").lower().split("/")[-1] in url.rstrip("/").removesuffix(".git").split("/")[-1:]:
            return r["nombre"]
    return None

# Sincronizar con GitHub (paso a paso)

Léelo antes de correr `scripts/sincronizar.py`. No pide permiso: Nick lo autorizó el
2026-10-24.

Las skills de la cuenta viven en **varios repos**. `registry/REPOS.yml` (en
`Skill_Repository`) dice cuál va a cuál: hoy `Skill_Repository` para las de Nick (por
defecto) y `Skills_Fisica` para las de Valeria (física). Los pasos de abajo se hacen **una
vez por cada repo activo del mapa**, siempre con el script de esta skill. El script solo
toca las skills que el mapa le asigna al repo que le pasas; las demás salen como "va en
otro repo". El mapa lo busca junto al script si corre desde el clon de `Skill_Repository`,
si no en `<ruta-del-repo>/registry/REPOS.yml`; para `Skills_Fisica` pásalo con
`--mapa <clon-de-Skill_Repository>/registry/REPOS.yml`.

El script compara y escribe solo en `perplexity/skills/<skill>/` de cada repo (las versiones de
Claude, en `skills/`, nunca se tocan). El catálogo que actualiza es
`perplexity/skills/router-ing/references/catalogo.md` (o el del router de esa familia).

Solo se ven las skills guardadas en Perplexity que ya se cargaron por nombre en esta sesión
(paso 4 de "Antes de empezar"). Las instaladas en Claude no se ven desde aquí.

1. Clona cada repo con `gh repo clone nicolascalle8-glitch/<repo>` (o `git pull` si ya
   está). Trae historia al clon (el script la necesita para saber qué es más nuevo):
   `git fetch --depth=200 origin main` y `git pull --rebase origin main`.
2. Simula:
   `python3 scripts/sincronizar.py <ruta-del-repo> [--instaladas /home/user/.perplexity/skills] [--excluir a,b] [--mapa <REPOS.yml>]`.
   Sin `--instaladas` usa `/home/user/.perplexity/skills` (y, si no existe, las rutas de
   Claude). Sin `manifest.json`, toda subcarpeta con `SKILL.md` cuenta como de Nick menos
   las integradas de Perplexity (lista en `scripts/comun.py`); si ves otra ajena, quítala
   con `--excluir`. Compara cada skill con el historial del repo, archivo por archivo:
   - **nueva** / **cambiada**: Nick la creó o la cambió en Perplexity → se sube.
   - **reinstalar**: lo guardado es una versión vieja del repo → no se toca; Nick debe
     re-guardar la skill en Perplexity con la versión del repo. Esto evita pisar mejoras
     hechas en el repo.
   - **conflicto**: cambios en los dos lados → no se toca; va como PROPUESTA con lo que
     cambió en cada lado.
   - **bloqueada**: un archivo parece tener una clave o contraseña → no se sube; avísale a
     Nick qué archivo y qué línea (sin repetir la clave).
   - **solo-repo**: está en el repo y no guardada (o no cargada) → no se borra nada; se
     avisa si de verdad no está guardada.
3. Si hay **nueva** o **cambiada**, aplica: el mismo comando con `--aplicar`. Copia los
   archivos y registra las nuevas en `registry/CAPACIDADES.yml` (estado `en-prueba`, etapa
   `por-definir`) y en el catálogo de **su** router: las de otra familia (por ejemplo las de
   física, que tienen `router-fisica`) van al catálogo de ese router, no al de `router-ing`.
   Si el nombre ya lo usa otra capacidad en el registro, la registra con otro nombre para
   no pisarla.
4. Revisa el diff (`git diff --stat` y el diff de cada `SKILL.md`): que no haya borrado de
   contenido grande sin razón y que los YAML carguen. Corre `scripts/inventario.py`: no debe
   dar hallazgos de `registro` nuevos (nombres repetidos, skill en el catálogo equivocado).
   Si algo se ve raro, no hagas push: déjalo como PROPUESTA.
5. Entrada HECHO en `proyectos/skills/BITACORA.md` **del repo que cambió** (en
   `Skill_Repository`, también su copia en Drive con `gws`), con fecha y hora de Bogotá:
   "Sincronización <fecha>" con qué skills se subieron, cuáles hay que re-guardar y cuáles
   quedaron bloqueadas o en conflicto.
6. Commit y push: `sync(skills): <skills subidas>`. Antes, `git fetch origin main` y rebase.
   Si falta autor de git, configúralo desde `gh api user`. Nunca `push --force`.
7. Si no hubo nada que subir, no hagas commit ni entrada; en la corrida diaria, no avises.
8. Si una skill nueva no la reconoce ningún repo y por su tema no parece de Nick (por
   ejemplo, es para otra persona), no la subas al repo por defecto: avísale a Nick y
   propón agregarla a `registry/REPOS.yml`.

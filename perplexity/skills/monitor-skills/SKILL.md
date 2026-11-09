---
name: monitor-skills
description: "Revisa las skills de Nick: cuál sobra, cuál actualizar o mejorar y qué skill crear según sus sesiones, con evidencia; y sube solas a GitHub las que guardó o cambió en Perplexity. Úsala con \"revisa mis skills\", \"sincroniza mis skills\" o \"guardé una skill\". No elige skill para una tarea (router-ing), no limpia memoria (depurador-recursos) ni revisa las de física (monitor-skills-fisica)."
metadata:
  perplexity:
    connectors:
      - id: github_mcp_direct
        reason: Lee y escribe los repos Skill_Repository y Skills_Fisica (skills, registro, bitácoras, reportes).
      - id: google_drive
        reason: Copia las entradas de bitácora en Drive (shared/BITACORA-DRIVE.md).
---

# Monitor de skills

Las skills se van acumulando: unas se quedan viejas, otras se pisan entre sí, y lo que
Nick repite en sus sesiones a veces nunca se vuelve skill. Esta skill mira el conjunto
completo, cruza eso con lo que Nick realmente ha hecho y le entrega un reporte corto con
cuatro respuestas: **qué sobra, qué actualizar, qué mejorar y qué crear**. Todo con
evidencia, y nada se cambia sin su sí, con una excepción: **subir al repo lo que Nick ya
guardó en Perplexity** se hace solo (lo decidió Nick el 2026-10-24), porque así el repo es
siempre copia de lo que él usa.

Escríbele a Nick en español simple y directo. El reporte es para leerlo en dos minutos.

Mandan `CONTRATO.md` (aprobaciones, historial que no se borra) y
`shared/PLANTILLA-SKILL.md` (cómo es una skill de Nick y qué falta para marcarla activa),
leídos desde el clon del repo.

**Dos carpetas en el repo.** Las versiones de Perplexity viven en `perplexity/skills/`; las de
Claude, en `skills/`. Esta skill (y sus scripts) solo leen y escriben `perplexity/skills/`.
Nunca toques `skills/`: si una versión de Claude quedó atrás de la de Perplexity, dilo como
PROPUESTA y que la actualice Claude.

**Desde Perplexity no se ven las skills instaladas en Claude.** Solo se comparan las
guardadas en Perplexity con el repo. Si Nick cambió algo en Claude, tiene que subirlo desde
allá o guardarlo también aquí. Dilo en "Lo que no pude revisar".

## Antes de empezar

1. Repo `nicolascalle8-glitch/Skill_Repository`: `gh repo clone nicolascalle8-glitch/Skill_Repository`
   (o `git pull` si ya está clonado). Sin repo, revisa solo las skills guardadas y dilo en
   una línea.
2. Lee de `proyectos/skills/BITACORA.md`: **Propuestas sin respuesta** y las entradas del
   monitor anteriores (busca "Revisión de skills"). Lo que Nick ya **rechazó** no se vuelve
   a proponer salvo que haya evidencia nueva; si la hay, dila.
3. Lee el último reporte en `proyectos/skills/monitor/` (si existe). Su fecha marca desde
   cuándo buscar actividad nueva. Si no hay, mira los últimos 30 días.
4. **Trae las skills guardadas a la sesión.** En Perplexity, una skill guardada solo aparece
   en `/home/user/.perplexity/skills/<nombre>/` después de cargarla por nombre. Lista las
   skills personales de Nick (skill `perplexity-platform`, guía de Skills marketplace,
   alcance individual) y carga por nombre cada una que no sea integrada, más las de
   `perplexity/skills/` del repo. Una que no carga no está guardada en Perplexity.
5. **Sincroniza primero** (sección siguiente). Así la revisión mira las skills al día.
6. Si Nick pidió algo puntual ("¿selector-ia sirve?", "¿me falta una skill para X?"),
   reduce el alcance a eso y salta los pasos que no apliquen.

## Sincronizar con GitHub (automático)

Corre al empezar cualquier revisión, cuando Nick dice "sube mis skills" o "guardé/cambié
una skill", y a diario como automatización. No pide permiso: Nick ya lo autorizó.

Siempre con `scripts/sincronizar.py` (primero simulación, luego `--aplicar` solo si hay
**nueva** o **cambiada**). **Lee `references/sincronizar.md` antes de correrlo**: tiene los
pasos por repo (`registry/REPOS.yml`), qué significa cada estado, las revisiones antes del
push, la entrada de bitácora y el commit. Si no hubo nada que subir, no hay commit ni
entrada; en la corrida diaria, no avises.

El repo nunca pierde archivos por la sincronización: el script solo agrega o actualiza.

## Cómo se hace

### 1. Inventario automático

```bash
python3 scripts/inventario.py <ruta-repo> [--instaladas /home/user/.perplexity/skills] [--excluir a,b]
```

Compara repo, skills guardadas (`/home/user/.perplexity/skills`, ya cargadas en el paso 4),
`registry/CAPACIDADES.yml` y el catálogo del router. Sin `manifest.json`, toda subcarpeta
con `SKILL.md` cuenta como de Nick menos las integradas de Perplexity (lista en
`scripts/comun.py`); otras ajenas se quitan con `--excluir`. Saca lo mecánico: skills que
están en un lado y no en el otro, texto guardado distinto al del repo, encabezados malos,
archivos nombrados que no existen, skills registradas que no están. Produce: tabla de
inventario y hallazgos automáticos. No los repitas uno por uno en el reporte: agrúpalos por
skill. "Está en el repo pero no guardada" puede ser solo que no se cargó: confírmalo con la
lista del paso 4 antes de reportarlo.

### 2. Leer cada skill de Nick

Lee el `SKILL.md` de cada skill propia (no las integradas de Perplexity) y sus
`references/` si hace falta para juzgar. Las skills que `registry/REPOS.yml` manda a otro
repo (hoy las de física de Valeria, en Skills_Fisica) no se revisan aquí: las revisa
`monitor-skills-fisica`. Sí se sincronizan, y sí se miran sus choques con las de Nick.
Busca, con los criterios de `references/criterios.md`:

- **Choques**: dos descripciones que se disparan con las mismas frases, o dos skills que
  hacen el mismo trabajo. Cita las frases que chocan.
- **Contradicciones** entre skills, o con `CONTRATO.md` y `shared/CONTRATO-OPERATIVO.md`.
- **Datos que vencen**: catálogos, planes, modelos o normas con fecha de revisión de más
  de 30 días.
- **Skills `en-prueba`** que ya llevan tiempo sin el caso real que les falta.

Produce: notas por skill.

### 3. Mirar lo que Nick ha estado haciendo

Esta es la parte que vuelve útil al monitor: las propuestas salen del uso real, no de
ideas sueltas.

- **Sesiones**: con las herramientas de memoria sobre sesiones pasadas (alcance personal),
  lista las sesiones desde la fecha del último reporte (máximo 100; si no alcanzó, dilo).
  Clasifica por título. Abre solo las que parezcan un procedimiento repetido o una
  corrección (máximo 5). Si corres dentro de un Project de Perplexity y solo ves las
  sesiones de ese Project, dilo en el reporte.
- **Uso de skills**: busca en las sesiones el nombre de cada skill propia para ver si se
  usó y si Nick tuvo que corregir el resultado ("no", "otra vez", "eso no", "te dije").
- **Bitácoras**: últimas 10 entradas de cada `proyectos/*/BITACORA.md`. Sirven para ver
  qué trabajo se repite y qué salió mal.
- **Memoria**: los temas guardados en la memoria de Perplexity dicen en qué anda Nick.
  Úsalos como pista de temas, no como evidencia de uso.

Anota cada señal con su prueba (link de la sesión o entrada de bitácora y fecha). Produce:
lista de señales.

### 4. Decidir

Aplica `references/criterios.md` a cada skill y a cada señal. Cada skill queda en una sola
casilla: **mantener**, **actualizar**, **mejorar**, **fusionar** o **retirar**. Las
señales sin skill pasan a **crear** o se descartan.

Reglas para no inflar:

- Antes de proponer una skill nueva, mira si cabe mejorando una que ya existe. Menos
  skills que funcionen bien vale más que muchas a medias.
- Mira primero `registry/CAPACIDADES.yml`: si lo que falta ya está como `pendiente` o
  `hueco`, la propuesta es **activarla** (con el caso real que apareció), no inventar otra.
- Máximo 3 propuestas de crear y 3 de mejorar por revisión, ordenadas por cuánto le
  ahorran a Nick. Lo demás va en una línea "también vi".
- Una skill con menos de 30 días no se propone retirar: "muy nueva para juzgar".
- Si no encontraste nada importante, dilo así. Un reporte vacío honesto sirve más que uno
  relleno.

### 5. Entregar el reporte

Usa el formato de `references/plantilla-reporte.md`. Cada propuesta lleva su evidencia; sin
evidencia, no va.

### 6. Preguntar qué se aplica

Pregúntale a Nick qué aplica, con una opción por propuesta grande más "nada por ahora"
(puede elegir varias). Lo que Nick apruebe:

- **Crear o mejorar**: sigue el flujo de la skill `create-skill` (borrador, prueba con un
  caso real, revisión de Nick). Si Nick quiere verlo antes, muéstrale la propuesta para que
  la revise y la guarde. Al terminar, regístrala en `registry/CAPACIDADES.yml` y en el
  catálogo del router en el mismo commit.
- **Actualizar** (catálogos, referencias rotas, sincronía repo ↔ guardada): hazlo y dile a
  Nick qué skills tiene que re-guardar en Perplexity (con la versión del repo).
- **Fusionar o retirar**: no se borra nada. La skill se marca `retirada` en
  `CAPACIDADES.yml` con la razón y la fecha, se quita del catálogo del router y las otras
  skills dejan de nombrarla. Nick la quita a mano en la página de Skills de Perplexity
  (y en Claude si también la tiene); dile cómo en una línea.

Lo que no apruebe ni rechace queda como **PROPUESTA** en la bitácora.

### 7. Dejar registro

1. Guarda el reporte en `proyectos/skills/monitor/AAAA-MM-DD.md` (se agrega uno por
   revisión, no se reescriben los viejos).
2. Entrada en `proyectos/skills/BITACORA.md`: tipo HECHO, título "Revisión de skills
   <fecha>", con el resumen (cuántas sobran, actualizar, mejorar, crear) y la ruta del
   reporte. Una entrada PROPUESTA por cada propuesta grande sin respuesta, y su línea en
   **Propuestas sin respuesta**. Copia todo igual en Drive (`shared/BITACORA-DRIVE.md`)
   con `gws` (carga antes `gws-best-practices`); si Drive falla, anota "Drive: pendiente
   de copiar" y sigue.
3. Commit y push: `perplexity(skills): revisión AAAA-MM-DD` (Perplexity Computer
   (<modelo>) firma). Antes, `git fetch origin main` y rebase. Si falta autor de git,
   configúralo desde `gh api user`.

## Corridas programadas (sin Nick al frente)

La sincronización diaria y la revisión semanal corren como automatizaciones de Perplexity
(skill `automations`). **Cuando corres desde una automatización, o Nick pide crear o
cambiar esas corridas, lee `references/revision-semanal.md`**: dice qué se aplica solo, qué
queda como PROPUESTA y cómo avisar con una notificación.

## Verificación

- Cargaste las skills guardadas de Nick antes de correr los scripts.
- Corriste `scripts/inventario.py` y sus hallazgos están en el reporte (agrupados) o
  explicados.
- Cada propuesta tiene evidencia con link o entrada de bitácora y fecha. Ninguna sale solo
  de tu opinión.
- No propusiste algo que Nick ya rechazó sin decir qué evidencia nueva hay.
- Antes de decir que una skill "no se usa", buscaste su nombre en las sesiones.
- La sincronización corrió y su resultado está en el reporte (subidas, re-guardar,
  bloqueadas, conflictos).
- Si cambiaste skills: pasan `agentskills validate <carpeta>`, `CAPACIDADES.yml` carga
  como YAML y vuelves a correr `scripts/inventario.py` sin hallazgos nuevos.

## Límites

- No elige qué skill usar para una tarea (`router-ing`), ni qué IA o modelo
  (`selector-ia`).
- No limpia memoria, docs del proyecto ni sesiones (`depurador-recursos`); si el problema
  que ves es ese, recomiéndala en una línea.
- No revisa ni cambia las skills integradas de Perplexity; solo puede decir si una de Nick
  repite lo que ya hace una de ellas.
- No borra skills ni archivos, ni en Perplexity ni en el repo: marca, propone y le dice a
  Nick qué hacer a mano.
- No guarda ni re-guarda skills en Perplexity por su cuenta: eso lo aprueba Nick. Cuando el
  repo va adelante, dile cuáles re-guardar.
- No ve ni toca las skills instaladas en Claude.
- No instala skills externas; para evaluar una de terceros, usa `router-ing`.

## Acceso a las otras skills de Nick

Todas las skills de Nick están guardadas en Perplexity. Carga de fondo `contexto-nick` (quién es Nick) y `cerebro-nick` (cómo decide Nick) si
todavía no están en la sesión. Cuando esta skill nombre otra, cárgala por su nombre antes de
pasarle el trabajo; si no carga, léela en `perplexity/skills/<nombre>/SKILL.md` del repo
`nicolascalle8-glitch/Skill_Repository`. El mapa completo está en el catálogo de `router-ing`.

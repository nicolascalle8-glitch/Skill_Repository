---
name: monitor-skills
description: >-
  Revisa todas las skills de Nick y le dice cuál sobra, cuál hay que actualizar o mejorar
  y qué skill nueva le conviene crear según lo que ha venido haciendo en sus chats y
  proyectos, con evidencia. Además detecta las skills que Nick creó o cambió en Claude y
  las sube solas al repo de GitHub. Corre a diario (sincronizar) y cada semana (revisión).
  Úsala cuando Nick pida revisar, auditar u ordenar sus skills, pregunte si alguna sobra,
  está vieja, choca con otra o le falta algo, qué skill debería crear o mejorar, o diga
  "revisa mis skills", "sube mis skills", "sincroniza las skills con GitHub" o que guardó
  o cambió una skill, aunque no nombre la skill. No sirve para elegir qué skill usar en una tarea concreta
  (eso es router-ing) ni para limpiar memoria o chats (eso es depurador-recursos).
---

# Monitor de skills

Las skills se van acumulando: unas se quedan viejas, otras se pisan entre sí, y lo que
Nick repite en sus chats a veces nunca se vuelve skill. Esta skill mira el conjunto
completo, cruza eso con lo que Nick realmente ha hecho y le entrega un reporte corto con
cuatro respuestas: **qué sobra, qué actualizar, qué mejorar y qué crear**. Todo con
evidencia, y nada se cambia sin su sí, con una excepción: **subir al repo lo que Nick ya
guardó en Claude** se hace solo (lo decidió Nick el 2026-10-24), porque así el repo es
siempre copia de lo que él usa.

Escríbele a Nick en español simple y directo. El reporte es para leerlo en dos minutos.

Mandan `CONTRATO.md` (aprobaciones, historial que no se borra) y
`shared/PLANTILLA-SKILL.md` (cómo es una skill de Nick y qué falta para marcarla activa).

## Antes de empezar

1. Repo `nicolascalle8-glitch/Skill_Repository`. Si no está en la sesión, agrégalo con
   `add_repo` (acceso `push`) y clónalo. Haz `git pull` para tener lo último. Sin repo,
   revisa solo las skills instaladas y dilo en una línea.
2. Lee de `proyectos/skills/BITACORA.md`: **Propuestas sin respuesta** y las entradas del
   monitor anteriores (busca "Revisión de skills"). Lo que Nick ya **rechazó** no se vuelve
   a proponer salvo que haya evidencia nueva; si la hay, dila.
3. Lee el último reporte en `proyectos/skills/monitor/` (si existe). Su fecha marca desde
   cuándo buscar actividad nueva. Si no hay, mira los últimos 30 días.
4. **Sincroniza primero** (sección siguiente). Así la revisión mira las skills al día.
5. Si Nick pidió algo puntual ("¿selector-ia sirve?", "¿me falta una skill para X?"),
   reduce el alcance a eso y salta los pasos que no apliquen.

## Sincronizar con GitHub (automático)

Corre al empezar cualquier revisión, cuando Nick dice "sube mis skills" o "guardé/cambié
una skill", y a diario como tarea programada. No pide permiso: Nick ya lo autorizó.

1. Trae historia al clon (el script la necesita para saber qué es más nuevo):
   `git fetch --depth=200 origin main` y `git pull --rebase origin main`.
2. Simula: `python3 skills/monitor-skills/scripts/sincronizar.py <ruta-repo>`.
   El script busca solo la carpeta de skills instaladas (cambia según la sesión:
   `/mnt/skills/plugins`, `/mnt/skills/user`, `~/.claude/skills/synced/<id>`…) y usa las de
   origen `plugin` en su `manifest.json`. Si no la encuentra, el error dice cómo buscarla y
   se pasa con `--instaladas`. Compara cada skill con el historial del repo, archivo por
   archivo:
   - **nueva** / **cambiada**: Nick la creó o la cambió en Claude → se sube.
   - **reinstalar**: lo instalado es una versión vieja del repo → no se toca; Nick debe
     reinstalar el `.skill`. Esto evita pisar mejoras hechas en el repo.
   - **conflicto**: cambios en los dos lados → no se toca; va como PROPUESTA con lo que
     cambió en cada lado.
   - **bloqueada**: un archivo parece tener una clave o contraseña → no se sube; avísale a
     Nick qué archivo y qué línea (sin repetir la clave).
   - **solo-repo**: está en el repo y no instalada → no se borra nada; se avisa.
3. Si hay **nueva** o **cambiada**, aplica: el mismo comando con `--aplicar`. Copia los
   archivos y registra las nuevas en `registry/CAPACIDADES.yml` (estado `en-prueba`, etapa
   `por-definir`) y en el catálogo de **su** router: las de otra familia (por ejemplo las de
   física, que tienen `router-fisica`) van al catálogo de ese router, no al de `router-ing`.
   Si el nombre ya lo usa otra capacidad en el registro, la registra con otro nombre para
   no pisarla.
4. Revisa el diff (`git diff --stat` y el diff de cada `SKILL.md`): que no haya borrado de
   contenido grande sin razón y que los YAML carguen. Corre `inventario.py`: no debe dar
   hallazgos de `registro` nuevos (nombres repetidos, skill en el catálogo equivocado).
   Si algo se ve raro, no hagas push: déjalo como PROPUESTA.
5. Entrada HECHO en `proyectos/skills/BITACORA.md` (y su copia en Drive), con fecha y hora
   de Bogotá: "Sincronización <fecha>" con qué skills se subieron, cuáles hay que reinstalar y cuáles
   quedaron bloqueadas o en conflicto.
6. Commit y push: `sync(skills): <skills subidas>`. Antes, `git fetch origin main` y rebase.
   Nunca `push --force`.
7. Si no hubo nada que subir, no hagas commit ni entrada; en la tarea diaria, no avises.

El repo nunca pierde archivos por la sincronización: el script solo agrega o actualiza.

## Cómo se hace

### 1. Inventario automático

```bash
python3 skills/monitor-skills/scripts/inventario.py <ruta-repo>
```

Compara repo, skills instaladas (`/mnt/skills/plugins`), `registry/CAPACIDADES.yml` y el
catálogo del router. Saca lo mecánico: skills que están en un lado y no en el otro, texto
instalado distinto al del repo, encabezados malos, archivos nombrados que no existen,
skills registradas que no están. Produce: tabla de inventario y hallazgos automáticos.
No los repitas uno por uno en el reporte: agrúpalos por skill.

### 2. Leer cada skill de Nick

Lee el `SKILL.md` de cada skill propia (no las de Anthropic que vienen con Claude) y sus
`references/` si hace falta para juzgar. Busca, con los criterios de
`references/criterios.md`:

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

- **Chats**: `recent_chats` desde la fecha del último reporte (20 por llamada, paginando
  con `before`, máximo 5 llamadas; si no alcanzó, dilo). Clasifica por título. Abre con
  `read_conversation` solo los que parezcan un procedimiento repetido o una corrección
  (máximo 5 chats, 1 página cada uno). Los chats que ves dependen de dónde corres: dentro
  de un proyecto de claude.ai solo ves los de ese proyecto. Dilo en el reporte.
- **Uso de skills**: `conversation_search` con el nombre de cada skill propia para ver si
  se usó y si Nick tuvo que corregir el resultado ("no", "otra vez", "eso no", "te dije").
- **Bitácoras**: últimas 10 entradas de cada `proyectos/*/BITACORA.md`. Sirven para ver
  qué trabajo se repite y qué salió mal.
- **Memoria**: la lista de archivos de memoria (áreas y temas) dice en qué anda Nick.
  Úsala como pista de temas, no como evidencia de uso.

Anota cada señal con su prueba (link del chat o entrada de bitácora y fecha). Produce:
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

Con AskUserQuestion (multiSelect), una opción por propuesta grande más "nada por ahora".
Lo que Nick apruebe:

- **Crear o mejorar**: sigue el flujo de `skill-creator` (borrador, prueba con un caso
  real, revisión de Nick). Si Nick quiere verlo antes, muestra la propuesta con
  `propose_skills` (tarjeta para revisar y guardar). Al terminar, regístrala en
  `registry/CAPACIDADES.yml` y en el catálogo del router en el mismo commit.
- **Actualizar** (catálogos, referencias rotas, sincronía repo ↔ instalada): hazlo y
  entrega los `.skill` que Nick tiene que reinstalar.
- **Fusionar o retirar**: no se borra nada. La skill se marca `retirada` en
  `CAPACIDADES.yml` con la razón y la fecha, se quita del catálogo del router y las otras
  skills dejan de nombrarla. Nick la desinstala a mano en Claude; dile cómo en una línea.

Lo que no apruebe ni rechace queda como **PROPUESTA** en la bitácora.

### 7. Dejar registro

1. Guarda el reporte en `proyectos/skills/monitor/AAAA-MM-DD.md` (se agrega uno por
   revisión, no se reescriben los viejos).
2. Entrada en `proyectos/skills/BITACORA.md`: tipo HECHO, título "Revisión de skills
   <fecha>", con el resumen (cuántas sobran, actualizar, mejorar, crear) y la ruta del
   reporte. Una entrada PROPUESTA por cada propuesta grande sin respuesta, y su línea en
   **Propuestas sin respuesta**. Copia todo igual en Drive (`shared/BITACORA-DRIVE.md`);
   si Drive falla, anota "Drive: pendiente de copiar" y sigue.
3. Commit y push: `monitor(skills): revisión AAAA-MM-DD`. Antes, `git fetch origin main`
   y rebase.

## Revisión semanal (sin Nick al frente)

Cuando corre como tarea programada nadie responde preguntas:

- Primero sincroniza (eso sí se aplica solo). Luego haz los pasos 1 a 5 y 7. En el paso 6
  no apliques nada: todo queda como PROPUESTA.
- Si desde el último reporte no hubo chats nuevos ni cambios en el repo, no hagas
  reporte: deja solo una línea en la bitácora ("Revisión semanal: sin actividad nueva").
- Al final manda con `SendUserMessage` el resumen corto del reporte (las 4 respuestas y
  las propuestas) y dónde quedó. Si el semáforo es rojo, que sea lo primero que diga.

## Verificación

- Corriste `inventario.py` y sus hallazgos están en el reporte (agrupados) o explicados.
- Cada propuesta tiene evidencia con link o entrada de bitácora y fecha. Ninguna sale solo
  de tu opinión.
- No propusiste algo que Nick ya rechazó sin decir qué evidencia nueva hay.
- Antes de decir que una skill "no se usa", buscaste su nombre en los chats.
- La sincronización corrió y su resultado está en el reporte (subidas, reinstalar,
  bloqueadas, conflictos).
- Si cambiaste skills: pasan `quick_validate` de `skill-creator`, `CAPACIDADES.yml` carga
  como YAML y vuelves a correr `inventario.py` sin hallazgos nuevos.

## Límites

- No elige qué skill usar para una tarea (`router-ing`), ni qué IA o modelo
  (`selector-ia`).
- No limpia memoria, docs del proyecto ni chats (`depurador-recursos`); si el problema que
  ves es ese, recomiéndala en una línea.
- No revisa ni cambia las skills de Anthropic que vienen con Claude; solo puede decir si
  una de Nick repite lo que ya hace una de ellas.
- No borra skills ni archivos, ni en Claude ni en el repo: marca, propone y le dice a Nick
  qué hacer a mano.
- No instala ni reinstala skills en Claude: eso lo hace Nick con el `.skill`. Cuando el repo
  va adelante, entrégale los `.skill` empaquetados.
- No instala skills externas; para evaluar una de terceros, usa `router-ing`.

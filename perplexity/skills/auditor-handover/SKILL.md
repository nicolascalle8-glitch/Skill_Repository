---
name: auditor-handover
description: "Audita si esta sesión (o un Project completo de Perplexity) está saturada y perdiendo calidad, da puntaje y semáforo y, si Nick quiere, arma HANDOVER y CONTEXTO en GitHub para seguir en una sesión nueva sin perder nada. Úsala si dice que las respuestas empeoran, la sesión está lenta u olvidadiza, pide auditar, hacer handover o traspaso. Para limpiar memoria, archivos o sesiones viejas: depurador-recursos."
metadata:
  perplexity:
    connectors:
      - id: github_mcp_direct
        reason: Lee y escribe proyectos/<proyecto>/ en Skill_Repository (CONTEXTO, HANDOVER, BITACORA, archivos).
      - id: google_drive
        reason: Copia la entrada de la bitácora al Doc de Drive del proyecto; sin Drive queda "pendiente de copiar".
---

# Auditor de sesión + Handover

Una sesión larga se degrada: entre más texto acumula, más se diluyen las instrucciones del inicio, se mezclan temas, se olvidan decisiones y las respuestas se vuelven genéricas. Esta skill hace dos cosas:

1. **Auditoría**: mide qué tan degradada está la sesión (o el Project) y da un veredicto honesto.
2. **Handover**: si Nick quiere, deja dos archivos por proyecto en GitHub:
   - `CONTEXTO.md` — corto (~1.500 palabras), se reescribe cada vez. Es lo **único** que la sesión nueva lee para arrancar, así no tiene que releer la sesión vieja ni el historial completo y no gasta tokens en eso.
   - `HANDOVER.md` — la trazabilidad completa: decisiones, hitos, tiempos, pendientes e historial con fechas que nunca se borra. Se consulta solo si hace falta saber cuándo o por qué cambió algo.

El usuario es Nick. Escríbele en español simple y directo. El handover también va en español simple: lo va a leer él y otra sesión (de Perplexity o de otra IA), no un comité.

## Paso 1 — Preguntar el alcance

Antes de auditar, pregunta a Nick (con opciones) qué se audita:

- **Esta sesión** (lo normal: la skill se corre al final de la sesión que está fallando).
- **El Project completo** (todas las sesiones del Project de Perplexity donde estás).

Pregunta también, en la misma tanda, **a qué proyecto pertenece** el trabajo, para saber en qué carpeta de GitHub archivar. Propón un nombre corto en minúsculas con guiones (ej. `arde-la-selva`, `fabrica-medias`) deducido del tema, y deja que lo corrija.

## Paso 2 — Reunir la evidencia

No audites de memoria vaga. Primero relee lo que realmente pasó.

**Si es esta sesión:**
- Recorre la sesión completa de principio a fin. Si los turnos del inicio ya no están en tu contexto (o ves un resumen en vez de los mensajes originales), búscalos con las herramientas de memoria sobre sesiones pasadas (`memory_search` / `memory_read`, alcance personal). Que los turnos del inicio ya no estén visibles es, en sí mismo, una señal fuerte de saturación: anótalo.
- Mientras lees, saca una lista cruda (para ti) de: decisiones, cambios de rumbo, hitos, archivos/links/entregables, pendientes, correcciones que Nick tuvo que hacer, y respuestas tuyas que se contradicen.

**Si es el Project completo:**
- Carga la skill `perplexity-platform` para ver los archivos, instrucciones y sesiones del Project.
- Ubica las sesiones del Project con `memory_search` / `memory_list`. Abre solo las que importan (`memory_read`, lo justo de cada una), no todo.
- Si existe `proyectos/<proyecto>/CONTEXTO.md` o `BITACORA.md` en el repo, léelos como referencia del estado anterior.

Cuenta lo que se pueda contar: número de turnos de Nick, número aproximado de temas distintos, número de correcciones, número de veces que se repitió una pregunta o una explicación.

## Paso 3 — Calificar

Lee `references/criterios-auditoria.md` y califica cada criterio de 0 a 10 (10 = perfecto, 0 = muy mal), con la evidencia concreta que justifica el número (cita el turno o el tema, no generalidades). Luego calcula el puntaje total y el semáforo con la regla de ese archivo.

Sé honesto, no complaciente: si la sesión está bien, dilo; si está mal, dilo aunque Nick esté de buen humor. Tampoco exageres para "vender" el handover. Y aclara una vez, sin drama, que no tienes un medidor exacto de tu capacidad interna: el puntaje se basa en señales observables, no en un contador de tokens.

## Paso 4 — Entregar el reporte

Formato del reporte en la sesión:

```
## Auditoría — <proyecto> — <fecha>
Alcance: <esta sesión | Project completo>
Semáforo: 🟢 / 🟡 / 🔴  — Puntaje: <X>/100

| Criterio | Puntaje | Evidencia |
|---|---|---|
| ... | x/10 | ... |

**Qué está fallando:** 2–4 frases concretas.
**Recomendación:** seguir aquí / hacer handover y abrir sesión nueva / dividir en varias sesiones por tema.
```

Si recomiendas dividir, di en qué sesiones (ej. "una para la web, otra para la cotización").

Si en la auditoría ves que el problema no es esta sesión sino lo que carga cada sesión (memoria inflada, archivos del Project pesados, muchas sesiones repetidas del mismo tema), dilo en una línea y recomienda `depurador-recursos` después del handover.

## Paso 5 — Preguntar si arma el handover

No lo armes solo. Pregunta a Nick: "¿Armo el handover?" con opciones claras (sí / no / sí, pero solo de un tema). Si el semáforo es verde, igual pregunta, pero dile que no es urgente.

## Paso 6 — Armar el handover y el contexto

Si el proyecto es `horno-vertical`, salta al caso especial del paso 7: no lleva HANDOVER ni CONTEXTO.

Lee `references/plantilla-handover.md` y `references/plantilla-contexto.md`. Primero llena el HANDOVER (es el registro completo) y después destila de ahí el CONTEXTO (es lo que la sesión nueva realmente carga). La razón de separarlos: el HANDOVER crece con cada actualización y leerlo entero al arrancar volvería a llenar la sesión nueva; el CONTEXTO se mantiene del mismo tamaño siempre.

Para el CONTEXTO, pregúntate en cada línea: "¿la sesión nueva necesita esto para hacer la siguiente tarea sin preguntarle a Nick?". Si no, va solo en el HANDOVER. Pon los datos exactos (cifras, nombres, URLs, versiones), no resúmenes vagos, porque un resumen vago obliga a la sesión nueva a volver a preguntar. Lo largo (código, textos aprobados extensos, tablas) va a `proyectos/<proyecto>/archivos/` y el CONTEXTO solo lo apunta con cuándo abrirlo.

Reglas para los dos:

- **Solo hechos de la sesión.** Si algo no se decidió, va en "Pendientes" o "Preguntas abiertas", no en "Decisiones".
- **Distingue quién dijo qué.** Una propuesta tuya que Nick no aceptó explícitamente no es una decisión.
- **Fechas reales.** Usa las fechas/horas de los mensajes cuando se vean; si no, pon "aprox." Usa la hora de Bogotá (UTC-5).
- **Incluye "No volver a discutir"**: lo que ya se cerró, para que la sesión nueva no reabra temas resueltos.
- **Incluye el "Mensaje de arranque"**: un bloque corto que Nick pega como primer mensaje de una sesión nueva de Perplexity (o de cualquier otra IA). Le dice que lea **solo el CONTEXTO.md**, no el HANDOVER ni la sesión vieja.
- Sin datos sensibles innecesarios: nada de contraseñas, tokens, números de cuenta o documentos de identidad, aunque aparezcan en la sesión. Si son necesarios para el trabajo, escribe "(ver en <dónde>)".

## Paso 7 — Archivar en GitHub (sin borrar lo anterior)

Repositorio: `nicolascalle8-glitch/Skill_Repository` (privado). Por proyecto:

```
proyectos/<proyecto>/
  CONTEXTO.md    se reescribe completo cada vez (no crece)
  HANDOVER.md    se actualiza sin borrar (crece con el historial)
  BITACORA.md    entrada nueva arriba (copia idéntica en Drive)
  archivos/      código, textos largos, tablas que el CONTEXTO apunta
```

1. Clona con `gh repo clone nicolascalle8-glitch/Skill_Repository` (o `git pull` si ya está clonado). Si GitHub no está disponible, salta al punto 8 de esta lista.
2. Si la carpeta `proyectos/<proyecto>/` no existe, **pregunta a Nick antes de crearla** (puede que el proyecto tenga otro nombre ya).
3. Si `HANDOVER.md` **no existe**: créalo con la plantilla completa y una primera entrada en el historial.
4. Si **ya existe**: léelo completo y actualízalo así, nunca borrando:
   - Reescribe la sección **Estado actual** (arriba) con lo vigente hoy.
   - Lo que ya no aplica no se borra: pásalo al historial marcado como `~~cerrado~~` o `reemplazado por: ...`.
   - Agrega una **entrada nueva al inicio del "Historial de actualizaciones"** con fecha y hora, puntaje de la auditoría y qué cambió desde la entrada anterior (decisiones nuevas, hitos cumplidos, pendientes cerrados y abiertos).
   - Actualiza la línea `Última actualización:` del encabezado.
5. Escribe `CONTEXTO.md` completo desde cero (si ya existía, se sobrescribe: su versión anterior queda en el historial de git y el HANDOVER guarda la trazabilidad). Revisa que no pase de ~1.500 palabras con `wc -w`; si pasa, comprime o mueve cosas a `archivos/`.
6. Guarda en `archivos/` lo largo que la sesión nueva pueda necesitar y que no viva ya en otro lado.
6b. **Bitácora del proyecto (GitHub y Google Drive).** Agrega una entrada HECHO arriba en `proyectos/<proyecto>/BITACORA.md` (créala con la plantilla de `perplexity/skills/colaboracion-ias/references/plantilla-bitacora.md` del repo si no existe), firmada `Perplexity Computer (<modelo>)`: "Handover <fecha> — <semáforo> <puntaje>/100", qué cambió y la siguiente tarea. Copia la misma entrada al Doc de Drive siguiendo `references/bitacora-drive-gws.md` (si el proyecto no tiene carpeta en Drive, créala ahí mismo y regístrala en `registry/DRIVE.yml`). Si Drive no responde, anota "Drive: pendiente de copiar" y sigue.
7. Haz commit y push a `main`:
   - Si falta el autor de git, configúralo desde `gh api user` antes del commit.
   - `git fetch origin main` y rebase si hace falta antes de empujar. Nada de `push --force`.
   - Mensaje: `handover(<proyecto>): <fecha> — <semáforo> <puntaje>/100`
8. Si no se pudo empujar a GitHub, comparte los archivos con Nick y di en una línea por qué no quedó en GitHub.

**Caso especial `horno-vertical`** (CONTRATO.md, sección 7): no se crea ni se actualiza HANDOVER ni CONTEXTO, y no hay copia en Drive. En su lugar: actualiza el estado y los pasos pendientes en `proyectos/horno-vertical/PLAN.md` (sin borrar pasos: los cerrados se marcan) y agrega arriba en su `BITACORA.md` una entrada corta con el formato de 3 líneas que trae ese archivo (Hecho / Verificado / Sigue), con el semáforo y puntaje en "Hecho". El Mensaje de arranque apunta a `PLAN.md` en vez de `CONTEXTO.md`. Lo viejo de `archivo/` no se toca. Commit igual que en el punto 7.

## Paso 8 — Cerrar

En la sesión entrega:
1. El **Mensaje de arranque** en un bloque de código, listo para copiar. Debajo, dentro del mismo bloque, pega el CONTEXTO.md completo (o el PLAN.md en `horno-vertical`): así sirve aunque la IA que lo reciba no tenga acceso a GitHub.
2. Una línea con dónde quedó archivado (ruta en GitHub y link de la bitácora en Drive), cuántas palabras tiene el CONTEXTO, o por qué no se pudo archivar.

Nada más. No repitas el reporte ni el handover completo.

## Acceso a las otras skills de Nick

Todas las skills de Nick están guardadas en Perplexity. Carga de fondo `contexto-nick` (quién es Nick) y `cerebro-nick` (cómo decide Nick) si
todavía no están en la sesión. Cuando esta skill nombre otra, cárgala por su nombre antes de
pasarle el trabajo; si no carga, léela en `perplexity/skills/<nombre>/SKILL.md` del repo
`nicolascalle8-glitch/Skill_Repository`. El mapa completo está en el catálogo de `router-ing`.

---
name: auditor-handover
description: Audita si un chat (o un proyecto completo) ya está saturado y perdiendo calidad, da un reporte con puntaje y semáforo, y si el usuario quiere, arma un handover con decisiones, hitos, trazabilidad, tiempos y pendientes, más un CONTEXTO compacto para que un chat nuevo continúe el trabajo sin releer el chat viejo ni gastar tokens; lo archiva en GitHub por proyecto sin borrar versiones anteriores. Úsala siempre que el usuario diga que las respuestas están empeorando, que el chat está "tonto", lento, repetitivo u olvidadizo, que pida auditar el chat, revisar la capacidad o el límite del chat, hacer un handover, un traspaso, un resumen para pasar a otro chat, "empezar un chat nuevo sin perder nada", o actualizar el HANDOVER de un proyecto, aunque no nombre la skill. Para limpiar la memoria de Claude, los docs del proyecto o los chats viejos, usa depurador-recursos.
---

# Auditor de chat + Handover

Un chat largo se degrada: entre más texto acumula, más se diluyen las instrucciones del inicio, se mezclan temas, se olvidan decisiones y las respuestas se vuelven genéricas. Esta skill hace dos cosas:

1. **Auditoría**: mide qué tan degradado está el chat (o el proyecto) y da un veredicto honesto.
2. **Handover**: si el usuario quiere, deja dos archivos por proyecto en GitHub:
   - `CONTEXTO.md` — corto (~1.500 palabras), se reescribe cada vez. Es lo **único** que el chat nuevo lee para arrancar, así no tiene que releer el chat viejo ni el historial completo y no gasta tokens en eso.
   - `HANDOVER.md` — la trazabilidad completa: decisiones, hitos, tiempos, pendientes e historial con fechas que nunca se borra. Se consulta solo si hace falta saber cuándo o por qué cambió algo.

El usuario es Nick. Escríbele en español simple y directo. El handover también va en español simple: lo va a leer él y otro chat, no un comité.

## Paso 1 — Preguntar el alcance

Antes de auditar, pregunta (con AskUserQuestion si está disponible, si no en texto) qué se audita:

- **Este chat** (lo normal: la skill se corre al final del chat que está fallando).
- **El proyecto completo** (todos los chats del proyecto de claude.ai donde estás).

Pregunta también, en la misma tanda, **a qué proyecto pertenece** el trabajo, para saber en qué carpeta de GitHub archivar. Propón un nombre corto en minúsculas con guiones (ej. `arde-la-selva`, `fabrica-medias`) deducido del tema del chat, y deja que lo corrija.

## Paso 2 — Reunir la evidencia

No audites de memoria vaga. Primero relee lo que realmente pasó.

**Si es este chat:**
- Recorre la conversación completa de principio a fin. Si los turnos del inicio ya no están en tu contexto (o ves un resumen en vez de los mensajes originales), usa `read_conversation` con `conversation_id: "current"` para recuperarlos. Que los turnos del inicio ya no estén visibles es, en sí mismo, una señal fuerte de saturación: anótalo.
- Mientras lees, saca una lista cruda (para ti) de: decisiones, cambios de rumbo, hitos, archivos/links/entregables, pendientes, correcciones que el usuario tuvo que hacer, y respuestas tuyas que se contradicen.

**Si es el proyecto completo:**
- Usa `Projects` → `project_info` para ver docs y archivos del proyecto.
- Usa `recent_chats` y `conversation_search` para ubicar los chats del proyecto. Abre solo los que importan (1–2 páginas por chat con `read_conversation`), no todo.
- Revisa la memoria del proyecto si existe.

Cuenta lo que se pueda contar: número de turnos del usuario, número aproximado de temas distintos, número de correcciones, número de veces que se repitió una pregunta o una explicación.

## Paso 3 — Calificar

Lee `references/criterios-auditoria.md` y califica cada criterio de 0 a 10 (10 = perfecto, 0 = muy mal), con la evidencia concreta que justifica el número (cita el turno o el tema, no generalidades). Luego calcula el puntaje total y el semáforo con la regla de ese archivo.

Sé honesto, no complaciente: si el chat está bien, dilo; si está mal, dilo aunque el usuario esté de buen humor. Tampoco exageres para "vender" el handover. Y aclara una vez, sin drama, que no tienes un medidor exacto de tu capacidad interna: el puntaje se basa en señales observables, no en un contador de tokens.

## Paso 4 — Entregar el reporte

Formato del reporte en el chat:

```
## Auditoría — <proyecto> — <fecha>
Alcance: <este chat | proyecto completo>
Semáforo: 🟢 / 🟡 / 🔴  — Puntaje: <X>/100

| Criterio | Puntaje | Evidencia |
|---|---|---|
| ... | x/10 | ... |

**Qué está fallando:** 2–4 frases concretas.
**Recomendación:** seguir aquí / hacer handover y abrir chat nuevo / dividir en varios chats por tema.
```

Si recomiendas dividir, di en qué chats (ej. "uno para la web, otro para la cotización").

Si en la auditoría ves que el problema no es este chat sino lo que carga cada chat (memoria inflada, docs del proyecto pesados, muchos chats repetidos del mismo tema), dilo en una línea y recomienda `depurador-recursos` después del handover.

## Paso 5 — Preguntar si arma el handover

No lo armes solo. Pregunta: "¿Armo el handover?" con opciones claras (sí / no / sí, pero solo de un tema). Si el semáforo es verde, igual pregunta, pero dile que no es urgente.

## Paso 6 — Armar el handover y el contexto

Lee `references/plantilla-handover.md` y `references/plantilla-contexto.md`. Primero llena el HANDOVER (es el registro completo) y después destila de ahí el CONTEXTO (es lo que el chat nuevo realmente carga). La razón de separarlos: el HANDOVER crece con cada actualización y leerlo entero al arrancar volvería a llenar el chat nuevo; el CONTEXTO se mantiene del mismo tamaño siempre.

Para el CONTEXTO, pregúntate en cada línea: "¿el chat nuevo necesita esto para hacer la siguiente tarea sin preguntarle a Nick?". Si no, va solo en el HANDOVER. Pon los datos exactos (cifras, nombres, URLs, versiones), no resúmenes vagos, porque un resumen vago obliga al chat nuevo a volver a preguntar. Lo largo (código, textos aprobados extensos, tablas) va a `proyectos/<proyecto>/archivos/` y el CONTEXTO solo lo apunta con cuándo abrirlo.

Reglas para los dos:

- **Solo hechos del chat.** Si algo no se decidió, va en "Pendientes" o "Preguntas abiertas", no en "Decisiones".
- **Distingue quién dijo qué.** Una propuesta tuya que el usuario no aceptó explícitamente no es una decisión.
- **Fechas reales.** Usa las fechas/horas de los mensajes cuando se vean; si no, pon "aprox." Usa la hora de Bogotá (UTC-5).
- **Incluye "No volver a discutir"**: lo que ya se cerró, para que el chat nuevo no reabra temas resueltos.
- **Incluye el "Mensaje de arranque"**: un bloque corto que el usuario pega como primer mensaje del chat nuevo. Le dice al chat nuevo que lea **solo el CONTEXTO.md**, no el HANDOVER ni el chat viejo.
- Sin datos sensibles innecesarios: nada de contraseñas, tokens, números de cuenta o documentos de identidad, aunque aparezcan en el chat. Si son necesarios para el trabajo, escribe "(ver en <dónde>)".

## Paso 7 — Archivar en GitHub (sin borrar lo anterior)

Repositorio: `nicolascalle8-glitch/Skill_Repository` (privado). Por proyecto:

```
proyectos/<proyecto>/
  CONTEXTO.md    se reescribe completo cada vez (no crece)
  HANDOVER.md    se actualiza sin borrar (crece con el historial)
  archivos/      código, textos largos, tablas que el CONTEXTO apunta
```

1. Si el repo no está en la sesión, agrégalo con `add_repo` (acceso `push`) y clónalo como diga el resultado. Si GitHub no está disponible, salta al paso 8 de esta lista.
2. Si la carpeta `proyectos/<proyecto>/` no existe, **pregunta antes de crearla** (puede que el proyecto tenga otro nombre ya).
3. Si `HANDOVER.md` **no existe**: créalo con la plantilla completa y una primera entrada en el historial.
4. Si **ya existe**: léelo completo y actualízalo así, nunca borrando:
   - Reescribe la sección **Estado actual** (arriba) con lo vigente hoy.
   - Lo que ya no aplica no se borra: pásalo al historial marcado como `~~cerrado~~` o `reemplazado por: ...`.
   - Agrega una **entrada nueva al inicio del "Historial de actualizaciones"** con fecha y hora, puntaje de la auditoría y qué cambió desde la entrada anterior (decisiones nuevas, hitos cumplidos, pendientes cerrados y abiertos).
   - Actualiza la línea `Última actualización:` del encabezado.
5. Escribe `CONTEXTO.md` completo desde cero (si ya existía, se sobrescribe: su versión anterior queda en el historial de git y el HANDOVER guarda la trazabilidad). Revisa que no pase de ~1.500 palabras con `wc -w`; si pasa, comprime o mueve cosas a `archivos/`.
6. Guarda en `archivos/` lo largo que el chat nuevo pueda necesitar y que no viva ya en otro lado.
6b. **Bitácora del proyecto (GitHub y Google Drive).** Agrega una entrada HECHO arriba en `proyectos/<proyecto>/BITACORA.md` (créala con la plantilla de `skills/colaboracion-ias/references/plantilla-bitacora.md` si no existe): "Handover <fecha> — <semáforo> <puntaje>/100", qué cambió y la siguiente tarea. Copia la misma entrada al documento de Drive siguiendo `shared/BITACORA-DRIVE.md` (si el proyecto no tiene carpeta en Drive, créala ahí mismo y regístrala en `registry/DRIVE.yml`). Si Drive no responde, anota "Drive: pendiente de copiar" y sigue.
7. Haz commit y push a `main`:
   - `git fetch origin main` y rebase si hace falta antes de empujar.
   - Mensaje: `handover(<proyecto>): <fecha> — <semáforo> <puntaje>/100`
8. Si no se pudo empujar a GitHub, entrega los archivos con SendUserFile y di en una línea por qué no quedó en GitHub.

## Paso 8 — Cerrar

En el chat entrega:
1. El **Mensaje de arranque** en un bloque de código, listo para copiar. Debajo, dentro del mismo bloque, pega el CONTEXTO.md completo: así sirve aunque el chat nuevo no tenga acceso a GitHub.
2. Una línea con dónde quedó archivado (ruta en GitHub y link de la bitácora en Drive), cuántas palabras tiene el CONTEXTO, o por qué no se pudo archivar.

Nada más. No repitas el reporte ni el handover completo.

---
name: depurador-recursos
description: >-
  Depura la memoria de Claude, los docs del proyecto y los chats viejos de Nick sin perder
  datos técnicos ni investigaciones, y le deja reglas para gastar menos tokens y límites.
  Úsala cuando Nick pida limpiar, ordenar, depurar u optimizar la memoria, el proyecto o los
  chats, ahorrar tokens o recursos, o "dejar todo más liviano", aunque no nombre la skill.
  No sirve para un chat concreto que está fallando (eso es auditor-handover) ni para elegir
  IA o modelo (eso es selector-ia).
---

# Depurador de recursos

Cada chat arranca cargando memoria, instrucciones y docs del proyecto antes de que Nick
escriba nada, y los chats viejos ensucian la búsqueda de chats pasados. Esta skill limpia
cuatro cosas: **memoria de Claude**, **docs del proyecto**, **chats viejos** y **hábitos de
uso**, y deja un plan con el ahorro estimado.

Nick es estudiante de ingeniería mecánica (EIA) y hace research de inversiones (M&A,
empresas, sectores). En ese trabajo limpiar mal es caro: un supuesto o una unidad perdida
obliga a rehacer el cálculo. Por eso la regla central es **comprimir el texto, nunca los
datos**.

Manda `shared/CONTRATO-OPERATIVO.md` (etiquetas de evidencia, unidades, estados de archivo)
y `CONTRATO.md` (aprobaciones, historial que no se borra). Escríbele a Nick en español simple
y directo.

## Antes de empezar

1. Lee `CONTRATO.md` y `shared/CONTRATO-OPERATIVO.md` si tienes el repo
   `nicolascalle8-glitch/Skill_Repository`; si no está en la sesión, agrégalo con `add_repo`.
2. Lee `references/criterios-depuracion.md` (qué se conserva, qué se quita, cuándo algo venció).
3. Pregunta con AskUserQuestion (multiSelect) qué depurar: memoria, docs del proyecto, chats
   viejos, hábitos. Por defecto, todo. Si Nick no está, haz todo y entrega solo el plan.

## Reglas fijas

1. **Primero el plan, después los cambios.** Nada se borra, mueve ni reescribe sin un sí de
   Nick. Borrar un archivo de memoria o un doc pide un sí para ese archivo.
2. **Comprimir texto, no datos.** Los datos con etiqueta del contrato ([Dato], [Medido],
   [Norma], [Supuesto], [Calculado], [Por validar], [Decisión]) se conservan exactos, con su
   etiqueta, fuente y unidades tal como están. Al depurar no se convierten unidades ni se
   redondea.
3. **Lo largo va al repo, no a la memoria.** Memorias de cálculo e investigaciones van a
   `proyectos/<proyecto>/archivos/`; en memoria y en el proyecto queda una línea que apunta.
   Se guarda primero y se borra después, nunca al revés.
4. **El historial no se toca.** BITACORA, HANDOVER y commits nunca se depuran.
5. **Números honestos.** No hay contador exacto de tokens: estima con caracteres ÷ 4 y di
   "aprox." una vez.

## Cómo se hace

1. **Clasificar.** Pon cada archivo, doc o chat en un tipo (técnico, investigación,
   proyecto o negocio, personal) y lo técnico en su etapa (1 Enmarcar … 6 Continuar), con el
   estado del contrato operativo: borrador, vigente o histórico. Produce: inventario.
2. **Memoria de Claude.** `memory_list` con `include_preview: true` y lee en una sola llamada
   lo que vas a revisar. Busca duplicados, vencidos, inflados, descripciones largas (la línea
   `description` se carga en cada chat) y datos largos que deberían estar en el repo. Al
   editar: lee antes, usa `if_version`, copia sin cambios las líneas `[observed]`,
   `[inferred]`, fechadas de Claude Code y las que terminan en `(for=code)` o `[s:…]`.
   Dentro de un proyecto de claude.ai solo puedes escribir en `/projects/<id>/`: para los
   archivos de la cuenta deja el plan y pide correr la skill en un chat normal. Produce:
   filas del plan de memoria.
3. **Docs del proyecto.** `Projects` → `project_info`. Marca normas, catálogos y libros en
   PDF completos (proponer extraer solo las tablas usadas, con norma, edición y página),
   reportes largos (→ ficha de investigación), versiones viejas, instrucciones largas
   (muestra la versión corta completa) y lo ya cubierto por un `CONTEXTO.md`. Produce:
   filas del plan de docs.
4. **Chats viejos.** `recent_chats` (20 por llamada, paginando con `before`, máximo 5
   llamadas; si no alcanzó, dilo). Clasifica por título y búsquedas cortas, sin abrir chats
   completos: **borrar**, **guardar y luego borrar** (di qué: memoria de cálculo, ficha de
   investigación o handover con `auditor-handover`), **unir** o **dejar**. Produce: lista
   con el link de cada chat.
5. **Hábitos.** Máximo 6 reglas, sacadas de lo que encontraste (ideas en
   `references/criterios-depuracion.md`). Para modelo y esfuerzo, remite a `selector-ia`;
   si un procedimiento se repite en varios chats, a `router-ing` para volverlo skill.
6. **Plan y aprobación.** Entrega el reporte con el formato de `references/plantillas.md` y
   pregunta qué aplica (multiSelect: archivos al repo, memoria, docs, todo, nada). Aplica en
   este orden: archivos al repo → memoria → docs (todos los docs de una vez: cada cambio
   rompe el caché de todos los chats del proyecto).

## Salida

- En el chat: el reporte de `references/plantillas.md` y, al final, 2–3 líneas con qué
  cambió, qué quedó en el repo y el ahorro aprox. por chat.
- En el repo: fichas de investigación en `proyectos/<proyecto>/archivos/investigaciones/` y
  memorias de cálculo en `proyectos/<proyecto>/archivos/calculos/` (formatos en
  `references/plantillas.md`).
- Bitácora: entrada HECHO en `proyectos/<proyecto>/BITACORA.md` y su copia en Drive
  (`shared/BITACORA-DRIVE.md`): "Depuración <fecha> — ahorro aprox. X tokens por chat". Si
  la depuración no es de un proyecto, va en `proyectos/skills/`. Lo que necesita aprobación y
  Nick no ha respondido va como PROPUESTA.
- Lo que Nick tiene que hacer a mano: borrar chats, quitar archivos subidos al proyecto,
  correr la skill fuera del proyecto.

## Verificación

- Cada dato con etiqueta que había antes sigue existiendo en algún lado (memoria, doc o
  repo). Compara antes de borrar.
- Todo archivo nuevo del repo existe y se lee bien antes de quitar su origen.
- Memoria: cada escritura devolvió versión nueva; ningún archivo quedó con descripción vieja.
- El ahorro se calcula con el mismo método antes y después.

## Límites

- No borra chats ni archivos subidos: solo da la lista.
- No hace handovers (`auditor-handover`), no elige IA ni modelo (`selector-ia`), no elige
  skill de ingeniería (`router-ing`) y no rehace cálculos (cuando exista, `calculo-trazable`).
- No decide qué investigación sigue vigente para una decisión de inversión: marca la fecha y
  Nick decide si se vuelve a buscar.

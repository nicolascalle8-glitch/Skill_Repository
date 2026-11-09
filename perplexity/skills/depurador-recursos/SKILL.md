---
name: depurador-recursos
description: "Depura la memoria de Perplexity, los archivos de los Projects y las sesiones viejas de Nick sin perder datos técnicos ni investigaciones, y deja reglas para gastar menos tokens. Úsala si Nick pide limpiar, ordenar, depurar u optimizar la memoria, el Project o las sesiones, ahorrar recursos o \"dejar todo más liviano\". Una sesión que falla es auditor-handover; elegir IA o modelo, selector-ia."
metadata:
  perplexity:
    connectors:
      - id: github_mcp_direct
        reason: Guarda fichas de investigación y memorias de cálculo en Skill_Repository y escribe la entrada de bitácora.
      - id: google_drive
        reason: Copia la entrada de la bitácora al Doc de Drive del proyecto; sin Drive queda "pendiente de copiar".
---

# Depurador de recursos

Cada sesión arranca cargando memoria, instrucciones y archivos del Project antes de que Nick
escriba nada, y las sesiones viejas ensucian la búsqueda en sesiones pasadas. Esta skill limpia
cuatro cosas: **memoria de Perplexity**, **archivos del Project**, **sesiones viejas** y
**hábitos de uso**, y deja un plan con el ahorro estimado.

Nick es estudiante de ingeniería mecánica (EIA) y hace research de inversiones (M&A,
empresas, sectores). En ese trabajo limpiar mal es caro: un supuesto o una unidad perdida
obliga a rehacer el cálculo. Por eso la regla central es **comprimir el texto, nunca los
datos**.

Manda `shared/CONTRATO-OPERATIVO.md` (etiquetas de evidencia, unidades, estados de archivo)
y `CONTRATO.md` (aprobaciones, historial que no se borra). Escríbele a Nick en español simple
y directo.

## Antes de empezar

1. Clona `nicolascalle8-glitch/Skill_Repository` con `gh repo clone` (o `git pull` si ya
   está) y lee `CONTRATO.md` y `shared/CONTRATO-OPERATIVO.md`.
2. Lee `references/criterios-depuracion.md` (qué se conserva, qué se quita, cuándo algo venció).
3. Pregunta a Nick (puede elegir varias) qué depurar: memoria, archivos del Project, sesiones
   viejas, hábitos. Por defecto, todo. Si Nick no está (por ejemplo, en una automatización),
   haz todo y entrega solo el plan.

## Reglas fijas

1. **Primero el plan, después los cambios.** Nada se borra, mueve ni reescribe sin un sí de
   Nick. Borrar una memoria o un archivo pide un sí para esa memoria o ese archivo.
2. **Comprimir texto, no datos.** Los datos con etiqueta del contrato ([Dato], [Medido],
   [Norma], [Supuesto], [Calculado], [Por validar], [Decisión]) se conservan exactos, con su
   etiqueta, fuente y unidades tal como están. Al depurar no se convierten unidades ni se
   redondea.
3. **Lo largo va al repo, no a la memoria.** Memorias de cálculo e investigaciones van a
   `proyectos/<proyecto>/archivos/`; en memoria y en el Project queda una línea que apunta.
   Se guarda primero y se borra después, nunca al revés.
4. **El historial no se toca.** BITACORA, HANDOVER y commits nunca se depuran.
5. **Números honestos.** No hay contador exacto de tokens: estima con caracteres ÷ 4 y di
   "aprox." una vez.

## Cómo se hace

1. **Clasificar.** Pon cada memoria, archivo o sesión en un tipo (técnico, investigación,
   proyecto o negocio, personal) y lo técnico en su etapa (1 Enmarcar … 6 Continuar), con el
   estado del contrato operativo: borrador, vigente o histórico. Produce: inventario.
2. **Memoria de Perplexity.** Recorre las memorias con `memory_list` / `memory_search` y lee
   con `memory_read` solo las que vas a revisar. Busca duplicados, vencidos, inflados, vagos y
   datos largos que deberían estar en el repo. Los cambios aprobados se aplican con
   `memory_update`; lee la memoria justo antes de cambiarla. Produce: filas del plan de memoria.
3. **Archivos del Project.** Carga la skill `perplexity-platform` para ver los archivos e
   instrucciones del Project. Marca normas, catálogos y libros en PDF completos (proponer
   extraer solo las tablas usadas, con norma, edición y página), reportes largos (→ ficha de
   investigación), versiones viejas, instrucciones largas (muestra la versión corta completa)
   y lo ya cubierto por un `CONTEXTO.md`. Produce: filas del plan de archivos.
4. **Sesiones viejas.** Lista las sesiones pasadas (con `perplexity-platform` o con las
   herramientas de memoria; máximo ~100 sesiones; si no alcanzó, dilo). Clasifica por título
   y búsquedas cortas, sin abrir sesiones completas: **borrar**, **guardar y luego borrar**
   (di qué: memoria de cálculo, ficha de investigación o handover con `auditor-handover`),
   **unir** o **dejar**. Solo se listan: Nick las borra a mano. Produce: lista con el link o
   nombre de cada sesión.
5. **Hábitos.** Máximo 6 reglas, sacadas de lo que encontraste (ideas en
   `references/criterios-depuracion.md`). Para modelo y esfuerzo, remite a `selector-ia`;
   si un procedimiento se repite en varias sesiones, a `router-ing` para volverlo skill.
6. **Plan y aprobación.** Entrega el reporte con el formato de `references/plantillas.md` y
   pregunta a Nick qué aplica (puede elegir varias: archivos al repo, memoria, archivos del
   Project, todo, nada). Aplica en este orden: archivos al repo → memoria → archivos del
   Project (todos de una vez).

## Salida

- En la sesión: el reporte de `references/plantillas.md` y, al final, 2–3 líneas con qué
  cambió, qué quedó en el repo y el ahorro aprox. por sesión.
- En el repo: fichas de investigación en `proyectos/<proyecto>/archivos/investigaciones/` y
  memorias de cálculo en `proyectos/<proyecto>/archivos/calculos/` (formatos en
  `references/plantillas.md`).
- Bitácora: entrada HECHO en `proyectos/<proyecto>/BITACORA.md`, firmada
  `Perplexity Computer (<modelo>)`, y su copia en Drive (`shared/BITACORA-DRIVE.md`, con los
  comandos de `references/bitacora-drive-gws.md`): "Depuración <fecha> — ahorro aprox. X
  tokens por sesión". Si la depuración no es de un proyecto, va en `proyectos/skills/`. En
  `horno-vertical` va solo en GitHub, con el formato corto de su bitácora (sin Drive). Lo que
  necesita aprobación y Nick no ha respondido va como PROPUESTA. Commit
  `perplexity(<proyecto>): depuración <fecha>`; si falta el autor de git, configúralo desde
  `gh api user`; `git fetch` + rebase antes de empujar, nunca `push --force`.
- Lo que Nick tiene que hacer a mano: borrar sesiones, quitar archivos subidos al Project.

## Verificación

- Cada dato con etiqueta que había antes sigue existiendo en algún lado (memoria, archivo o
  repo). Compara antes de borrar.
- Todo archivo nuevo del repo existe y se lee bien antes de quitar su origen.
- Memoria: relee cada memoria cambiada y confirma que quedó como se aprobó.
- El ahorro se calcula con el mismo método antes y después.

## Límites

- No borra sesiones ni archivos subidos: solo da la lista.
- No hace handovers (`auditor-handover`), no elige IA ni modelo (`selector-ia`), no elige
  skill de ingeniería (`router-ing`) y no rehace cálculos (cuando exista, `calculo-trazable`).
- No decide qué investigación sigue vigente para una decisión de inversión: marca la fecha y
  Nick decide si se vuelve a buscar.

## Acceso a las otras skills de Nick

Todas las skills de Nick están guardadas en Perplexity. Carga de fondo `contexto-nick` (quién es Nick) y `cerebro-nick` (cómo decide Nick) si
todavía no están en la sesión. Cuando esta skill nombre otra, cárgala por su nombre antes de
pasarle el trabajo; si no carga, léela en `perplexity/skills/<nombre>/SKILL.md` del repo
`nicolascalle8-glitch/Skill_Repository`. El mapa completo está en el catálogo de `router-ing`.

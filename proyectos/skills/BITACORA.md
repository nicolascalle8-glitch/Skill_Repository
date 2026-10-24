# BITÁCORA — Skills (Skill_Repository)

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra.
Copia en Google Drive: Proyectos IA / skills / Bitácora — skills (https://docs.google.com/document/d/18QtRuv0MvYGrumv7YzqNIKsTefi9423Fgm904UdUWeI/edit)

## En curso
- (nada)

## Propuestas sin respuesta
- 2026-10-24 17:41 — Claude — Cambiar la regla "todo en SI" del contrato operativo a "SI por defecto, salvo que el libro o el enunciado use otro sistema".
- 2026-10-24 18:04 — Claude — Agregar depurador-recursos a la sección 8 del contrato operativo.
- 2026-10-24 18:22 — Claude — (monitor) Subir panel-asesores y presentaciones-universidad al repo y registrarlas.
- 2026-10-24 18:22 — Claude — (monitor) Crear voz-nick (activar la pendiente).
- 2026-10-24 18:22 — Claude — (monitor) Crear calculo-trazable (activar la pendiente).
- 2026-10-24 18:22 — Claude — (monitor) Decidir system-oriented-design: base de marco-problema-ing, aparte o descartar.

---

## Entradas

### 2026-10-24 18:40 — Claude Opus 5.5 — HECHO
**Qué:** Depuración de memoria, chats y hábitos (docs del proyecto no revisados: sin acceso desde el chat). Ahorro aprox. 150 tokens por chat.
**Archivos:** proyectos/skills/archivos/investigaciones/fotosintesis-cuantica-2026-05.md (nuevo). Memoria: presentacion-engranajes-helicoidales (corregido: ejercicio Mott, no el video), brake-lever (recibe las 2 líneas de Ashby), recent-work (acortado), coursework (recibe Térmicas), interests (acortado), descripción de trading-memecoins (acortada), computer-setup (sin el dato de financiación).
**Fuentes:** chat de engranajes helicoidales; recent_chats (40 chats, 2 páginas); chat de fotosíntesis para la ficha.
**Verificado:** cada escritura de memoria devolvió versión nueva; las 2 líneas de Ashby se copiaron exactas a brake-lever antes de quitarlas de recent-work; las de Térmicas se copiaron a coursework (el archivo viejo sigue); la ficha existe en el repo.
**Para Nick:** borrar a mano los chats de la lista del reporte; decidir si se borra /areas/thermal-systems-design.md (ya está copiado en coursework); revisar los docs del proyecto de claude.ai.
**Para la siguiente IA:** las cifras de la ficha de fotosíntesis están [Por validar] contra el artículo.

### 2026-10-24 18:22 — Claude Opus 5.5 — PROPUESTA
**Qué:** Salen de la revisión de skills de hoy (proyectos/skills/monitor/2026-10-24.md). Aprobar cada una por separado: (1) subir panel-asesores y presentaciones-universidad al repo y registrarlas en CAPACIDADES y en el catálogo (hoy solo están instaladas en Claude); (2) crear voz-nick con el perfil de escritura que salió en el chat de presentaciones, y que presentaciones-universidad y panel-asesores la llamen en vez de repetir reglas; (3) crear calculo-trazable con el caso Mott 10-2; (4) system-oriented-design: usarla como base de marco-problema-ing, guardarla aparte o descartarla.
**Archivos:** ninguno todavía.
**Fuentes:** proyectos/skills/monitor/2026-10-24.md (evidencia de cada una).
**Verificado:** n/a hasta ejecutar.
**Para Nick:** aprobar o rechazar 1 a 4.
**Para la siguiente IA:** no crear voz-nick ni calculo-trazable hasta que Nick apruebe.

### 2026-10-24 18:22 — Claude Opus 5.5 — HECHO
**Qué:** Revisión de skills 2026-10-24 (primera, 🟡). Sobra: ninguna. Actualizar: 2 (panel-asesores y presentaciones-universidad fuera del repo). Mejorar: 2 (panel-asesores, router-ing). Crear: 2 (voz-nick, calculo-trazable) + decidir system-oriented-design.
**Archivos:** proyectos/skills/monitor/2026-10-24.md
**Fuentes:** inventario.py; 7 chats del proyecto Skills; bitácoras de skills y engranajes.
**Verificado:** inventario.py corrido sobre el repo y las skills instaladas.
**Para Nick:** ver propuestas arriba.
**Para la siguiente IA:** la próxima revisión arranca desde esta fecha.

### 2026-10-24 18:22 — Claude Opus 5.5 — HECHO
**Qué:** Se crea la skill monitor-skills: revisa todas las skills y dice cuál sobra, cuál actualizar o mejorar y qué crear según el uso real (chats y bitácoras), con evidencia; solo propone, Nick aprueba. Corre también como revisión semanal. router-ing ya no propone skills nuevas: lo remite al monitor. Se agrega el estado `retirada` a CAPACIDADES.
**Archivos:** skills/monitor-skills/ (SKILL.md, references/criterios.md, references/plantilla-reporte.md, scripts/inventario.py), skills/router-ing/SKILL.md, skills/router-ing/references/catalogo.md, registry/CAPACIDADES.yml, README.md
**Fuentes:** pedido de Nick en el chat del 2026-10-24 (revisión semanal; monitor se queda con crear/mejorar/sobra; propone y él aprueba).
**Verificado:** monitor-skills y router-ing pasan quick_validate; CAPACIDADES.yml carga como YAML; inventario.py corrido sin falsos positivos.
**Para Nick:** instalar monitor-skills.skill y reinstalar router-ing.skill.
**Para la siguiente IA:** para crear o retirar skills, pasar por monitor-skills.

### 2026-10-24 18:04 — Claude Opus 5.5 — HECHO
**Qué:** Se crea la skill depurador-recursos: limpia memoria de Claude, docs del proyecto y chats viejos para gastar menos tokens, sin perder datos técnicos (etiquetas del contrato operativo) ni investigaciones (fichas con fecha y vigencia). Se registra en CAPACIDADES y en el catálogo del router, y las otras 4 skills la nombran. auditor-handover ya no se dispara con "auditar la memoria" para no chocar con la nueva.
**Archivos:** skills/depurador-recursos/, registry/CAPACIDADES.yml, skills/router-ing/SKILL.md, skills/router-ing/references/catalogo.md, skills/auditor-handover/SKILL.md, skills/selector-ia/SKILL.md, skills/colaboracion-ias/SKILL.md, README.md
**Fuentes:** pedido de Nick en el chat del 2026-10-24 ("skill para depurar los chats y reservar memoria").
**Verificado:** Las 5 skills pasan quick_validate; CAPACIDADES.yml carga como YAML; las 5 se empaquetaron como .skill. La skill no se ha probado con una depuración real (estado en-prueba).
**Para Nick:** Instalar depurador-recursos.skill y reinstalar auditor-handover, router-ing, selector-ia y colaboracion-ias (cambió su texto). Probarla con "depura mi memoria" en un chat normal (fuera de proyecto) para que pueda editar la memoria de la cuenta.
**Para la siguiente IA:** Fichas de investigación en proyectos/<proyecto>/archivos/investigaciones/ y memorias de cálculo en archivos/calculos/. Leerlas antes de volver a investigar o calcular.

### 2026-10-24 18:04 — Claude Opus 5.5 — PROPUESTA
**Qué:** Agregar en shared/CONTRATO-OPERATIVO.md, sección 8, la línea: "Para limpiar memoria, docs del proyecto y chats viejos sin perder datos, se usa depurador-recursos."
**Archivos:** ninguno todavía.
**Fuentes:** creación de depurador-recursos (entrada anterior).
**Verificado:** n/a.
**Para Nick:** aprobar o rechazar.
**Para la siguiente IA:** no cambiar el contrato operativo hasta que Nick decida.

### 2026-10-24 17:55 — Claude Opus 5.5 — HECHO
**Qué:** Se crea la skill selector-ia (qué IA, modelo y nivel usar) con catálogo de modelos revisado el 2026-10-24. Se monta la copia de las bitácoras en Google Drive: carpeta Proyectos IA con una subcarpeta y un Doc de bitácora por proyecto (engranajes-helicoidales y skills). colaboracion-ias, auditor-handover y selector-ia ahora escriben en GitHub y en Drive.
**Archivos:** skills/selector-ia/, shared/BITACORA-DRIVE.md, shared/scripts/entrada_drive.py, registry/DRIVE.yml, registry/CAPACIDADES.yml, skills/colaboracion-ias/SKILL.md, skills/auditor-handover/SKILL.md, CONTRATO.md (v0.1.1), GEMINI.md, README.md
**Fuentes:** Docs de Anthropic, gemini.google, cursor.com y docs.github.com (links en skills/selector-ia/references/catalogo.md).
**Verificado:** Las 4 skills pasan quick_validate; los YAML cargan; esta entrada se agregó a Drive con entrada_drive.py y se revisó leyendo el Doc.
**Para Nick:** Confirmar qué plan de Claude tienes, si es Cursor o Copilot (y qué plan), y si Gemini es Pro o Ultra. Decir qué otros proyectos quieres con carpeta en Drive.
**Para la siguiente IA:** Los ids de Drive están en registry/DRIVE.yml. Toda entrada va idéntica a GitHub y a Drive (shared/BITACORA-DRIVE.md).

### 2026-10-24 17:41 — Claude Opus 5.5 — HECHO
**Qué:** Se sube el esqueleto de skills de ingeniería basado en twolucky-capabilities (repo de Luisa): contrato operativo, plantilla de skill, router-ing y registro de capacidades. Se corrige el encabezado de colaboracion-ias, que no pasaba la validación.
**Archivos:** shared/CONTRATO-OPERATIVO.md, shared/PLANTILLA-SKILL.md, skills/router-ing/, registry/CAPACIDADES.yml, CONTRATO.md, README.md, skills/colaboracion-ias/SKILL.md
**Fuentes:** chat "Repositorio de skills de mi mentora" (2026-10-24).
**Verificado:** CAPACIDADES.yml carga como YAML; router-ing y colaboracion-ias pasan quick_validate.
**Para Nick:** Instalar router-ing.skill y la versión corregida de colaboracion-ias.skill. Decidir la regla de unidades (ver propuesta).
**Para la siguiente IA:** Las skills nuevas se escriben con shared/PLANTILLA-SKILL.md y se registran en CAPACIDADES.yml y en el catálogo del router en el mismo commit.

### 2026-10-24 17:41 — Claude Opus 5.5 — PROPUESTA
**Qué:** Cambiar en shared/CONTRATO-OPERATIVO.md la regla "Se trabaja en SI" por "SI por defecto, salvo que el libro o el enunciado use otro sistema". El proyecto de engranajes se trabajó en unidades inglesas porque Mott viene así.
**Archivos:** ninguno todavía.
**Fuentes:** CONTEXTO de engranajes-helicoidales ("Presentación en Claude Slides, unidades inglesas").
**Verificado:** n/a.
**Para Nick:** aprobar o rechazar.
**Para la siguiente IA:** no cambiar la regla hasta que Nick decida.

### 2026-10-24 17:29 — Claude Opus 5.5 — HECHO
**Qué:** Se crea el contrato de trabajo para todas las IAs (v0.1, borrador), la skill colaboracion-ias y los archivos de entrada para Cursor, Copilot, Gemini y Claude.
**Archivos:** CONTRATO.md, AGENTS.md, GEMINI.md, CLAUDE.md, .github/copilot-instructions.md, .cursor/rules/contrato.mdc, skills/colaboracion-ias/
**Fuentes:** pedido de Nick en el chat del 2026-10-24.
**Verificado:** commit 91ffcec en main.
**Para Nick:** completar las líneas [COMPLETAR NICK] del contrato.
**Para la siguiente IA:** leer CONTRATO.md antes de cualquier cosa.

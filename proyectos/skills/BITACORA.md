# BITÁCORA — Skills (Skill_Repository)

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra.
Copia en Google Drive: Proyectos IA / skills / Bitácora — skills (https://docs.google.com/document/d/18QtRuv0MvYGrumv7YzqNIKsTefi9423Fgm904UdUWeI/edit)

## En curso
- (nada)

## Propuestas sin respuesta
- 2026-10-24 17:41 — Claude — Cambiar la regla "todo en SI" del contrato operativo a "SI por defecto, salvo que el libro o el enunciado use otro sistema".
- 2026-10-24 18:04 — Claude — Agregar depurador-recursos a la sección 8 del contrato operativo.
- 2026-10-24 18:22 — Claude — (monitor) Crear calculo-trazable (activar la pendiente).
- 2026-10-24 18:22 — Claude — (monitor) Decidir system-oriented-design: base de marco-problema-ing, aparte o descartar.
- 2026-10-24 20:50 — Claude — Integración del sistema de Gemini: 3 reglas al contrato, ordenar D:\Personal\Claude por proyecto, guion cronometrado en presentaciones-universidad, confirmar perfil.

---

## Entradas

### 2026-10-24 20:48 — Claude Opus 5.5 — HECHO
**Qué:** Se ordenó D:\Personal\Claude por proyecto (aprobado por Nick): proyectos\banco-pruebas-fz15\ y proyectos\taller-final-mecanismos\ con fuentes/trabajo/entregables/anterior, y _entrada\ con el archivo de Gemini. Solo se movió y copió, nada se borró. En taller-final, entregables\ y anterior\ son copias (los originales siguen en trabajo\Soluciones\).
**Archivos:** proyectos/README.md (rutas nuevas). En el computador: D:\Personal\Claude\proyectos\, D:\Personal\Claude\_entrada\
**Fuentes:** —
**Verificado:** listado de la carpeta después de mover: no quedó nada en Yamaha_banco_pruebas\ (la carpeta vacía sigue porque no hay permiso de borrar).
**Para Nick:** borrar a mano la carpeta vacía Yamaha_banco_pruebas\. extract_imgs.m y build_report.py tienen la ruta vieja D:/Personal/Claude escrita; si los vuelves a correr, hay que cambiarla.
**Para la siguiente IA:** los archivos de trabajo de cada proyecto están en D:\Personal\Claude\proyectos\<proyecto>\.

### 2026-10-24 20:50 — Claude Opus 5.5 — PROPUESTA
**Qué:** Lo que sale de la revisión del sistema de Gemini y necesita a Nick: (1) agregar al CONTRATO, sección 4: "no leer libros ni PDFs largos completos sin permiso", "lo viejo se mueve a anterior/, no se borra" y "lo que está en Excel se verifica con un script aparte"; (2) ordenar D:\Personal\Claude con la estructura nueva (proyectos\banco-pruebas-fz15\ y proyectos\taller-final-mecanismos\ con fuentes/trabajo/entregables/anterior, y _entrada\ para el archivo de Gemini); (3) agregar a presentaciones-universidad el guion cronometrado (palabras y tiempo por slide con acumulado, 2 primeras frases con la idea, bloques [RECORTABLE]); (4) confirmar si el perfil que puso Gemini es cierto ("Ingeniería Mecánica y Economía", Mede3DLab, consultor SEO/GEO).
**Archivos:** ninguno todavía.
**Fuentes:** proyectos/skills/archivos/gemini/revision-2026-10-24.md
**Verificado:** n/a hasta ejecutar.
**Para Nick:** aprobar o rechazar 1 a 4.
**Para la siguiente IA:** no mover nada en el computador de Nick ni tocar el contrato hasta que Nick apruebe.
✅ Aprobado por Nick — 2026-10-24 20:48 — punto (2): ordenar D:\Personal\Claude. (1), (3) y (4) siguen abiertos.

### 2026-10-24 20:50 — Claude Opus 5.5 — HECHO
**Qué:** Nueva estructura de proyectos: shared/PLANTILLA-PROYECTO.md (repo + computador con fuentes/trabajo/entregables/anterior, arranque con máx. 5 preguntas, criterio de cierre, estados) e índice proyectos/README.md con los 4 proyectos (skills, engranajes-helicoidales, y por confirmar banco-pruebas-fz15 y taller-final-mecanismos). La plantilla del CONTEXTO de auditor-handover tiene ahora "Criterio de cierre". Se dejaron listas para instalar (tarjetas en el chat): calculo-trazable (nueva, punto 3 de la propuesta del monitor de 18:22), y cambios a colaboracion-ias y auditor-handover para que usen la plantilla.
**Archivos:** shared/PLANTILLA-PROYECTO.md, proyectos/README.md, skills/auditor-handover/references/plantilla-contexto.md, README.md, proyectos/skills/archivos/gemini/
**Fuentes:** archivo de Gemini (proyectos/skills/archivos/gemini/sistema-skills-agentes-2026-10-24.md); pedido de Nick en el chat 2026-10-24 20:32.
**Verificado:** rutas de la plantilla revisadas contra CONTRATO.md §7 y las skills que las usan (colaboracion-ias, auditor-handover, depurador-recursos): no se contradicen.
**Para Nick:** guardar las 3 tarjetas de skills si estás de acuerdo (monitor-skills las sube al repo); calculo-trazable queda en-prueba con el caso Mott 10-2.
**Para la siguiente IA:** la estructura de un proyecto ahora se lee en shared/PLANTILLA-PROYECTO.md.

### 2026-10-24 20:45 — Claude Opus 5.5 — REVISIÓN
**Qué:** Revisión del sistema de Gemini. Ya lo teníamos casi todo (context-handover = auditor-handover; arquitecto-proyecto ≈ colaboracion-ias flujo E). Sirve: caso base primero, fórmulas del Excel, break-even/tornado (→ calculo-trazable); revisión de consistencia entre archivos; carpeta anterior/ y criterio de cierre (→ estructura de proyectos); guion cronometrado (→ presentaciones-universidad). Fuera de este proyecto: digital-growth-geo y propuestas comerciales. No se copió el perfil de Gemini porque tiene datos sin confirmar.
**Archivos:** proyectos/skills/archivos/gemini/revision-2026-10-24.md
**Fuentes:** el archivo de Gemini, comparado con las skills del repo.
**Verificado:** leído completo; cada pieza comparada con la skill que la cubre.
**Para Nick:** confirmar el perfil (punto 4 de la propuesta).
**Para la siguiente IA:** la tabla de qué se integra y qué no está en la revisión.

### 2026-10-24 20:30 — Gemini — HECHO (subido por Claude desde el chat de Nick)
**Qué:** Propuesta de "Sistema genérico de skills y agentes": CLAUDE.md global, 4 skills (context-handover, quant-verification, editorial-deliverables, digital-growth-geo) y 2 subagentes (auditor-consistencia, arquitecto-proyecto). Nick lo bajó a D:\Personal\Claude\claude_sistema_skills_agentes.md.
**Archivos:** proyectos/skills/archivos/gemini/sistema-skills-agentes-2026-10-24.md (copia exacta)
**Fuentes:** no indica.
**Verificado:** no indica.
**Para Nick:** —
**Para la siguiente IA:** —

### 2026-10-24 18:45 — Claude Opus 5.5 — HECHO
**Qué:** Se crea la skill voz-nick con el perfil de escritura sacado de textos reales de Nick en Drive (chat de presentaciones del 2026-10-24): rasgos suyos, lo que no es Nick, calibración por tipo de texto y una sección de correcciones que crece cuando él corrige. Incluye revisar_voz.py, que marca muletillas, lenguaje inflado, guiones largos, cierres tipo eslogan, tríos de adjetivos y frases muy largas. presentaciones-universidad y panel-asesores ahora la llaman en vez de repetir reglas de estilo.
**Archivos:** skills/voz-nick/ (SKILL.md, references/perfil.md, scripts/revisar_voz.py), skills/presentaciones-universidad/SKILL.md, skills/panel-asesores/SKILL.md, registry/CAPACIDADES.yml, skills/router-ing/references/catalogo.md, README.md
**Fuentes:** perfil de la tarjeta de presentaciones-universidad (chat "Presentaciones universitarias bien hechas", 2026-10-24).
**Verificado:** prueba con un texto de IA sobre las conclusiones de engranajes: revisar_voz.py marcó 20 hallazgos en el original y 0 en la versión final; todos los números, materiales y conclusiones quedaron iguales (comparados con script). Un texto en su estilo no dio falsos positivos. voz-nick pasa quick_validate.
**Para Nick:** instalar voz-nick.skill y reinstalar presentaciones-universidad, panel-asesores y router-ing. Confirmar si las plantillas de WhatsApp del consultorio y los apuntes de marketing los escribiste tú, y si en notas prefieres frases medianas con punto y coma o cortas.
**Para la siguiente IA:** todo texto que Nick presente como suyo pasa por voz-nick. El perfil es la fuente única de su estilo.

### 2026-10-24 18:30 — Claude Opus 5.5 — HECHO
**Qué:** Sincronización 2026-10-24. Subidas: panel-asesores y presentaciones-universidad (nuevas; registradas en CAPACIDADES como en-prueba, etapa por-definir, y en el catálogo). Reinstalar: monitor-skills y router-ing (el repo va adelante). Bloqueadas o en conflicto: ninguna.
**Archivos:** skills/panel-asesores/, skills/presentaciones-universidad/, registry/CAPACIDADES.yml, skills/router-ing/references/catalogo.md
**Fuentes:** skills instaladas en Claude (manifest.json, origen plugin).
**Verificado:** sincronizar.py sin pendientes después de aplicar; CAPACIDADES.yml carga como YAML.
**Para Nick:** reinstalar monitor-skills.skill y router-ing.skill.
**Para la siguiente IA:** revisar etapa y caso de prueba de panel-asesores y presentaciones-universidad en CAPACIDADES.

### 2026-10-24 18:30 — Claude Opus 5.5 — HECHO
**Qué:** monitor-skills ahora sincroniza solo con GitHub: detecta las skills que Nick creó o cambió en Claude y las sube al repo sin pedir permiso (decisión de Nick del 2026-10-24 18:27). Compara con el historial de git para no pisar el repo cuando va más nuevo (en ese caso pide reinstalar), no sube archivos con posibles claves y nunca borra nada del repo. Corre a diario como tarea programada y al empezar cada revisión.
**Archivos:** skills/monitor-skills/SKILL.md, skills/monitor-skills/scripts/sincronizar.py, skills/monitor-skills/scripts/inventario.py
**Fuentes:** pedido de Nick en el chat del 2026-10-24 18:27.
**Verificado:** sincronizar.py probado con casos simulados (skill nueva, cambiada en Claude, repo más nuevo, posible clave): los cuatro dieron el resultado esperado. monitor-skills pasa quick_validate.
**Para Nick:** reinstalar monitor-skills.skill.
**Para la siguiente IA:** subir skills al repo es automático; crear, mejorar o retirar sigue necesitando aprobación de Nick.

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
✅ Aprobado por Nick — 2026-10-24 18:27 — solo el punto (1): pidió que el monitor suba todo al repo automáticamente. (2), (3) y (4) siguen abiertos.
✅ Aprobado por Nick — 2026-10-24 18:36 — punto (2): crear voz-nick.

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

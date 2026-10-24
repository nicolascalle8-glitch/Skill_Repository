# BITÁCORA — Presentación Engranajes Helicoidales

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra.

## En curso
- (nada)

## Propuestas sin respuesta
- 2026-10-24 17:45 — Claude — Mover archivos viejos de Helical_Gears_Deliverables a `anterior/`
- 2026-10-24 17:45 — Claude — Alinear el artículo de Google Docs con Mott 10-2 (Casos A y B)

---

## Entradas

### 2026-10-24 17:45 — Claude Opus 5.5 — PROPUESTA
**Qué:** (1) Mover a `Helical_Gears_Deliverables/anterior/` los archivos que contradicen el ejercicio final: Guia_Tablero_Engranajes_Helicoidales.pdf, ejercicio_helicoidal.py, Helical Gears-Design-Fixed.xlsx, Helical_Gears_Mott_Presentation_EN.html, Helical_Gears_Presentation_Outline_and_Script.md, Helical_Gears_Technical_Article_EN.md, "Helical Gears — Mechanical Design.pdf" (exportación del 22 oct). (2) Alinear el artículo de Google Docs (doc 1tQkRlo_…) con el ejercicio Mott 10-2, Casos A y B, con los números del CONTEXTO.
**Archivos:** ninguno todavía (necesita aprobación: mover archivos y cambio grande al artículo, contrato §5).
**Fuentes:** CONTEXTO.md; auditoría del 2026-10-24.
**Verificado:** no aplica hasta ejecutar.
**Para Nick:** aprobar o rechazar (1) y (2) por separado. Para (2), decir si el artículo deja también el Problema modelo 10-1 y el ejemplo de 11 hp.
**Para la siguiente IA:** no mover ni editar estos archivos hasta que Nick apruebe.

### 2026-10-24 17:45 — Claude Opus 5.5 — REVISIÓN
**Qué:** Revisión del trabajo de Gemini hecho antes de abrir la bitácora (Guía Maestra, Helical Gears-Design-Fixed.xlsx). Sirve: diccionario de símbolos, figuras de Mott y ejemplos 8-5, 10-1 y Example #1 (números rehechos, cuadran). Está mal: (a) dice que el Excel del profesor falla porque G40 perdió la referencia a G27; en el archivo original G40 = G30*G24*G17/(G16*G18) y G17 está vacía, por eso sc da 0. Las celdas que cita (G19, G63, F79) no existen así en el original. (b) Example #2: pone Kv = 1.08 "para Av 11"; 1.08 sale con Qv 11 (escala 4ª ed.); con Av 11 (6e) Kv = 1.42.
**Archivos:** ninguno (lo bueno ya se usó en Kit_Sustentacion_Engranajes_Helicoidales.pdf, en la carpeta local de Nick).
**Fuentes:** Helical Gears-Design.xlsx (original del curso); Mott 4ª ed. §9; ecuaciones de Kv del CONTEXTO.
**Verificado:** fórmulas leídas con openpyxl; Kv y ejemplos recalculados en Python.
**Para Nick:** nada.
**Para la siguiente IA:** no usar la explicación de Gemini del error del Excel ni su Kv del Example #2.

### 2026-10-24 17:29 — Claude Opus 5.5 — HECHO
**Qué:** Se abre la bitácora del proyecto. El trabajo anterior (presentación, Excel, kit, guía de Gemini) está registrado en HANDOVER.md y CONTEXTO.md.
**Archivos:** proyectos/engranajes-helicoidales/BITACORA.md
**Fuentes:** CONTEXTO.md del 2026-10-24 14:45.
**Verificado:** n/a.
**Para Nick:** nada.
**Para la siguiente IA:** Ojo: la Guía Maestra de Gemini explica mal el error del Excel del profesor (ver "Errores que no repetir" en el CONTEXTO).

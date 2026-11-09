# BITÁCORA — Horno vertical (pirólisis de café, práctica GIEM UdeA/EIA)

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra. Copia idéntica en Google Drive: Proyectos IA / horno-vertical / Bitácora — horno-vertical.

## En curso
- Claude Opus 5.5 — diseño del motor nuevo (subproyecto A, spec) — desde 2026-11-08 19:33
- Gemini — investigación de datos del café y del reactor — desde 2026-11-08 19:36
- Perplexity — datos del controlador MC-5438 — desde 2026-11-08 19:36

## Propuestas sin respuesta
- (ninguna)

---

## Entradas

### 2026-11-08 19:36 — Claude Opus 5.5 — HECHO
**Qué:** Reglas del proyecto para ahorrar tokens (todas las IAs).
**Archivos:** proyectos/horno-vertical/CONTEXTO.md (sección "Cómo se trabaja").
**Fuentes:** depurador-recursos y selector-ia, revisión del 2026-11-08.
**Verificado:** n/a.
**Para Nick:** (1) Un chat por subproyecto: A motor, B calibración, C app; la Línea 2 (IA local) siempre aparte. (2) Cuando un chat se alargue (respuestas lentas, olvida cosas), cerrarlo con auditor-handover y abrir otro que arranque leyendo CONTEXTO.md. (3) Al abrir un chat, decir solo "trabajemos en horno-vertical, subproyecto X": la IA lee CONTEXTO y las últimas 5 entradas, no todo. (4) CSV, resultados y logs no se pegan en el chat: se dejan en la carpeta y la IA los lee. (5) Corridas pesadas en la Terminal de macOS; Claude solo prepara scripts. (6) Investigar → Gemini/Perplexity; código repetitivo de la app → Cursor/Copilot; Claude para física, numérica, revisión y verificación.
**Para la siguiente IA:** Respetar el reparto del punto 6. El estado vive en CONTEXTO.md, no en el doc del Project de claude.ai (cada cambio al doc rompe el caché de todos los chats).

### 2026-11-08 19:36 — Claude Opus 5.5 — PREGUNTA
**Qué:** Tarea para CURSOR o COPILOT (modelo Auto). EN ESPERA: no empezar todavía.
**Archivos:** Repo PyrolysisReactorCoffee, rama del motor nuevo (la crea Claude).
**Fuentes:** Spec del motor y de la app (los escribe Claude; Nick los aprueba).
**Verificado:** n/a.
**Para Nick:** Cuando Claude anuncie en esta bitácora que la interfaz del motor quedó fija, abrir el repo en Cursor/Copilot y pedirle: "Haz la tarea de Cursor de la bitácora horno-vertical".
**Para la siguiente IA:** CURSOR/COPILOT: construir las pantallas de la app Streamlit (entradas de parámetros, gráficas, carga del CSV del termopar) usando SOLO la interfaz pública del paquete motor/. No tocar la física, la numérica ni parametros.toml. Cada pantalla con su prueba. Al terminar, entrada HECHO en esta bitácora.

### 2026-11-08 19:36 — Claude Opus 5.5 — PREGUNTA
**Qué:** Tarea para PERPLEXITY (gratis, Pro Search si hay). Datos del controlador Max-Therma / MaxThermo MC-5438 del horno.
**Archivos:** ninguno (Perplexity no tiene acceso; Nick pega la respuesta en el chat de Claude).
**Fuentes:** Manual o ficha del fabricante primero; foros solo marcados como [Por validar].
**Verificado:** n/a (lo revisa Claude).
**Para Nick:** Pegar en Perplexity el bloque que dejó Claude en el chat y traer la respuesta al chat del motor/calibración.
**Para la siguiente IA:** PERPLEXITY: busca el manual del MC-5438 y responde en tabla con URL: tipo de salida para SSR (voltaje), tiempo de ciclo de la salida (valor por defecto y rango), parámetros PID y sus unidades (banda P en % o °C, I y D en s), rangos de cada uno, autotune (cómo funciona), programas de rampa/meseta (cuántos pasos), tipo de termopar aceptado y precisión. Cierra con tu entrada de bitácora en un bloque de código con el formato de CONTRATO.md §7.

### 2026-11-08 19:36 — Claude Opus 5.5 — PREGUNTA
**Qué:** Tarea para GEMINI (Deep Research, modelo Argon o Pro). Investigar con fuente los datos del café y del reactor que el modelo hoy tiene como [Supuesto].
**Archivos:** Gemini crea en Drive, carpeta Proyectos IA / horno-vertical, el Doc "Investigación — datos del café y del reactor".
**Fuentes:** Solo artículos revisados por pares, libros o fichas técnicas. Cada valor con autor, año, DOI o URL, tabla o página, y el método de medida.
**Verificado:** n/a (lo revisa Claude con una entrada REVISIÓN).
**Para Nick:** Abrir Gemini Deep Research, pegar el link de esta bitácora y decirle: "Haz la tarea de Gemini de la bitácora horno-vertical".
**Para la siguiente IA:** GEMINI: (1) Composición del residuo de café usado (spent coffee grounds) en base seca: celulosa, hemicelulosa, lignina (y si hay, ácido-soluble/insoluble), lípidos, proteína, extractivos. (2) Análisis elemental C, H, O, N y poder calorífico. (3) Propiedades del lecho de café molido: densidad aparente, porosidad, conductividad térmica efectiva y cp vs. temperatura. (4) Emisividad del acero inoxidable AISI 304 oxidado entre 300 y 600 °C. (5) TGA/DTG de residuo de café en N2 a 5–20 °C/min: temperaturas de pico, pérdida de masa por etapa, residuo a 600–700 °C. (6) Cinética de pirólisis de lípidos o aceite de café si existe. Entrega una tabla por tema: parámetro | valor | unidad | rango entre fuentes | fuente exacta | método. Si no encuentras algo, escribe "no encontrado"; no inventes ni redondees. Al terminar, escribe tu entrada HECHO arriba, debajo de "Entradas", con este mismo formato.

### 2026-11-08 19:33 — Claude Opus 5.5 — PREGUNTA
**Qué:** Datos que faltan para calibrar el modelo con el horno real.
**Archivos:** ninguno.
**Fuentes:** revisión de Max_Power/01_Horno_Vertical/datos/ (Mac de Nick).
**Verificado:** n/a.
**Para Nick:** (1) ¿"Café grano" del FTIR es el mismo residuo de tinto del reporte GIEM 28ago2604? (2) Masas de la corrida "Pirolizado 1-2": café cargado, biochar obtenido, rampa y T final. (3) Cualquier registro de temperatura de esa corrida. (4) Fuente de la composición celulosa/hemicelulosa/lignina/lípidos (12/35/28/15 %).
**Para la siguiente IA:** no tratar esa composición como dato del GIEM: el reporte no la trae.

### 2026-11-08 19:33 — Claude Opus 5.5 — HECHO
**Qué:** Se abre el proyecto. Modelo traído al Mac, corrida medida, barrido en paralelo probado, datos revisados y plan aprobado por Nick (A motor nuevo → B calibración térmica → C app Streamlit).
**Archivos:** proyectos/horno-vertical/CONTEXTO.md, BITACORA.md; en el Mac: Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee/ (copia del repo, commit ddb0a63) y modelos/barrido_paralelo.py.
**Fuentes:** repo nicolascalle8-glitch/PyrolysisReactorCoffee (docs/EVALUACION_CINETICAS.md); reporte GIEM 28ago2604 (7-sep-2026); FTIR muestras 013/014/015 (4-sep-2026).
**Verificado:** caso base (10 °C/min, 500 °C, 30 min, 8 % humedad) corrido en la VM del Mac: 25 s, biochar 24.93 %, bio-oil 38.94 %, gas 20.23 %, agua 15.90 %, balance 100.000 % (igual al informe). Barrido demo 4 casos con 4 procesos: x3.1.
**Para Nick:** nada (el plan ya lo aprobó en el chat).
**Para la siguiente IA:** la shell de Claude en el Mac es una VM Linux de 4 núcleos y ~3 GB; las corridas grandes van en la Terminal de macOS. El GIEM solo reporta humedad 61.2 % bh, cenizas 2.31 % bs, pérdida por calcinación 650 °C 97.7 % bs, CO 49.4 % bs, N 0.418 % bs, C/N 118.2.

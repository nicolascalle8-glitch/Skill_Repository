# BITÁCORA — Morcelador contenido

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra. Esta bitácora es la misma que el Doc de Drive "Bitácora – morcelador-contenido" (1K9-2UZJSV0wwkSG9HuYTCGWawoseDuFHrtyDj94Em5U). Las entradas anteriores al 2026-11-11 12:55 (Gemini, Perplexity, Comet, Claude) están solo en ese Doc.

## En curso

- (nada)

## Propuestas sin respuesta

- (ninguna)

## Entradas

### 2026-11-11 13:00 — Perplexity Computer (Claude Opus 5.5) — HECHO
- **Qué:** Búsqueda de motorreductores con eje normal para el banco (Uso A: 12 V, 800–1500 rpm, bloqueo ≥0,5 N·m) y para el mango (Uso B: Ø≤32 mm, L≤70 mm, ≤150 g, 2S/3S, 1000–2000 rpm, nominal ≥0,2 N·m). Medellín (Didácticas, BigTronica): nada en el rango. Uso A: goBILDA 5202-0002-0005 (1150 rpm, bloqueo 7,9 kg·cm) cumple pero está agotado en Dynamo (Bucaramanga, $297.000) y descontinuado; Pololu #4748 10:1 (1000 rpm, bloqueo 4,9 kg·cm, 4 % corto) disponible en ja-bots Bogotá a $230.000 + IVA; afuera NFP-36GP-555 1260# (1150 rpm, nominal 3 kg·cm, bloqueo ≥7 kg·cm) y NFP-42GP-775 3,7:1 (1100 rpm, nominal 5,5 kg·cm). Uso B: ningún motor cumple; 0,2 N·m a 1000–2000 rpm pide 21–42 W en el eje y los de 25–28 mm publican ≤12 W.
- **Archivos:** proyectos/morcelador-contenido/archivos/investigacion-motores-banco-y-mango-2026-11-11.md (fichas, tablas A y B, enlaces).
- **Fuentes:** Hoja goBILDA 5202-0002-0005, ficha y hoja 37D de Pololu, fichas NFP (36GP-555, 42GP-775, GA28Y-385), SLW, SGMADA, páginas de Dynamo, ja-bots, Vistronica, Didácticas, BigTronica, AliExpress. Enlaces en el archivo.
- **Verificado:** Cada valor sale de la página o PDF citado; lo no publicado quedó como NO ENCONTRADO. No verificado: MercadoLibre y el catálogo de Electronilab (no cargaron), WhatsApp de Didácticas, existencias reales.
- **Para Nick:** Elegir motor del banco: Pololu #4748 (en Bogotá, 4 % corto de bloqueo) o importar NFP-36GP-555 1260#. Para el mango hay que bajar el torque nominal, aceptar Ø36 mm o pedir un BLDC con driver a fabricante. Antes de comprar, preguntar por WhatsApp a BigTronica y Didácticas.
- **Para la siguiente IA:** Leer el archivo de la investigación antes de volver a buscar motores. Con un motor elegido, revisar el torque de corte (0,055–0,165 N·m) contra el nominal del motor y ajustar el banco en Fusion.

### 2026-11-11 12:55 — Claude (Opus 5.5) — HECHO
- **Qué:** Handover del chat de diseño (auditoría 🟡 65/100). Proyecto creado en el repo: CONTEXTO.md, HANDOVER.md, BITACORA.md y archivos/ (reporte Fase 1, Fase 3 v2, roadmap, scripts de Fusion del banco y del prototipo). Registrado en registry/DRIVE.yml.
- **Archivos:** proyectos/morcelador-contenido/ en Skill_Repository.
- **Fuentes:** chat de Claude del 2026-11-10 y 2026-11-11.
- **Verificado:** CONTEXTO con menos de 1.500 palabras; archivos copiados y subidos.
- **Para Nick:** abrir un chat nuevo con el mensaje de arranque; correr el prompt de motores en Perplexity; dar permiso para guardar los diseños en Fusion.
- **Para la siguiente IA:** diseño acordado = v3 (motor fuera del eje, rotor hueco con anillo de imanes, funda con adaptador y túnel, válvula trasera). Leer CONTEXTO.md.

# CONTEXTO — Morcelador contenido (morcelador-contenido)

Actualizado: 2026-11-11 12:55 (Bogotá). Lee solo esto para arrancar. El historial completo está en HANDOVER.md y solo se abre si Nick pregunta por algo del pasado.

## En una frase
Morcelador laparoscópico inalámbrico y en bolsa para el Dr. Gustavo Calle (papá de Nick, ginecólogo). Concepto aprobado; vamos en el banco de pruebas y en el prototipo imprimible **v3** (con canal central para sacar el mioma). **Confidencial hasta radicar la patente.**

## Tu siguiente tarea
1. Leer en la bitácora de Drive (doc 1K9-2UZJSV0wwkSG9HuYTCGWawoseDuFHrtyDj94Em5U) la entrada de Perplexity con los motores (uso A banco, uso B mango). Si no está, pedirle a Nick que corra ese prompt.
2. Elegir motor A (banco) y B (mango) con sus medidas reales.
3. Modelar el **prototipo v3** en Fusion con el conector (Nick no pega scripts). Ver diseño abajo.
4. Revisar interferencias, sacar capturas, pasar por `puerta-fabricacion`, exportar STL. Pedir permiso antes de guardar.
5. Entrada en la bitácora de Drive y en `BITACORA.md`.

## Diseño v3 (acordado con Nick 2026-11-11)
- **Mango reutilizable** sellado, no estéril, se limpia con toallita. Forma de pistola; 2 pilas 18650 en la empuñadura.
- **Canal central libre de punta a punta**: la pinza (tenáculo de 10 mm) entra por detrás y la tira de mioma sale por el centro.
- **Motor fuera del eje**, en la parte alta de la empuñadura, paralelo al eje, desplazado ~30 mm. Mueve con **engranajes rectos** un **rotor hueco** (sobre 2 rodamientos de pared delgada) que lleva los **imanes motrices en anillo** (8 imanes N52 10 × 3, círculo ~Ø34 → hueco central ~Ø20).
- **Funda plástica estéril desechable** sobre todo el mango, con:
  - **anillo adaptador rígido** en la punta: bayoneta de 2 pernos, giro 30°, sobre la nariz del mango; ventana central donde solo queda el plástico (el torque pasa magnéticamente, la funda no se perfora);
  - **túnel interno** (tubo rígido delgado) que atraviesa el canal del mango y termina atrás en una **válvula de sello** (mantener neumoperitoneo).
- **Cartucho desechable** con bayoneta sobre el adaptador: **anillo conducido** de imanes + **tubo cuchilla** pegado al anillo, girando en un buje; collar para la bolsa; imán de enclavamiento (r = 22,5 mm) que un sensor Hall del mango detecta a través de la funda → sin cartucho/bolsa no arranca.
- **Canal se agranda hacia atrás**: cuchilla ID 11 → túnel ID ~12 → válvula ~12,5. Sin escalones.
- Largo de canal del mango ≤ ~120 mm (que la pinza estándar alcance).
- Separación entre imanes en v2: 1,9 mm (pared 0,8 + funda). Mantener o mejorar.

## Hechos clave (exactos)
- Trocar máximo 12 mm. Tubo cuchilla de prueba: acero 304 **12 × 0,5 mm** (AliExpress Metals World $12.753) — para prototipo; el real ≤ 11,5 mm OD.
- Tope: **< 2.000.000 COP por mango nuevo** (≈ USD 620, TRM 3.228,26 del 6-nov-2026). Desechables aparte.
- Torque de corte estimado [EST]: 0,055–0,165 N·m (11 mm, 10–30 N). ~9–27 W eléctricos a 1000 rpm; ~13 Wh para 30 min.
- JGB37-520: bloqueo 0,16 N·m @1000 rpm, 0,10 @1590 → **no sirve para el banco**. Sirve para la maqueta.
- Banco: rodamientos 6808 (40 × 52 × 7), celda 1 kg 80 × 12,7 × 12,7 + HX711, riel MGN12H (H = 13, 4 × M3 en 20 × 20), ESP32, BTS7960. Total ~COP 644.000.
- Imanes N52 10 × 3: 100 u $87.946 (MercadoLibre internacional).
- INVIMA: Decreto 4725/2005 vigente → probable clase IIa (registro automático). Proyecto de decreto nuevo sigue en borrador.
- FDA: desde dic-2020 solo morcelación contenida; jul-2026 Claria (DEN250034, código SIM, cuchilla 34 mm, consola, bolsa vaginal).
- Patentes: en SIPI no hay patentes de LiNA, Applied Medical, Tavigny, Brigham, Blue Endo, Claria (búsqueda parcial de Comet). Antecedentes mundiales activos: Tavigny US11974777 (fuga por presión, 2036), Brigham US11103274 (parada por carga, 2034), Blue Endo US9877740 (escudo con bolsa). **Espacio libre**: cartucho pre-unido a la bolsa + enclavamiento magnético a través de la funda + torque magnético por la misma pared.

## Decisiones vigentes (no reabrir)
- Concepto A (mango reutilizable + desechables). Concepto B descartado.
- Funda plástica, no carcasa rígida.
- Canal central libre; motor fuera del eje.
- Cuchilla rotatoria.
- Patente solo Colombia (SIC), invención → convertible a modelo de utilidad (Dec. 486 art. 35).
- Nada público antes de radicar la patente.

## Restricciones
- Pruebas solo en banco y tejido animal ex vivo. Nunca pacientes.
- No usar recursos de la EIA ni de la práctica (propiedad intelectual).
- Fusion: crear diseños nuevos; no tocar archivos de Nick; no guardar sin permiso. Los cortes deben afectar solo su componente (`participantBodies`).

## Pendientes abiertos
- [ ] Motores (Perplexity) — Nick
- [ ] Prototipo v3 en Fusion — Claude
- [ ] Guardar banco y prototipo v2 en Fusion (están abiertos sin título) — pedir permiso
- [ ] Tamaño de mioma y tiempo de morcelación actual — Nick pregunta al Dr. Calle
- [ ] Acuerdos: opciones A/B, [CONFIRMAR], abogado — Nick
- [ ] HX711 pin RATE en alto — Nick
- [ ] Copias viejas de Fase 3/Roadmap en Drive — Gemini

## Criterio de cierre (v3)
- [ ] v3 en Fusion sin interferencias, todas las operaciones sanas
- [ ] STL por pieza + tabla de impresión (material, orientación)
- [ ] Pasó `puerta-fabricacion`

## Preguntas abiertas
- A1 vs A2 → banco. Motor del mango → Perplexity. Engranajes rectos vs otra transmisión.

## Cómo quiere trabajar Nick aquí
- Español simple y directo. Corto.
- Delegar: Perplexity (datos con fuente), Comet (webs con formularios: SIPI, SECOP, tiendas), Gemini (Drive/documentos), Copilot (código). Claude solo en compuertas, diseño y revisión.
- Prompts listos para copiar; tiendas locales primero (Didácticas Electrónicas, BigTronica en Medellín).
- Claude corre Fusion directo.

## Errores que no repetir
- Diseñar contra lo que Nick escribió (pidió funda plástica desde el inicio).
- Olvidar el canal central de extracción.
- Cortes de extrusión que atraviesan otros componentes en Fusion.

## Mapa de archivos (abrir solo cuando la tarea lo pida)
| Archivo | Qué tiene | Abrir cuando |
|---|---|---|
| archivos/prototipo_morcelador_v1.py | Script base del prototipo (helpers de Fusion) | Para reutilizar funciones al modelar v3 |
| archivos/banco_morcelador_v1.py | Banco de pruebas | Ajustar el banco al motor nuevo |
| archivos/fase3-conceptos-banco-v2.md | Conceptos A/B, puntajes, banco, respuestas del Dr. Calle | Dudas de concepto o banco |
| archivos/roadmap-y-guia.md | 11 etapas con compuertas | Planear siguiente etapa |
| archivos/fase1-reporte-investigacion.md | Regulación, competencia, patentes, costos | Patente, INVIMA o costos |
| Bitácora Drive (1K9-2UZJ…) | Entradas de todas las IAs | Siempre al empezar (últimas 3) |
| HANDOVER.md | Historial | Nick pregunte por el pasado |

## Glosario
- **Mango**: parte reutilizable (motor, batería, electrónica). **Funda**: plástico estéril desechable con adaptador y túnel. **Cartucho**: desechable con cuchilla, anillo magnético y collar de bolsa.
- **A1/A2**: acople magnético del lado cuchilla (A1) o del lado motor con engranaje en el cartucho (A2).
</content>

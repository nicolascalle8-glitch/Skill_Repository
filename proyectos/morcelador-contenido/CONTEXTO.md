# CONTEXTO — Morcelador contenido (morcelador-contenido)

Actualizado: 2026-11-12 13:28 (Bogotá). Lee solo esto para arrancar. El historial completo está en HANDOVER.md y solo se abre si Nick pregunta por algo del pasado.

## En una frase
Morcelador laparoscópico inalámbrico y en bolsa para el Dr. Gustavo Calle (papá de Nick, ginecólogo). Concepto aprobado. Banco v2 modelado. Prototipo **v3** modelado e impresión preparada; **v3.1 (con fijaciones) quedó SIN TERMINAR** (ver abajo). **Confidencial hasta radicar la patente.**

## Tu siguiente tarea: PROBAR EL v3.2
Estado (2026-11-12 13:28): el v3.2 reemplaza al v3.1 (que no se podía armar). Script `archivos/prototipo_morcelador_v3_2.py`; STL en `Documentos\morcelador_STL\v3_2`; placas laminadas sin guardar (X2D 2h11m, K2 6h53m). Cambios: tubo del canal aparte (se mete al final), válvula con bayoneta + O-ring + tapa con 3 M2, cuchilla impresa con lengüetas, empuñadura de 27 mm con 18650 en línea, sin tapa de baterías. Falta:
1. Nick: guardar el diseño, imprimir, armar y decir qué falla.
2. Aprobar o no: sin tapa de baterías; motor B2-1 y 2,75:1 (hoy 43/17).
3. Medir lo "por calibrar" (motor, O-ring, insertos M2) y la probeta de holguras.

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
- [x] Prototipo v3 y banco v2 modelados en Fusion (2026-11-11 13:25, sin guardar) — Claude
- [ ] Guardar v3 y banco v2 + exportar STL — permiso de Nick
- [ ] Aprobar separación 1,6 mm y Hall abajo (ver bitácora 13:25) — Nick
- [ ] Motor del mango con requisito corregido (Perplexity, Uso B v2) — Nick
- [ ] rpm de los morceladores Storz — Nick
- [x] v3.2 modelado completo, STL y placas laminadas (2026-11-12 13:28) — Claude
- [ ] Guardar v3.2, imprimir y armar — Nick
- [ ] Decidir motor del mango B2-1 (RS-380PH-4045 + 5:1) y enviar consulta a SLW — Nick
- [ ] Tamaño de mioma y tiempo de morcelación actual — Nick pregunta al Dr. Calle
- [ ] Acuerdos: opciones A/B, [CONFIRMAR], abogado — Nick
- [ ] HX711 pin RATE en alto — Nick
- [ ] Copias viejas de Fase 3/Roadmap en Drive — Gemini

## Criterio de cierre (v3.2)
- [x] v3.2 completo en Fusion, sin interferencias, todas las operaciones sanas
- [x] STL por pieza + placas laminadas
- [x] puerta-fabricacion = PRUEBA LIMITADA (banco y ex vivo; la cuchilla impresa no corta tejido)
- [ ] Armado real sin piezas flojas (Nick)

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
- Piezas que no se pueden montar: revisar el orden de montaje antes de partir el mango (v3.1).

## Mapa de archivos (abrir solo cuando la tarea lo pida)
| Archivo | Qué tiene | Abrir cuando |
|---|---|---|
| archivos/prototipo_morcelador_v3_2.py | v3.2 completo (armable) | **Siempre: modelo vigente** |
| archivos/prototipo_morcelador_v3_1.py | v3.1 (no se podía armar) | Comparar |
| archivos/prototipo_morcelador_v3.py | v3 completo (túnel 0,8 mm) | Comparar con el v3.1 |
| archivos/investigacion-motores-banco-y-mango-2026-11-11.md | Motores banco y mango (Perplexity) | Integrar el motor B2-1 |
| archivos/prototipo_morcelador_v1.py | Script base viejo | Casi nunca |
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

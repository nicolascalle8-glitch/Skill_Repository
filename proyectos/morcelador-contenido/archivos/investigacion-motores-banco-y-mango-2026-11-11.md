# Búsqueda de motorreductores — banco (Uso A) y mango (Uso B)

Perplexity Computer (Claude Opus 5.5) · 2026-11-11 · Confidencial (proyecto morcelador).
Regla: lo que no está publicado en la fuente = NO ENCONTRADO. No se usaron datos de modelos parecidos.

## Requisitos

- **Uso A – banco de pruebas:** 12 V, 800–1500 rpm a la salida, torque de bloqueo ≥ 0,5 N·m (≥ 5 kg·cm), eje normal (no hueco), tamaño libre.
- **Uso B – mango del instrumento:** Ø ≤ 32 mm, largo total ≤ 70 mm, ≤ 150 g, 7,4 V (2S) u 11,1 V (3S) con 18650, 1000–2000 rpm, nominal ≥ 0,2 N·m y bloqueo ≥ 0,5 N·m.

## Resultado corto

- **Medellín:** nada en el rango. Didácticas Electrónicas: el JGB37 más rápido es el JGB37-550 12 V 500 rpm, $77.087 (https://www.didacticaselectronicas.com/shop?search=JGB37). BigTronica: 300 rpm como máximo a 12 V (https://bigtronica.com/motorreductor), WhatsApp 315 643 53 52.
- **Uso A:** la única opción en Colombia que cumple (goBILDA 5202 en Dynamo) está agotada; el Pololu #4748 (ja-bots, Bogotá) está disponible pero le falta 4 % de torque de bloqueo. Afuera: NFP-36GP-555 y NFP-42GP-775 con ficha publicada.
- **Uso B:** ningún motor encontrado cumple. 0,2 N·m a 1000–2000 rpm = 21–42 W en el eje; los motores de 25–28 mm revisados publican 12 W o menos.

## Uso A — opciones

### A1. goBILDA/ServoCity 5202-0002-0005 (planetario 5,2:1, motor RS-555, encoder)
- Tienda: Dynamo Electronics, Bucaramanga. $297.000. AGOTADO. No se recoge en Medellín. https://www.dynamoelectronics.com/tienda/motorreductor-12v-1150rpm-reduccion-51-encoder/
- El fabricante lo marca descontinuado: https://www.servocity.com/5202-series-yellow-jacket-planetary-gear-motor-5-2-1-ratio-1150-rpm-3-3-5v-encoder
- Hoja: https://www.gobilda.com/content/spec_sheets/5202-0002-0005_spec_sheet.pdf
- 1150 rpm sin carga; bloqueo 7,9 kg·cm (0,77 N·m) con 9,2 A; 0,25 A sin carga; 387 g.
- Medidas: el plano muestra Ø32 y Ø37,5 mm y largo 108,5 mm; Dynamo dice 37,5 × 132,8 mm → confirmar en el plano.
- Eje 6 mm con plano D de 5,5 mm; el plano muestra 24 y 21,5 mm sin decir cuál es el largo del eje.
- Montaje: M4×0,7, 10 mm de profundidad; cotas de 16 y 32 mm sin decir cuál es el círculo (ServoCity habla de patrón goBILDA de 16 mm).
- Nominal: NO ENCONTRADO (Dynamo: 1 kg·cm y 2 A en máxima eficiencia).

### A2. Pololu #4748 (10:1, 37D × 50L mm, 12 V) — casi cumple
- Tienda: ja-bots, Bogotá. $230.000 + IVA (≈ $273.700). 2 disponibles. No se recoge en Medellín. https://ja-bots.com/categoria-producto/motores/motorreductores/
- Ficha: https://www.pololu.com/product/4748/specs · Hoja 37D: https://www.pololu.com/file/0J1736/pololu-37d-metal-gearmotors-rev-1-2.pdf
- 1000 rpm sin carga; bloqueo 4,9 kg·cm (0,48 N·m) con 5,5 A → 4 % por debajo de 5 kg·cm.
- Ø37 mm × 50 mm (sin eje ni terminales); 175 g; eje 6 mm con plano D, 16 mm.
- Nominal: NO ENCONTRADO (máx. eficiencia: 0,66 kg·cm a 850 rpm, 0,91 A). Montaje: NO ENCONTRADO.

### A3. NFP-36GP-555, versión 12 V "1260#" (5,2:1)
- Tienda del fabricante NFP (internacional). 30,00 (moneda no indicada); COP NO ENCONTRADO. https://nfpshop.com/product/36mm-dc-planetary-geared-motor-model-nfp-36gp-555
- 1150 rpm sin carga (≤0,4 A); nominal 3 kg·cm a 880 rpm (≤2,0 A); bloqueo ≥7 kg·cm (≤9,5 A).
- Ø36 mm, caja 26,5 mm, largo total NO ENCONTRADO; ≈450 g; eje 8 mm × 20 mm; plano D y montaje NO ENCONTRADO.

### A4. NFP-42GP-775, 3,7:1 a 12 V
- Tienda del fabricante (PMD/NFP, internacional). 50,00; COP NO ENCONTRADO. https://precisionminidrives.com/product/42mm-planetary-gear-motor-model-nfp-42gp-775
- 1100 rpm sin carga (≤500 mA); nominal 5,5 kg·cm (0,53 N·m) a 550 rpm (≤6 A); 12 A en bloqueo.
- Bloqueo: NO ENCONTRADO (el nominal publicado ya pasa de 0,5 N·m).
- Ø42 mm, caja 33,5 mm, largo total NO ENCONTRADO; ≈730 g; eje 8 mm con plano D de 12 mm, 22 mm. Montaje NO ENCONTRADO.

### A5. AliExpress (sin ficha técnica)
- 36PG-555, Motor Factory Store, opción 1538 rpm, US$27,18: https://www.aliexpress.com/i/1005002965382699.html
- 42-775, Bobo02 Store, opciones 1160 y 1600 rpm, US$39,99: https://www.aliexpress.com/item/1005010587045877.html
- Torque, corriente, medidas y montaje: NO ENCONTRADO en los dos.

## Uso B — más cercanos (ninguno cumple)

| Modelo | Fuente | rpm | Nominal | Bloqueo | Notas |
|---|---|---|---|---|---|
| JGA25-370 1360 rpm | Vistronica, Bogotá — https://www.vistronica.com/robotica/motores/motorreductores/motorreductor-con-encoder-jga25-370-1360-rpm-01-kgcm-detail.html | 1360 | 0,1 kg·cm (0,07 A) | 0,4 kg·cm (1,8 A) | 83 g; precio y medidas NO ENCONTRADO |
| NFP-GA28Y-385 4:1 | NFP — https://nfpshop.com/product/28mm-planetary-gear-motor-model-nfp-28-385 | 1000 (12 V) | 0,3 kg·cm | 0,7 kg·cm | Ø28; 15,50 |
| SLW BLDC 28 mm 4:1 12 V | SLW — https://slwmotor.com/product/28mm-diameter-brushless-dc-motor-with-planetary-gearbox/ | 2000 | 0,5 kg·cm (1,25 A) | 1,5 kg·cm (3,4 A) | caja 23,2 mm |
| SGMADA PG28-395 (24 V) | SGMADA — https://sggearbox.com/product/pg28-395/ | 790 (nominal) | 0,14 N·m | 1,52 N·m | el más cercano; es de 24 V |

El NFP-36GP-555 (A3) cumple el torque nominal pero mide Ø36 mm y pesa ≈450 g. Para el Uso B hay que bajar el torque nominal, aceptar Ø36 mm o pedir un BLDC con driver a un fabricante.

## Tablas resumen

### Uso A
| Modelo | Tienda | Ciudad | COP | rpm | Torque nominal | Torque de bloqueo | Ø × L | Enlace |
|---|---|---|---|---|---|---|---|---|
| goBILDA 5202-0002-0005 | Dynamo (agotado) | Bucaramanga | $297.000 | 1150 | NO ENCONTRADO | 7,9 kg·cm | 37,5 × 108,5 (o 132,8) mm | https://www.dynamoelectronics.com/tienda/motorreductor-12v-1150rpm-reduccion-51-encoder/ |
| Pololu #4748 10:1 | ja-bots (2 und.) | Bogotá | $230.000 + IVA | 1000 | NO ENCONTRADO | 4,9 kg·cm (no cumple) | 37 × 50 mm | https://ja-bots.com/categoria-producto/motores/motorreductores/ |
| NFP-36GP-555 1260# | NFP | Internacional | NO ENCONTRADO (30,00) | 1150 | 3 kg·cm | ≥7 kg·cm | 36 × NO ENCONTRADO | https://nfpshop.com/product/36mm-dc-planetary-geared-motor-model-nfp-36gp-555 |
| NFP-42GP-775 3,7:1 | PMD/NFP | Internacional | NO ENCONTRADO (50,00) | 1100 | 5,5 kg·cm | NO ENCONTRADO | 42 × NO ENCONTRADO | https://precisionminidrives.com/product/42mm-planetary-gear-motor-model-nfp-42gp-775 |
| 36PG-555 1538 rpm | AliExpress | China | NO ENCONTRADO (US$27,18) | 1538 | NO ENCONTRADO | NO ENCONTRADO | NO ENCONTRADO | https://www.aliexpress.com/i/1005002965382699.html |
| 42-775 1160/1600 rpm | AliExpress | China | NO ENCONTRADO (US$39,99) | 1160 / 1600 | NO ENCONTRADO | NO ENCONTRADO | 42 × NO ENCONTRADO | https://www.aliexpress.com/item/1005010587045877.html |

### Uso B (ninguno cumple)
| Modelo | Tienda | Ciudad | COP | rpm | Torque nominal | Torque de bloqueo | Ø × L | Enlace |
|---|---|---|---|---|---|---|---|---|
| JGA25-370 1360 rpm | Vistronica | Bogotá | NO ENCONTRADO | 1360 | 0,1 kg·cm | 0,4 kg·cm | NO ENCONTRADO | https://www.vistronica.com/robotica/motores/motorreductores/motorreductor-con-encoder-jga25-370-1360-rpm-01-kgcm-detail.html |
| NFP-GA28Y-385 4:1 | NFP | Hong Kong | NO ENCONTRADO (15,50) | 1000 (12 V) | 0,3 kg·cm | 0,7 kg·cm | 28 × NO ENCONTRADO | https://nfpshop.com/product/28mm-planetary-gear-motor-model-nfp-28-385 |
| SLW BLDC 28 mm 4:1 | SLW | Internacional | NO ENCONTRADO | 2000 | 0,5 kg·cm | 1,5 kg·cm | 28 × NO ENCONTRADO | https://slwmotor.com/product/28mm-diameter-brushless-dc-motor-with-planetary-gearbox/ |
| SGMADA PG28-395 (24 V) | SGMADA | China | NO ENCONTRADO | 790 (nominal) | 0,14 N·m | 1,52 N·m | 28 × NO ENCONTRADO | https://sggearbox.com/product/pg28-395/ |

## No encontrado / no revisado

- WhatsApp de Didácticas Electrónicas.
- MercadoLibre Colombia: las páginas no cargaron; sin datos de ofertas.
- Electronilab: catálogo no cargó; solo apareció un N20 12 V 1000 rpm, sin torque revisado.
- Montaje de Pololu 37D, NFP y AliExpress; nominal de goBILDA y Pololu; bloqueo de NFP-42GP-775; precios en COP de tiendas internacionales.
- Antes de comprar: preguntar por WhatsApp a BigTronica y Didácticas, y revisar MercadoLibre a mano, si tienen algo de 36–42 mm y ~1000 rpm.

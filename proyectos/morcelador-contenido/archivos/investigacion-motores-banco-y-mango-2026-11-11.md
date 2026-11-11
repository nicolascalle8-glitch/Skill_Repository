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

## Anotaciones de Perplexity

Estas notas son mías. Las que dicen "estimación" son cálculos con un modelo simple, no salen de las fichas.

### Cómo se buscó
- Orden de tiendas que pidió Nick: Medellín (Didácticas Electrónicas, BigTronica), luego el resto de Colombia (MercadoLibre, Electronilab, Vistronica, Dynamo, Sigma, Ferretrónica, y también ja-bots), y AliExpress o el fabricante solo cuando en Colombia no había nada.
- Revisé el 36GP-555, el 42GP-775, el 775 con reducción, el JGB37 de baja velocidad, planetarios de 22–32 mm con 370/385/395 o BLDC, el GA25/JGA25 y motores de destornillador.
- Cada valor sale de la ficha o la página citada. Si una tienda y el fabricante no coinciden, anoté las dos cifras.
- Conversión: 1 kg·cm = 0,0981 N·m. 5 kg·cm ≈ 0,49 N·m, por eso usé 5 kg·cm como el límite de 0,5 N·m.
- El precio de ja-bots con IVA ($273.700) sale de $230.000 × 1,19.

### Torque de corte contra el motor (Uso A)
- El torque de corte estimado es 0,055–0,165 N·m (entrada de Claude, 2026-11-11 10:45; tubo de 12 × 0,5 mm).
- Estimación con la recta torque–velocidad de un motor DC, \(n \approx n_0\,(1 - T/T_{bloqueo})\), a 0,165 N·m:
  - goBILDA 5202 (1150 rpm, 0,77 N·m): ≈ 905 rpm. Queda dentro de 800–1500.
  - NFP-36GP-555 1260# (1150 rpm, bloqueo ≥0,69 N·m): ≈ 875 rpm o más. Queda dentro.
  - Pololu #4748 (1000 rpm, 0,48 N·m): ≈ 655 rpm. Cae por debajo de 800 rpm con el corte más duro. Con 0,055 N·m daría ≈ 885 rpm.
  - NFP-42GP-775 3,7:1: la ficha da 550 rpm con 0,53 N·m. Si se interpola entre 1100 rpm sin carga y ese punto, a 0,165 N·m daría ≈ 930 rpm.
- Conclusión: el Pololu sirve solo para la parte baja del corte. Para cubrir todo el rango sin bajar de 800 rpm, conviene el A1 o el A3.
- Las fichas no publican la eficiencia de la caja ni cuánto se calienta el motor si trabaja mucho tiempo cerca del bloqueo. El banco no debería pasar mucho tiempo a más del 30–40 % del bloqueo.

### Fuente y conexión (Uso A)
- Para el arranque y el bloqueo, la fuente de 12 V tiene que dar esta corriente: goBILDA 9,2 A, NFP-36GP-555 ≤9,5 A, NFP-42GP-775 12 A, Pololu 5,5 A. Una fuente de 12 V y 10 A no alcanza para el 775 si se bloquea, salvo que tenga limitador de corriente.
- Ejes: goBILDA y Pololu son de 6 mm con plano D; los NFP son de 8 mm. Para pasar al tubo de 12 mm hace falta un acople de 6→12 u 8→12 mm. El sensor de torque, si va en línea, define el acople.
- El largo del goBILDA no coincide entre el plano (108,5 mm) y Dynamo (132,8 mm). Puede ser con o sin encoder; hay que confirmarlo en el plano antes de diseñar el soporte.

### Uso B: por qué no hay motor
- Potencia en el eje: \(P = T\,\omega\). 0,2 N·m a 1000 rpm (104,7 rad/s) = 20,9 W; a 2000 rpm = 41,9 W.
- Estimación: con una eficiencia total de 60–70 %, la entrada eléctrica sería de 30–70 W. Con 2S (7,4 V) son unos 4–9 A continuos y con 3S (11,1 V) unos 3–6 A. Un 370/385 de 25–28 mm no aguanta eso de forma continua. Las fichas revisadas publican 12 W o menos.
- El más cercano es el SGMADA PG28-395: el bloqueo pasa de sobra (1,52 N·m), pero el nominal es 0,14 N·m a 790 rpm y es de 24 V.
- Opciones para seguir: (1) bajar el nominal del mango a lo que de verdad pide el corte (≤0,165 N·m, y probablemente menos en uso normal); (2) aceptar Ø36 mm (NFP-36GP-555, pero pesa ≈450 g, lo que choca con ≤150 g); (3) pedirle a un fabricante (SLW, SGMADA, NFP) un BLDC de 28–32 mm con planetario y driver a 2S/3S; (4) en destornilladores no encontré fichas con torque y rpm publicados en el rango.

### Descartes
- JGB37-520 y JGB37-550: no sirven para el banco. La versión más rápida que hay en Medellín es de 500 rpm.
- N20 de Electronilab (12 V, 1000 rpm): no publica torque. No sirve para el banco.
- AliExpress (A5): hay rpm, pero no hay torque ni corriente. Solo serviría si el vendedor envía la ficha.

### Pendiente
- Que Nick elija el motor del banco: A2 (Pololu, en Bogotá, 4 % corto de bloqueo y lento con el corte duro) o importar el A3 (NFP-36GP-555 1260#).
- Preguntar por WhatsApp a BigTronica (315 643 53 52) y Didácticas si tienen algo de 36–42 mm a unos 1000 rpm.
- Revisar MercadoLibre a mano, porque desde aquí no cargó.
- Definir el torque nominal real del mango antes de volver a buscar el motor del Uso B.

## Uso B v2 (mango con engranaje recto de ~2,75:1) — 2026-11-11 13:26

Perplexity Computer (Claude Opus 5.5). Se usó la misma regla: lo que no está publicado = NO ENCONTRADO. Lo marcado como "estimación" es un cálculo mío, no viene de una ficha.

### Requisito nuevo
- Salida del motorreductor (o del motor sin caja): 2500–3500 rpm con carga.
- Torque nominal ≥ 0,6 kg·cm (0,06 N·m) a esa velocidad; torque de bloqueo ≥ 2 kg·cm (0,2 N·m).
- Alimentación 2S 18650: 7,4 V nominal (6–8,4 V).
- Ø ≤ 28 mm (máximo 32), largo ≤ 60 mm sin eje, ≤ 120 g, corriente nominal ≤ 4 A.
- Sirve un BLDC con planetario (indicando driver) o un motor con escobillas con caja de 2:1 a 5:1.
- Potencia útil: 0,06 N·m × 3000 rpm ≈ 19 W. A 7,4 V y 4 A entran 29,6 W, así que la eficiencia total del motor más la caja tiene que ser de ~64 % o más. Eso deja fuera a la mayoría de los motores de 25–28 mm con caja barata.

### Tiendas revisadas (en el orden pedido)
- **Didácticas Electrónicas (Medellín):** en su categoría de motores DC hay N20 de 12 V hasta 1000 rpm, JGB37 de hasta 500 rpm, motores 795/895 de 12 V (grandes) y motorreductores de 24 V hasta 470 rpm. No hay nada de 380/385 ni planetarios de 28 mm. https://www.didacticaselectronicas.com/shop/category/motores-actuadores-solenoides-y-drivers-motores-acdc-31
- **BigTronica (Medellín):** en motores solo hay un "Motor DC 6-9V con piñón" a $10.000 sin ficha, brushless de dron de 1000 Kv (agotados) y micromotores de dron. https://bigtronica.com/motores-drones. Habría que preguntar por WhatsApp (315 643 53 52) si tienen 380/385.
- **Resto de Colombia:** no encontré motores 380/385 ni planetarios de 28 mm con ficha en Vistronica, Electronilab, Dynamo, ja-bots, Sigma ni Ferretrónica. Ja-bots tiene Pololu 20D/25D/37D, pero ninguno a 2500 rpm. MercadoLibre volvió a fallar al cargar.
- Como en Colombia no había nada, pasé al fabricante, a tiendas internacionales y a AliExpress.

### Revisado y descartado (sin estimaciones; cada valor sale de la ficha)
| Modelo | Por qué no sirve | Fuente |
|---|---|---|
| SLW BLDC 28 mm con planetario | Relación mínima publicada 4:1: 2000 rpm sin carga / 1600 nominal a 12 V, 0,5 kg·cm nominal, 1,5 kg·cm de bloqueo, 1,25 A. A 7,4 V iría más lento. La caja de 1 etapa solo se publica en 4:1 y 5:1 (22,9 mm); 3:1 y 2,5:1 = NO ENCONTRADO. Driver: NO ENCONTRADO. Precio: NO ENCONTRADO. | https://slwmotor.com/product/28mm-diameter-brushless-dc-motor-with-planetary-gearbox/ · https://slwmotor.com/product/28mm-planetary-gearbox-reducer/ |
| SLW 28 mm con escobillas (395) y planetario | 4:1 a 12 V: 2000 / 1600 rpm, 0,5 kg·cm nominal, 1,5 de bloqueo, 1,8 A | https://slwmotor.com/product/28mm-diameter-brushed-motor-with-planetary-gearbox/ |
| NFP-GA28Y-385 (todas las relaciones) | La relación mínima es 4:1. A 12 V: 1000 rpm, 0,3 / 0,7 kg·cm. Versión de 24 V: 2000 rpm, 0,5 / 1,2 kg·cm. Las otras relaciones (16:1 a 400:1) son más lentas. | https://nfpshop.com/product/28mm-planetary-gear-motor-model-nfp-28-385 |
| NFP-GA28Y-2838 BLDC | 4:1 a 12 V: 1500 rpm, 0,15 / 0,4 kg·cm. A 24 V: 3000 rpm, 0,3 / 0,8 kg·cm. US$36. | https://microdcmotors.com/product/28mm-high-torque-dc-brushless-gear-motor |
| SGMADA PG28-395 a 12 V | Variantes de 12 V: 298 y 306 rpm nominales (0,11 y 0,20 N·m) | https://sggearbox.com/product/pg28-395/ |
| Transmotec PBTI2838-12 (BLDC, driver interno) | 4:1: 1300 rpm nominales y 2,7 N·cm; motor de 12 V con 6000 rpm sin carga. Lento. | https://transmotec.com/Download/Datasheets/Transmotec-Datasheet-PBTI2838-12.pdf |
| Mechtex BI2838 / Kegu BL2838 (BLDC sin caja, driver interno) | BI2838 12 V: 4800 rpm y 1,3 N·cm. BL2838-V1 7,4 V: 4100 rpm y 7 mN·m; BL2838-V2 12 V: 3200 rpm y 12 mN·m. Muy poco torque (se pide 60 mN·m). | http://www.opis.cz/mechtex/pdf/BI%2028.pdf · https://minibldcmotor.com/product/micro-bldc-brushless-dc-motor/bl2838-bl2838i-b2838m-28mm-bldc-motor.html |
| Pololu 25D HP 6V 4.4:1 (#1570) | A 6 V: 2200 rpm, bloqueo 1,2 kg·cm, 6 A, potencia máxima 6,7 W. No llega a 2 kg·cm de bloqueo. | https://www.pololu.com/product/1570/specs |
| Faulhaber 2232U006SR | 7100 rpm sin carga a 6 V, 11 W. Con su caja más corta (3,71:1) queda lento. Desde €111,74 solo el motor (referencia). | https://www.glockenankermotor.com/dc-kleinstmotoren-faulhaber/2232...sr-faulhaber/ |
| Motores de taladro de 12 V (clase 540/550) | La clase 540 mide 35,8 mm de diámetro (Mabuchi RS-540SH), así que no cabe. En la clase 380, el motor que Mabuchi publica para taladro y destornillador es el RS-380PH-4045 (abajo). | https://www.mabuchi-motor.co.jp/motorize/branch/motor/ |

### Opciones
| # | Modelo | Tienda | COP con envío | rpm sin carga / con 0,06 N·m (7,4 V) | Torque nominal | Torque de bloqueo | Corriente nominal / bloqueo | Ø × L | Eje | Montaje | Peso | Plano / STEP | Enlace |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2-1 (recomendada) | Mabuchi RS-380PH-4045 + caja planetaria de 28 mm, 1 etapa, 5:1 | Motor: Super Radicon, Japón (¥1.139). Caja: SLW (cotizar) | NO ENCONTRADO | Estimación: 3083 / ≈2630 (≈2045 a 6,0 V y ≈3045 a 8,4 V) | Motor: NO ENCONTRADO (máxima eficiencia 11,6 mN·m a 6 V). Estimación a la salida: 0,06 N·m con ≈3,7 A | Motor: 77,5 mN·m a 6 V. Estimación a la salida, 7,4 V: ≈0,41 N·m | Motor a 6 V: 0,56 A sin carga, 3,17 A en máxima eficiencia, 18 A en bloqueo. Estimación a 7,4 V: ≈3,7 A / ≈22 A | Motor: 27,7 mm (plano 29,2 MAX) × 37,8 mm. Caja SLW 1 etapa: 22,9 mm. Total ≈ 60,7 mm | Motor 2,3 mm. Salida de la caja: NO ENCONTRADO | Motor: rosca M2,6×0,45, tornillo de 3,0 mm máx.; cantidad y círculo NO ENCONTRADO (en el plano aparece 16,0 sin decir qué mide) | Motor 80 g; caja NO ENCONTRADO | Plano del motor en la hoja de datos; STEP NO ENCONTRADO | https://product.mabuchi-motor.com/detail.html?id=99 · https://www.robotistan.com/Data/EditorFiles/%C3%9Cr%C3%BCnler%20A%C3%A7%C4%B1klama/Motorlar/Mabuchi%20RS-380PH%2016975/RS-380PH%20Datasheet.pdf · https://super-rc.co.jp/rc/product/view?id=82428 · https://slwmotor.com/product/28mm-planetary-gearbox-reducer/ |
| B2-1b | Mabuchi RS-380PH-4045 + caja de 28 mm 1:4 de AliExpress | Caja: CL Motor01 Store (R$44,09 + envío R$68,79 en la vista de Brasil) | NO ENCONTRADO | Estimación: 3854 / ≈3140 (≈2410 a 6 V) | Igual que B2-1; con 4:1 la salida da 0,06 N·m con ≈4,5 A (más de 4 A) | Estimación: ≈0,33 N·m | Estimación: ≈4,5 A / ≈22 A | Caja: largo NO ENCONTRADO | Caja: NO ENCONTRADO | Caja: NO ENCONTRADO | Caja: NO ENCONTRADO | NO ENCONTRADO | https://www.aliexpress.com/item/1005008878534309.html |
| B2-2 (referencia de precio) | maxon DCX 22 L 9 V (DCX22L01GBSL450) + GPX 22 3,9:1 (GPX22AAKLSL03D9CPLW) | maxon (tienda en línea) | NO ENCONTRADO (€217,36 + €96,94 = €314,30 sin IVA ni envío) | A 9 V el motor da 12300 rpm sin carga y 11400 nominales. Estimación a 7,4 V: 2593 / ≈2450 | Motor: 26,5 mN·m continuos (≈0,09 N·m a la salida) | Motor: 371 mN·m | Motor: 4 A continuos / 53,4 A | Ø22; caja de 19,9 mm; largo del motor NO ENCONTRADO | NO ENCONTRADO | NO ENCONTRADO | 95 + 45 = 140 g (pasa de 120) | maxon publica el plano; STEP NO ENCONTRADO | https://www.maxongroup.com/maxon/view/product/motor/dcmotor/DCX/DCX22/DCX22L01GBSL450 · https://www.maxongroup.com/maxon/view/product/gear/planetary/GPX/GPX22/GPX22-1-Stufig-A/GPX22AAKLSL03D9CPLW |
| B2-3 (BLDC, hay que pedirla al fabricante) | SLW BLDC 28 mm con devanado para 7,4 V y caja de 1 etapa | SLW (cotizar) | NO ENCONTRADO | NO ENCONTRADO (la versión publicada no llega) | NO ENCONTRADO | NO ENCONTRADO | NO ENCONTRADO | Ø28; caja de 23,2 mm | NO ENCONTRADO | NO ENCONTRADO | NO ENCONTRADO | NO ENCONTRADO | https://slwmotor.com/product/28mm-diameter-brushless-dc-motor-with-planetary-gearbox/ |

### Cómo salen las estimaciones
- Uso la recta de un motor DC: velocidad y torque de bloqueo proporcionales al voltaje, \(n = n_0\,(1 - T/T_{bloqueo})\) e \(I = I_0 + T/K_t\). Para el RS-380PH-4045, \(K_t = 77{,}5 / (18 - 0{,}56) \approx 4{,}44\) mN·m/A.
- La eficiencia de la caja planetaria de 1 etapa la supuse en 0,85 (la ficha de la caja no la publica) y la de maxon en 0,90.
- B2-1 a 7,4 V con 5:1: el motor da 0,06 / (5 × 0,85) = 14,1 mN·m a ≈13.140 rpm, o sea ≈2630 rpm a la salida, con ≈3,7 A.
- Pasado por el engranaje de 2,75:1, a la cuchilla llegan ≈955 rpm y 0,06 × 2,75 ≈ 0,165 N·m (sin contar la eficiencia del engranaje), igual al techo del torque de corte estimado (0,055–0,165 N·m). En bloqueo llegarían ≈1,1 N·m a la cuchilla.
- Con la batería baja (6,0 V), B2-1 cae a ≈2045 rpm, por debajo de 2500. Si eso importa, la 4:1 se mantiene en rango (2410–3660 rpm entre 6 y 8,4 V) pero consume ≈4,5 A.

### Driver
- **B2-1 y B2-2 (con escobillas):** basta un puente H o un MOSFET con PWM de ≥5 A continuos que aguante el pico de bloqueo (~22 A), o un driver con limitador de corriente. Didácticas tenía una "Tarjeta driver para motor DC 15A DRV-36V-15A" a $57.596, pero la página es antigua y hay que confirmar si sigue y qué medidas tiene. https://www.didacticaselectronicas.com/index.php/view/category/virtuemart_category_id/344
- **B2-3 (BLDC):** la página de SLW no dice qué driver usa ni si viene incluido (NO ENCONTRADO). Los BLDC de 28 mm con driver interno que revisé (Transmotec, Mechtex, Kegu) no llegan al torque pedido.

### Recomendación
- **Para el prototipo, B2-1:** el RS-380PH-4045 es el único con ficha publicada que llega a 2500–3500 rpm con 0,06 N·m sin pasar de 4 A, y cumple el diámetro (27,7 mm de cuerpo). Lo que no está confirmado: el largo total (≈60,7 mm con la caja de SLW, 0,7 mm más de lo pedido), el peso de la caja (para no pasar de 120 g la caja tendría que pesar ≤40 g) y el eje de salida de la caja.
- **Si se compra ya en AliExpress, B2-1b (4:1):** es la caja que se puede pedir hoy. Consume ≈4,5 A, por encima del límite.
- B2-2 (maxon) sirve como referencia de calidad y precio: ≈€314 sin IVA ni envío, pesa 140 g y queda justo de rpm a 7,4 V.

### Pendiente para Nick
- Pedir a SLW (sin compra) cotización de la caja de 28 mm de 1 etapa 5:1 para un motor 380 y preguntar si tienen el BLDC de 28 mm en 3:1 o 2,5:1 para 7,4–12 V. Texto sugerido: "Hello, I need a quote for 1–2 units: (1) 28 mm 1-stage planetary gearbox, 5:1 (or 4:1), input for a Mabuchi RS-380 motor (2.3 mm shaft); please send length, weight, output shaft (diameter, D-flat, length), mounting holes, rated torque, efficiency and a drawing/STEP. (2) Your 28 mm BLDC planetary motor with a 3:1 or 2.5:1 ratio and a winding for 7.4–12 V: no-load and rated speed, rated and stall torque, currents, which driver it needs, and price with shipping to Colombia."
- Confirmar en el plano del RS-380PH-4045 la cantidad de agujeros M2,6 y su círculo antes de diseñar el adaptador.
- Preguntar por WhatsApp a BigTronica si el "Motor DC 6-9V con piñón" es un 380 y de qué modelo.

# CONTEXTO — Detector de partículas DIY de CERN

Actualizado: 2026-11-06 20:30 (Bogotá). Lee solo esto para arrancar. El historial completo está en HANDOVER.md y solo se abre si Nick pregunta por algo del pasado.

## En una frase
Nick está armando en el laboratorio de Electrónica de la EIA el detector DIY de CERN S'Cool LAB (diseño oficial v1.2). Ya tiene los planos y los componentes de la variante alfa (TLE2072ACP + BPX61), y le falta montarla y probarla.

## Tu siguiente tarea
Ayudar a montar la variante alfa en protoboard y probarla, en este orden: medir DC → pulso de prueba en pin 1 → pin 7 → SALIDA. Si algo falla, pedir foto del osciloscopio y los voltajes DC.

## Hechos clave (exactos)
- Fuentes: artículo https://physicsopenlab.org/2020/06/15/cern-diy-particle-detector/ · diseño https://github.com/ozel/DIY_particle_detector (hardware/V1.2, CERN OHL v1.2) · paper doi 10.3390/s19194264.
- Variante alfa (la que se arma), con valores iguales a la esquemática oficial:
  - D1 = BPX61 sin vidrio; cátodo al pin 2, ánodo a GND.
  - U1 = TLE2072ACP, DIP-8: **pin 8 = +9 V, pin 4 = GND**. Etapa 1 = pines 1 (out), 2 (−), 3 (+). Etapa 2 = pines 7 (out), 6 (−), 5 (+).
  - R1 = 4,7 kΩ (+9 V → pin 3), R2 = 15 kΩ (pin 3 → GND), C3 = 100 nF (pin 3 → GND). Pin 3 ≈ 6,85 V, y el diodo queda en inverso a ≈6,9 V.
  - Cf = C1 + C2 en serie = 10 pF + 10 pF = 5 pF, entre pin 2 y pin 1. R3 = 40 MΩ en paralelo (τ = 200 µs). Si no hay de 40 MΩ, 4 × 10 MΩ en serie.
  - C4 = 470 nF (pin 1 → R4), R4 = 4,7 kΩ (→ pin 6), R5 = 1 MΩ y C6 = 3,3 nF entre pin 6 y pin 7. Ganancia ≈ −213.
  - R6 = R7 = 10 kΩ, divisor +9 V/GND → pin 5 = 4,5 V. C7 = 100 nF a GND.
  - Salida: pin 7 → R8 = 10 kΩ → nodo con C9 = 6,8 nF a GND → C10 = 100 nF → SALIDA, con R9 = 2,2 kΩ a GND.
  - C5 = 100 nF entre pin 8 y pin 4, pegado al chip. C8 = 47 µF electrolítico en la entrada de alimentación.
- Variante electrones (plano aparte, con TL074CN en DIP-14: pin 4 = +9 V, pin 11 = GND; amplificadores C y D como seguidores a 4,5 V). Lleva 4 × BPW34, R3 = 10 MΩ, R4 = 1 kΩ, R5 = 100 kΩ, C4 = 100 nF, C6 = 10 pF, R8 = puente y sin C9.
- Señales esperadas (estimadas):
  - Alfa de 5,5 MeV → ≈1,5 millones de pares → 0,24 pC → ≈49 mV en el pin 1.
  - En SALIDA, pulsos negativos de 50–100 mV (artículo).
  - Pulso de prueba: Q = Cprueba × ΔV (1 pF × 100 mV = 100 fC).
- Voltajes DC esperados con 9,0 V: pin 3 ≈ 6,9 V, pin 1 ≈ 6,9 V, pin 5 ≈ 4,5 V, pin 7 ≈ 4,5 V.
- Instrumentos de la EIA:
  - Fuente BK Precision 1672: salida MASTER a 9,0 V con límite de ≈50 mA; − unido al GND verde; perillas en modo independiente.
  - Generador BK 4045B: cuadrada de 100 Hz.
  - Osciloscopio GW Instek GDS-1072A: puntas en ×10 con el menú en 10X; mínimo 20 mV/div; CH2 en acople AC sobre pines 1 y 7.

## Decisiones vigentes (no reabrir)
- Se sigue el diseño oficial CERN v1.2 porque ya está probado.
- Sensor BPX61 (no hay BPW34 en Medellín). Los LED y receptores IR del laboratorio no sirven.
- Chip TLE2072ACP para la variante alfa. El TL074CN queda para electrones o como comparador.
- La electrónica se prueba primero con pulso de prueba (Cprueba de 1–2 pF desde el generador), antes del sensor.
- Los planos nuevos van siempre en archivo aparte; nunca se tocan los existentes (pedido de Nick).
- Una sola tierra para fuente, protoboard, osciloscopio, generador y Arduino.
- El contador con Arduino usa un comparador y entra por D2, no por el ADC.

## Restricciones
- Nada está probado en hardware: decirlo siempre.
- El BPX61 sin vidrio es sensible a la luz, así que todo va en caja metálica cerrada y oscura.
- R3 de 40 MΩ: placa limpia, sin flux.
- Con 9 V hay poca holgura: no alimentar por debajo de 9 V (una batería gastada de ≈7,5 V hace fallar el circuito).
- La fuente radiactiva solo con autorización del profesor.

## Pendientes abiertos
- [ ] Medir los voltajes DC de los pines 1, 3, 5 y 7 — Nick
- [ ] Ver el pulso de prueba en pin 7 y SALIDA (base de tiempo ≈500 µs/div en alfa) — Nick
- [ ] Quitar el vidrio del BPX61 e identificar el cátodo con el multímetro — Nick
- [ ] Conseguir R3 = 40 MΩ (o 4 × 10 MΩ) — Nick
- [ ] Compilar contador_particulas.ino en el Arduino IDE — Nick
- [ ] Confirmar la fuente radiactiva con el profesor — Nick

## Criterio de cierre
- [ ] Pulso de prueba visible en SALIDA con la forma esperada
- [ ] BPX61 montado en caja oscura y pulsos de alfa reales vistos (con fuente autorizada)
- [ ] Planos finales y fotos del montaje guardados (computador o Drive)

## Preguntas abiertas
- ¿Se mantiene el contador con Arduino ahora que el TLE2072 no tiene amplificadores sobrantes? (Opción: TL074 aparte solo como comparador.)
- ¿Es entrega de Electrónica 2 o proyecto propio?
- ¿Con qué se van a leer los pulsos al final: osciloscopio, jack del celular o Arduino?

## Cómo quiere trabajar Nick aquí
- Español simple, con ejemplos. Pidió tres veces explicaciones más sencillas: explicar qué hace cada cosa antes de dar números.
- Respuestas cortas y prácticas, porque está en el laboratorio mandando fotos de los equipos.
- No modificar los planos que ya tiene.

## Errores que no repetir
- No recomendar punta ×10 junto con escalas de 5 mV/div: con ×10 el mínimo es 20 mV/div. Para el pin 1, usar punta ×1; si no, medir en el pin 7.
- Confirmar siempre la referencia exacta del chip (TLE2072 ≠ TLE2027).
- En el TLE2072 el pin 4 es GND; en el TL074 el pin 4 es +9 V. Avisar si se reutiliza la protoboard.

## Mapa de archivos (abrir solo cuando la tarea lo pida)
| Archivo | Qué tiene | Abrir cuando |
|---|---|---|
| archivos/planos/esquematica_tle2072_alfa.py | Plano alfa (schemdraw, genera PNG/PDF/SVG) | Haya que regenerar o hacer otra versión del plano alfa |
| archivos/planos/esquematica_tl074.py | Plano electrones con TL074CN | Pregunten por la variante de electrones |
| archivos/planos/esquematica_arduino.py | Plano del contador con comparador | Trabajen el contador |
| archivos/arduino/contador_particulas.ino | Sketch del contador (D2, CSV por serial a 9600) | Trabajen el contador |
| archivos/calculos/capacitores_serie.py | Calculadora de capacitores en serie | Pidan calcular capacitancias |
| HANDOVER.md | Trazabilidad e historial de decisiones | Nick pregunte cuándo o por qué cambió algo |

## Glosario
- Cf: condensador de realimentación del preamplificador (5 pF).
- Pulso de prueba / Cprueba: carga inyectada desde el generador por un condensador pequeño.
- REF: nodo de 4,5 V (R6/R7).
- Variante alfa / electrones: las dos configuraciones del diseño de CERN.

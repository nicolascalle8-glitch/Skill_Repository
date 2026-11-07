# HANDOVER — Detector de partículas DIY de CERN

Última actualización: 2026-11-06 20:30 (Bogotá)
Chat de origen: chat del proyecto "Skills para Fisica" en claude.ai, "Necesito desarrollar este proyecto… esquemática" (29 oct 2026)
Auditoría más reciente: 🟡 73/100

---

## 1. Estado actual

### Qué es el proyecto
Armar el detector de partículas DIY de CERN S'Cool LAB (fotodiodos PIN + preamplificador de carga + amplificador), basado en el artículo de PhysicsOpenLab y en el diseño oficial v1.2 de GitHub (ozel/DIY_particle_detector). Se monta en el laboratorio de Electrónica de la EIA. Relacionado con Electrónica 2 (Arduino) de Valeria.

### Dónde vamos
- Hecho: esquemáticas de 3 versiones (TL074 + 4 BPW34 electrones; TLE2072 + BPX61 alfa; contador con Arduino aparte), sketch del contador, revisión de todos los valores con la hoja de datos de TI, explicación del circuito por partes, calculadora de capacitores en serie.
- En curso: montaje en protoboard y prueba con generador + osciloscopio. Se vio la cuadrada del generador en CH1; todavía no se confirmó el pulso en el pin 7.
- Próximo paso: montar la variante alfa con TLE2072ACP + BPX61 y probarla con el pulso de prueba (1 pF, cuadrada 100 mV, 100 Hz).

### Decisiones vigentes
| Fecha | Decisión | Por qué | Quién la tomó |
|---|---|---|---|
| 2026-10-29 | Seguir el diseño oficial CERN v1.2 | Valores probados y publicados (paper Sensors 2019) | acordado |
| 2026-10-29 | No usar los LED IR que había en el laboratorio como sensor | LED emisor no sirve; receptor IR de 5 mm: chip pequeño y epoxi frena alfas/betas | acordado |
| 2026-10-29 | Probar la electrónica primero con pulso de prueba (Cprueba 1–2 pF desde el generador) | Permite validar el circuito sin sensor ni fuente radiactiva | acordado |
| 2026-10-29 | Planos nuevos siempre en archivo aparte, sin tocar los anteriores | Pedido explícito de Nick ("sin tocarme los planos que ya tengo") | Nick |
| 2026-10-29 | Alimentar con la fuente de banco BK Precision 1672 (salida MASTER, 9,0 V, límite ≈50 mA), una sola tierra | Disponible en el laboratorio; − unido al GND verde | acordado |
| 2026-10-29 | Usar el TLE2072ACP (chip original) con el BPX61 → variante alfa | Nick consiguió ambos | Nick |
| 2026-10-29 | El contador con Arduino usa un comparador (amp. sobrante del TL074) y no lee el ADC | El ADC del Uno es muy lento para medir altura de pulsos | acordado |

### Hitos
| Fecha | Hito | Estado |
|---|---|---|
| 2026-10-29 | Esquemática oficial v1.2 extraída del repo de CERN | ✅ hecho |
| 2026-10-29 | Plano TL074CN (electrones, 4 BPW34) | ✅ hecho |
| 2026-10-29 | Plano contador Arduino + sketch | ✅ hecho (sketch sin compilar) |
| 2026-10-29 | Revisión de valores de diseño contra hoja de datos TI | ✅ hecho |
| 2026-10-29 | Plano TLE2072ACP (alfa, BPX61) | ✅ hecho |
| 2026-10-29 | Instrumentos configurados (fuente, generador, osciloscopio) | ⏳ en curso |
| — | Pulso de prueba visto en pin 7 y SALIDA | 🔜 próximo |
| — | BPX61 sin vidrio montado en caja metálica oscura | 🔜 |
| — | Partículas reales vistas (fuente autorizada) | 🔜 |

### Pendientes
| Pendiente | Responsable | Fecha límite | Bloqueado por |
|---|---|---|---|
| Medir DC: pin 3 ≈6,9 V, pin 1 ≈6,9 V, pin 5 ≈4,5 V, pin 7 ≈4,5 V | Nick | — | montaje |
| Ver pulso de prueba en pin 7 / SALIDA | Nick | — | medición DC |
| Quitar el vidrio del BPX61 e identificar cátodo con multímetro | Nick | — | — |
| Conseguir R3 = 40 MΩ (o 4 × 10 MΩ en serie) | Nick | — | — |
| Compilar contador_particulas.ino en el Arduino IDE | Nick | — | — |
| Confirmar con el profesor qué fuente radiactiva se puede usar (Am-241 típico) | Nick | — | — |
| Decidir cómo leer pulsos: osciloscopio, jack del celular o Arduino | Nick | — | — |

### Preguntas abiertas
- ¿Se mantiene el contador con Arduino ahora que se usa el TLE2072 (que no tiene amplificadores sobrantes)? Opción: TL074 aparte solo como comparador.
- ¿Es entrega de Electrónica 2 o proyecto propio? (cambia el alcance).

### No volver a discutir
- BPW34 no se consigue en tiendas de Medellín: ya se pasó al BPX61.
- Los LED IR / receptores IR del laboratorio no sirven como sensor.
- HC-SR04 no tiene nada que ver: el "micrófono" del diseño es la entrada de micrófono del celular/PC.
- TL074CN funciona con 9 V (4,5–40 V en DIP-14, hoja de datos TI). Valores de diseño ya revisados: no hay que cambiar nada.
- No hace falta adaptador SMD→DIP: TL074CN y TLE2072ACP son DIP.
- TLE2027 ≠ TLE2072: el 2027 (simple, bipolar) no sirve; el que se tiene es TLE2072ACP.

### Archivos, links y entregables
| Qué | Dónde | Notas |
|---|---|---|
| Artículo | https://physicsopenlab.org/2020/06/15/cern-diy-particle-detector/ | fuente original |
| Diseño oficial v1.2 (KiCad, BOM, PDF) | https://github.com/ozel/DIY_particle_detector (hardware/V1.2) | CERN OHL v1.2 |
| Paper de referencia | https://doi.org/10.3390/s19194264 | calibración alfa |
| Script plano TL074 | archivos/planos/esquematica_tl074.py | genera PNG/PDF/SVG |
| Script plano alfa TLE2072 | archivos/planos/esquematica_tle2072_alfa.py | genera PNG/PDF/SVG |
| Script plano contador Arduino | archivos/planos/esquematica_arduino.py | genera PNG/PDF |
| Sketch contador | archivos/arduino/contador_particulas.ino | D2/INT0, CSV por serial 9600 |
| Calculadora capacitores en serie | archivos/calculos/capacitores_serie.py | probado: 10 pF + 10 pF = 5 pF |
| PNG/PDF de los planos | entregados en el chat del 29 oct; se regeneran corriendo los scripts (requiere `pip install schemdraw`) | no van al repo (archivos pesados) |

### Preferencias de trabajo para este proyecto
- Español simple. Explicar con ejemplos y sin terminología pesada: Nick pidió 3 veces explicaciones más simples (batería, polarización, preamplificador).
- No tocar planos existentes: cada cambio grande va en archivo nuevo.
- Decir siempre que nada está probado en hardware.

---

## 2. Mensaje de arranque para el chat nuevo

> Vengo de un chat anterior sobre el detector de partículas DIY de CERN. Para arrancar lee **solo** `proyectos/detector-particulas-cern/CONTEXTO.md` del repo `nicolascalle8-glitch/Skill_Repository` (o el contexto que pego abajo). No releas el chat viejo ni el HANDOVER completo; abre el HANDOVER o los `archivos/` solo si la tarea lo pide o yo pregunto por algo del pasado. Lo siguiente que necesito: ayudarme a montar y probar la variante alfa (TLE2072ACP + BPX61). No reabras las decisiones vigentes.

---

## 3. Historial de actualizaciones

### 2026-11-06 20:30 — 🟡 73/100
- **Nuevo:** primer handover del proyecto. Todo lo del chat del 29 oct (10:15–17:48): planos TL074, Arduino y TLE2072 alfa; sketch; revisión de valores; explicación del circuito; calculadora de capacitores.
- **Cerrado:** búsqueda de sensor (BPX61) y de chip (TLE2072ACP).
- **Cambiado:** sensor BPW34 → BPX61 (no se conseguía BPW34); chip TL074CN → TLE2072ACP para la versión alfa (el TL074 sigue sirviendo para electrones o como comparador).
- **Error corregido en el chat:** se recomendó punta ×10 y a la vez 5 mV/div; con ×10 el mínimo es 20 mV/div. Solución: medir en pin 7 o usar punta ×1 en pin 1.

# CONTEXTO — Presentación Engranajes Helicoidales (Diseño Mecánico, EIA)

Actualizado: 2026-10-24 14:45 (Bogotá). Lee solo esto para arrancar. El historial completo está en HANDOVER.md y solo se abre si Nick pregunta por algo del pasado.

## En una frase
Exposición de Nick (60–75 min + preguntas, la revisa el profesor, entra al examen final) sobre engranajes helicoidales. Presentación, Excel y kit de sustentación están listos con el ejercicio de Mott 10-2. Falta alinear el artículo y limpiar la carpeta antes de subir los entregables.

## Tu siguiente tarea
Preguntarle a Nick si ya fue la sustentación (estaba para el 2026-10-23) y qué dijo el profesor. Después, si él lo confirma: alinear el artículo de Google Docs con el ejercicio final (Mott 10-2, Casos A y B) y mover lo viejo de la carpeta de entregables a una subcarpeta `anterior/`.

## Hechos clave (exactos)
- Entregables: presentación + documento tipo artículo con ejercicio resuelto, subidos a la carpeta compartida del curso. Diapositivas y artículo en inglés; la parte oral en español.
- Ejercicio único: Mott 4ª ed. Problema modelo 10-2 (pp. 461–462) = Mott 6e Ejemplo 10-3. Fresadora, motor eléctrico 65 hp a 3450 rpm, salida ≈ 1100 rpm, choque moderado, caja comercial cerrada.
- Decisiones del libro: Pnd 12, φn 20°, ψ 15°, NP 24, NG 75 (nG 1104 rpm), F 2.25 in, Qv 8 (= Av 9).
- Geometría: Pd 11.59, φt 20.65°, DP 2.071 in, DG 6.471 in, C 4.271 in, px 1.012 in, Fmin 2.02 in, F/DP 1.09.
- Fuerzas: vt 1,870 ft/min, Wt 1,147 lb, Wx 307 lb, Wr 432 lb, WN 1,264 lb, T 1,187 lb·in.
- Factores: Ko 1.5, Ks 1, KB 1, Cpf 0.099, Cma 0.162, Km 1.26, Kv 1.35, JP 0.48, JG ≈ 0.53 (Excel 0.526), I 0.202, Cp 2300. ΠK = 2.555.
- Esfuerzos: stP 31,400 psi (Excel 31,462), stG ≈ 28,700, sc 128,200 psi (Excel 128,369).
- Caso A (10⁷ ciclos, R 99 %, YN = ZN = KR = 1): ≈ 250 HB flexión, ≈ 310 HB picadura → AISI 5150 OQT 1000, 321 HB (Apéndice 3), templado completo.
- Caso B (R 99.9 % → KR 1.25; 10,000 h → Nc 2.07·10⁹, ZN 0.89, YN 0.93): sac requerido ≈ 180,000 psi (≈ 470 HB, más de 400) → cementar los dos: AISI 4320 SOQT 450, HRC 59, núcleo 415 HB (Tabla 9-3 grado 1, Apéndice 5).
- Mensaje central: misma geometría, mismos esfuerzos; la confiabilidad y la vida cambian el material. En los dos casos manda la picadura.
- Ecuaciones: st = Wt·Pd/(F·J)·Ko·Ks·Km·KB·Kv; sc = Cp·√[Wt·Ko·Ks·Km·Kv/(F·DP·I)]; sat = 77.3·HB + 12,800; sac = 322·HB + 29,100; Kv (Qv) con B = 0.25(12−Qv)^(2/3), A = 50 + 56(1−B), Kv = [(A+√vt)/A]^B.

## Decisiones vigentes (no reabrir)
- Un solo ejercicio — lo pidió Nick.
- Ejercicio de Mott con números del libro; el del video de YouTube quedó descartado — "asume demasiadas cosas".
- Se muestra en Caso A y Caso B — así lo resuelve el libro.
- Sin "Prueba 2" (Pnd 8) en la presentación; solo aparece como pregunta de respaldo en el kit (Pnd 8, F 3.25 in → sc 74 ksi, ≈ 235 HB).
- La diapositiva "what" la borró Nick; no volver a ponerla.
- Presentación en Claude Slides, unidades inglesas.
- El artículo se corrige sobre el Google Doc existente, no se hace uno nuevo.

## Restricciones
- Nunca escribir contraseñas: si hace falta sesión de Google, Nick entra él mismo en el navegador.
- No hacer OCR completo del PDF de Mott; solo páginas puntuales.
- Pedir permiso antes de mover o borrar archivos en la carpeta de Nick.

## Pendientes abiertos
- [ ] Confirmar si fue la sustentación y qué dijo el profesor — Nick.
- [ ] Alinear el artículo de Google Docs con Mott 10-2 (Casos A y B) — Claude, si Nick confirma — antes de subir.
- [ ] Volver a exportar la presentación a PDF: el "Helical Gears — Mechanical Design.pdf" de la carpeta es del 22 oct y tiene el ejercicio del video — Nick.
- [ ] Mover a `anterior/`: Guia_Tablero_Engranajes_Helicoidales.pdf, ejercicio_helicoidal.py, Helical Gears-Design-Fixed.xlsx, Helical_Gears_Mott_Presentation_EN.html, Helical_Gears_Presentation_Outline_and_Script.md, Helical_Gears_Technical_Article_EN.md — con aprobación de Nick.
- [ ] Subir entregables a la carpeta compartida del curso — Nick.

## Preguntas abiertas
- ¿El artículo final usa solo Mott 10-2 o deja también el Problema modelo 10-1 y el ejemplo de 11 hp de la clase?
- ¿Se programa algo más en Python? (Nick lo mencionó al inicio como opción.)

## Cómo quiere trabajar Nick aquí
- Español simple y directo en todo lo que él presenta como suyo (notas de voz, kit, comentarios). Nada muy pulido ni muy técnico.
- Diapositivas y artículo en inglés.
- Cada número con su fuente (figura, tabla o página del libro).
- Respuestas cortas: qué cambió y dónde quedó.

## Errores que no repetir
- No proponer ejercicios con datos supuestos; usar los del libro.
- Al cambiar el ejercicio, buscar restos viejos en todas las diapositivas, notas y el kit (quedó una diapositiva anunciando la Prueba 2).
- Corrección de J: depende del compañero. El piñón engrana con 75 dientes y no se corrige; la rueda engrana con 24 y sí.
- Si cambia ψ, cambian Pd, DP, vt y Kv (poco); no decir que Kv no cambia.
- Antes de entregar archivos, copiar la versión nueva a outputs; una vez se subió una copia vieja.
- La Guía Maestra de Gemini explica mal el error del Excel del profesor y usa celdas que no existen en el original.

## Datos que te pueden preguntar
- Error del Excel del profesor ("Helical Gears-Design.xlsx"): G40:G41 multiplican por la celda vacía G17, por eso sc sale 0. Se arregla quitando *G17.
- Excel vs libro en el Caso B: la hoja lee ZN 0.88 → 182 ksi y 476 HB; el libro 0.89 → 180 ksi. La decisión es la misma.
- Example #2 de la clase: Kv = 1.08 es con Qv 11 (escala vieja). Con Av 11 (6e) Kv = 1.42 y st ≈ 2,720 psi en vez de ≈ 2,070.

## Mapa de archivos (abrir solo cuando la tarea lo pida)
| Archivo | Qué tiene | Abrir cuando |
|---|---|---|
| Presentación https://claude.ai/artifact/MWUPNTufCr8rGPL3f8T6td | 28 diapositivas; ejercicio en la 18–24 | Cambiar diapositivas (leerla antes con Artifact read) |
| Artículo https://docs.google.com/document/d/1tQkRlo_1VN9JFjm_mw9rZXc18gBQMVAGwQqOzFAQO0Q | Artículo en inglés con ejemplos anteriores | Alinear el artículo |
| Carpeta del curso https://drive.google.com/drive/folders/1pi2Ol_GlQl70H1oVSDyNX0x68ZE4xR0R | Donde se suben los entregables | Subir |
| ~/Documents/Gemini/Helical_Gears_Deliverables/Helical_Gears_Calculator.xlsx | Hoja "Design 10-3": col. C = Caso B, col. D = Caso A | Recalcular o mostrar Excel |
| …/Kit_Sustentacion_Engranajes_Helicoidales.pdf | 14 pág.: símbolos, Tablero 0, 4 tableros, gráficas, números, ejemplos, 40 preguntas | Preparar preguntas o tablero |
| …/helical.py | Verificación independiente en Python | Verificar números |
| …/Guia_Maestra_Mott_Engranajes_Helicoidales.html | Guía de Gemini (fuente del kit) | Solo como referencia |
| ~/Documents/Gemini/412310576-Diseno-de-Elementos-de-Maquinas-Robert-l-Mott-4-PDF.pdf | Libro Mott 4ª ed. | Confirmar un dato del libro |
| HANDOVER.md | Trazabilidad e historial de decisiones | Nick pregunte cuándo o por qué cambió algo |

La carpeta local solo se alcanza si el chat está vinculado al computador de Nick.

## Glosario
- Caso A / Caso B: el mismo ejercicio con admisibles básicos (A) y con R 99.9 % + 10,000 h (B).
- Qv / Av: calidad del engranaje. Qv (Mott 4ª ed.): más alto = mejor. Av (Mott 6e): más bajo = mejor. Av = 17 − Qv.
- Kit: el PDF de preparación para la sustentación.
- Tablero 0–4: las páginas del kit para copiar en el tablero.

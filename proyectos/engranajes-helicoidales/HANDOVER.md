# HANDOVER — Presentación Engranajes Helicoidales (Diseño Mecánico, EIA)

Última actualización: 2026-10-24 14:45 (Bogotá)
Chat de origen: chat "Engranajes helicoidales" en claude.ai (22–24 oct 2026)
Auditoría más reciente: 🔴 60/100 (rojo por regla de corte: chat muy largo, el inicio ya solo existe como resumen)

---

## 1. Estado actual

### Qué es el proyecto
Exposición de Nick sobre engranajes helicoidales para Diseño Mecánico (Universidad EIA). Dura 60–75 min + preguntas, la revisa el profesor y el tema entra al examen final. Entregables: presentación + documento tipo artículo con un ejercicio resuelto, subidos a la carpeta compartida. Diapositivas y artículo en inglés; la parte oral puede ser en español.

### Dónde vamos
- Hecho: presentación (28 diapositivas), Excel, kit de sustentación (14 páginas), Python de verificación, artículo de Google Docs corregido (versión con ejemplos anteriores).
- La sustentación estaba para el 23 oct 2026. No se sabe si ya se hizo ni qué dijo el profesor.
- Próximo paso concreto: alinear el artículo de Google Docs con el ejercicio final (Mott 10-2, Caso A y Caso B) y limpiar la carpeta de entregables (mover lo viejo a una subcarpeta "anterior").

### Decisiones vigentes
| Fecha | Decisión | Por qué | Quién la tomó |
|---|---|---|---|
| 2026-10-22 | Presentación hecha como Claude Slides (artifact), unidades inglesas (Mott) | Respuesta de Nick al inicio | Nick |
| 2026-10-22 | Helical.pdf = presentación de ejemplo del profesor (referencia de estilo/contenido) | Respuesta de Nick | Nick |
| 2026-10-22 | Corregir el artículo que ya estaba en Google Drive en vez de hacer uno nuevo | "Mejor corrige el que ya está hecho en Google Drive" | Nick |
| 2026-10-22 | Solo 1 ejercicio en la sustentación | "no tienen que ser 2 ejercicios, solo debe ser 1" | Nick |
| 2026-10-23 | El ejercicio es Mott 4ª ed. Problema modelo 10-2 (= Mott 6e Ejemplo 10-3, fresadora 65 hp) con números del libro. Se descartó el ejercicio del video de YouTube | "ese ejercicio del video asume demasiadas cosas" | Nick |
| 2026-10-23 | El ejercicio se muestra en dos casos: A (10⁷ ciclos, R 99 % → AISI 5150 OQT 1000, 321 HB) y B (R 99.9 %, 10,000 h → AISI 4320 SOQT 450 cementado, HRC 59) | Es como lo resuelve el libro; mismos esfuerzos, cambia el material | Claude propuso, Nick no objetó |
| 2026-10-23 | Se quitó la "Prueba 2" (Pnd = 8) de la presentación | Era una iteración de Claude, no del libro | Claude, aceptado en la práctica |
| 2026-10-23 | Kit actualizado con la Guía Maestra de Gemini, manteniendo las preguntas del final | Pedido de Nick | Nick |
| — | La diapositiva "what" fue borrada por Nick; no volver a ponerla | Edición de Nick en el editor | Nick |

### Hitos
| Fecha | Hito | Estado |
|---|---|---|
| 2026-10-22 | Presentación y Excel iniciales | ✅ |
| 2026-10-22 | Artículo de Google Docs corregido (números) | ✅ (pero no alineado con el ejercicio final) |
| 2026-10-22 | Guía de tablero PDF (dos ejercicios) | ✅ (ya no aplica) |
| 2026-10-22 | Kit con ejercicio del video | ✅ → reemplazado |
| 2026-10-23 | Presentación y kit cambiados al ejercicio de Mott | ✅ |
| 2026-10-23 | Kit con Guía Maestra (14 pág., 40 preguntas) | ✅ |
| 2026-10-23 | Sustentación | ❓ sin confirmar |
| 2026-10-24 | Auditoría: 4 errores corregidos (Kv al cambiar ψ, razonamiento de JG, diapositiva 9, HB negativo en helical.py) | ✅ |

### Pendientes
| Pendiente | Responsable | Fecha límite | Bloqueado por |
|---|---|---|---|
| Alinear el artículo de Google Docs con el ejercicio Mott 10-2 (Casos A y B) | Claude, si Nick lo pide | Antes de subir entregables | Nick debe confirmar |
| Volver a exportar la presentación a PDF ("Helical Gears — Mechanical Design.pdf" en la carpeta es del 22 oct, con el ejercicio del video) | Nick | Antes de subir | — |
| Mover a subcarpeta "anterior": Guia_Tablero PDF, ejercicio_helicoidal.py, Helical Gears-Design-Fixed.xlsx, archivos de Gemini (Mott_Presentation_EN.html, Outline_and_Script.md, Technical_Article_EN.md) | Claude o Nick | Antes de subir | Nick debe aprobar |
| Subir entregables a la carpeta compartida del curso | Nick | Según el curso | — |

### Preguntas abiertas
- ¿Ya fue la sustentación? ¿Qué comentó el profesor?
- ¿El artículo final debe usar solo el ejercicio de Mott 10-2 o dejar también los ejemplos 10-1 y el de 11 hp?
- ¿Se programa más en Python (lo mencionó Nick al inicio como posibilidad)?

### No volver a discutir
- Ejercicio del video de YouTube: descartado, asume demasiado.
- Hacer dos ejercicios: no, solo uno.
- Prueba 2 con Pnd = 8 en la presentación: quitada (solo aparece como pregunta de respaldo en el kit).
- Diferencia Excel vs libro: el Excel da 476 HB porque lee ZN = 0.88; el libro usa 0.89 y llega a 180,000 psi. Es lectura de gráfica, la decisión (cementar) es igual.
- Error del Excel del profesor: G40:G41 multiplican por la celda vacía G17, por eso sc sale 0. La explicación de Gemini (G40 y G27) no coincide con el archivo original.
- Kv = 1.08 del Example #2 del profesor corresponde a Qv 11 (escala vieja); con Av 11 (6e) da 1.42.
- No hacer OCR completo del PDF de Mott (Nick lo rechazó); solo páginas puntuales.

### Archivos, links y entregables
| Qué | Dónde | Notas |
|---|---|---|
| Presentación (Claude Slides) | https://claude.ai/artifact/MWUPNTufCr8rGPL3f8T6td | 28 diapositivas; ejercicio en 18–24 |
| Artículo (Google Docs) | https://docs.google.com/document/d/1tQkRlo_1VN9JFjm_mw9rZXc18gBQMVAGwQqOzFAQO0Q | Falta alinear con el ejercicio final |
| Carpeta compartida del curso | https://drive.google.com/drive/folders/1pi2Ol_GlQl70H1oVSDyNX0x68ZE4xR0R | Para subir entregables |
| NotebookLM | https://notebook.google.com/notebook/a830de7a-af0a-4966-9d47-462c07e7ad8d | Fuentes de Gemini/NotebookLM y el video |
| Carpeta local | ~/Documents/Gemini/Helical_Gears_Deliverables/ | Ahí está todo lo de abajo |
| Helical_Gears_Calculator.xlsx | carpeta local | Hoja "Design 10-3" = ejercicio (col. C = Caso B, col. D = Caso A) |
| Kit_Sustentacion_Engranajes_Helicoidales.pdf | carpeta local | 14 pág.: símbolos, Tablero 0, 4 tableros, gráficas, números, ejemplos de respaldo, 40 preguntas |
| helical.py | carpeta local | Verificación independiente del Excel |
| Guia_Maestra_Mott_Engranajes_Helicoidales.html | carpeta local | Hecha por Gemini; usada como fuente del kit |
| Handover en Google Drive | Google Doc "HANDOVER — Engranajes Helicoidales" (Mi unidad) https://docs.google.com/document/d/15CEf_HZiUipjBLmVnwQYpwVHQMX4jm6SfFfIvvNk5oY | Copia del 2026-10-24 |
| Libro Mott 4ª ed. PDF | ~/Documents/Gemini/ | Problema modelo 10-2 en pp. 461–462 |

### Números clave del ejercicio (Mott 10-2)
65 hp, 3450 rpm → 1104 rpm · Pnd 12, φn 20°, ψ 15°, NP 24, NG 75, F 2.25 in · Pd 11.59, φt 20.65°, DP 2.071 in · px 1.012 in · vt 1,870 ft/min · Wt 1,147 lb, Wx 307, Wr 432, WN 1,264 · Ko 1.5, Km 1.26, Kv 1.35 (Qv 8), JP 0.48, JG ≈ 0.53, I 0.202 · stP 31,400 psi, sc 128,200 psi · Caso A ≈ 310 HB → 5150 OQT 1000 · Caso B sac ≈ 180 ksi → 4320 SOQT 450 cementado.

### Preferencias de trabajo para este proyecto
- Español simple y directo en todo lo que Nick presenta como suyo (notas de voz, kit, comentarios). Nada muy pulido.
- Diapositivas y artículo en inglés.
- Números siempre del libro; decir de dónde sale cada uno.
- No escribir contraseñas: Nick inicia sesión él mismo cuando hace falta.

---

## 2. Mensaje de arranque para el chat nuevo

> Vengo de un chat anterior sobre mi presentación de engranajes helicoidales (Diseño Mecánico, EIA). Lee solo `proyectos/engranajes-helicoidales/CONTEXTO.md` del repo `nicolascalle8-glitch/Skill_Repository` (o el texto que pego abajo). No leas el HANDOVER ni el chat viejo salvo que te pregunte por algo del pasado. Lo siguiente que necesito: [TAREA]. No reabras lo que está en "Decisiones vigentes".

---

## 3. Historial de actualizaciones

### 2026-10-24 14:45 — 🔴 60/100
- **Nuevo:** se archiva en GitHub (`proyectos/engranajes-helicoidales/`) con CONTEXTO.md aparte; copia en Google Drive.
- **Cambiado:** el mensaje de arranque ahora apunta solo al CONTEXTO.md.

### 2026-10-24 14:30 — 🔴 60/100
- **Nuevo:** primer handover del proyecto (guardado en Google Drive y en la carpeta local).
- **Cerrado:** cambio al ejercicio de Mott; kit con Guía Maestra; 4 errores de la auditoría corregidos.
- **Cambiado:** ejercicio del video → Mott 10-2 (porque el video asumía demasiado).
- **Reemplazado / ya no aplica:** ~~Kit con ejercicio del video (10 hp, bomba)~~ → kit Mott; ~~Prueba 2 Pnd = 8 en la presentación~~ → quitada; ~~Guía de tablero con dos ejercicios~~ → un solo ejercicio.

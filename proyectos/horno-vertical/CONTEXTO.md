# CONTEXTO — Horno vertical

Actualizado: 2026-11-08 21:36 (Claude Opus 5.5)

## En una frase
Modelo 2D (r, z) del reactor vertical de pirólisis de residuo de café con cinética RAC + TGL, que se va a rehacer como motor limpio, calibrar con el horno real y usar desde una app (Streamlit) como "tuner": calibrar modelo → sintonizar PID → escoger receta.

## Dónde está todo
- Código: GitHub nicolascalle8-glitch/PyrolysisReactorCoffee, rama main = motor nuevo (unido con el PR #2) (motor/, parametros/base.toml, tests/). El modelo anterior se borró (historial git, commit c2acaae); su referencia está en tests/referencia/.
- En el Mac: 01_Horno_Vertical/modelos/PyrolysisReactorCoffee (clon con git, rama main) y modelos/barrido_motor.py (barrido en paralelo).
- Carpeta de trabajo: Mac de Nick, ~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/01_Horno_Vertical (datos/, modelos/, resultados/).
- Brief: doc del Project "MacBook's Power" → lineas/01-horno-vertical.md.

## Decisiones vigentes (aprobadas por Nick, 2026-11-08)
1. Orden: A motor nuevo (archivo de parámetros con fuente y etiqueta, verificado contra el actual) → B ensayo térmico + calibración térmica → C app Streamlit encima.
2. Numérica del motor: paso dividido — conducción implícita (Euler implícito, sistema disperso) + química integrada exacta por nodo.
3. Horno modelado como el real: masa térmica, resistencias P_max, PID → SSR con ventana de tiempo, pérdidas, intercambio horno-tubo, retardo de termopar.
4. App: Streamlit local. PID se sintoniza en Python dentro de la app; MATLAB/Simulink verifica y sirve para el micro.
5. Spec del motor aprobado (2026-11-08 19:53): PyrolysisReactorCoffee, rama motor-nuevo, docs/specs/2026-11-08-motor-nuevo-design.md. Datos del GIEM/FTIR no se suben (repo público).
6. legacy/ borrado y copia vieja del Mac reemplazada (aprobado 2026-11-08 21:17).
7. Composición base: celulosa 12.4 y lignina 23.9 % bs de Ballesteros 2014; hemicelulosa 35 y lípidos 15 siguen sin medir (aprobado 2026-11-08 21:17).
8. lecho.R_contacto_extra = 0.011 m²K/W (resistencia efectiva de legacy; se calibra en B) (aprobado 2026-11-08 21:17).

## Datos disponibles
- [Dato] GIEM 28ago2604: humedad 61.2 % bh; cenizas 2.31 % bs; pérdida por calcinación 650 °C 97.7 % bs; CO 49.4 % bs; N org 0.418 % bs; C/N 118.2.
- [Dato] FTIR (590–4000 cm⁻¹, %T): Café grano, Pirolizado 1-2, Pirolizado sedimento. Solo cualitativo.
- [Dato, literatura] Celulosa 12.4 y lignina 23.9 % bs (Ballesteros et al. 2014, Tabla 1).
- [Supuesto / Por validar] Hemicelulosa 35, lípidos 15 % bs; densidad 380 kg/m³; h_c = 90 W/m²K (incluye radiación); evaporación por Arrhenius.
- Falta: curvas de termopar, masas de productos, TGA.

## Pendientes
- Motor (A) HECHO 2026-11-08: 78 pruebas, caso base igual a legacy, ≈12× más rápido. Interfaz fija (cargar_parametros, simular, simular_lote, Resultado) → Cursor/Copilot ya puede hacer la app.
- Verificado en el Mac (2026-11-08): 78 pruebas pasan en macOS, caso base 1.4 s, prueba 7 en MATLAB 0.349 K (PASA).
- Nick: crear de nuevo el .venv del repo en el Mac; medir lípidos (Soxhlet) y densidad; pedir al GIEM confirmar N = 0.418 % bs.
- B: aviso de horno saturado y demás menores de la revisión (bitácora 20:54).
- Respuestas de Nick a la PREGUNTA del 2026-11-08 19:33.
- Plan del ensayo térmico (termopar pared + centro; corrida en vacío y con café).
- Manual Max-Therma MC-5438: tiempo de ciclo SSR y rangos PID.

## Cómo se trabaja (ahorro de tokens, 2026-11-08)
1. Un chat por subproyecto (A motor, B calibración, C app); la Línea 2 (IA local) siempre aparte.
2. Chat largo o que empieza a fallar → cerrar con `auditor-handover` y abrir otro que lea este CONTEXTO.
3. Al empezar, leer este CONTEXTO y las últimas 5 entradas de la bitácora; no todo.
4. CSV, resultados y logs se leen desde la carpeta del Mac; no se pegan en el chat.
5. Corridas pesadas en la Terminal de macOS; Claude prepara los scripts.
6. Reparto: investigación → Gemini (Deep Research) / Perplexity; pantallas de la app → Cursor/Copilot; física, numérica, revisión y verificación → Claude.

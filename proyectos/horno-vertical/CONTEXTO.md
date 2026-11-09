# CONTEXTO — Horno vertical

Actualizado: 2026-11-08 19:33 (Claude Opus 5.5)

## En una frase
Modelo 2D (r, z) del reactor vertical de pirólisis de residuo de café con cinética RAC + TGL, que se va a rehacer como motor limpio, calibrar con el horno real y usar desde una app (Streamlit) como "tuner": calibrar modelo → sintonizar PID → escoger receta.

## Dónde está todo
- Código original: GitHub nicolascalle8-glitch/PyrolysisReactorCoffee (simulador_interactivo.py = modelo vigente; docs/EVALUACION_CINETICAS.md).
- Carpeta de trabajo: Mac de Nick, ~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/01_Horno_Vertical (datos/, modelos/, resultados/).
- Brief: doc del Project "MacBook's Power" → lineas/01-horno-vertical.md.

## Decisiones vigentes (aprobadas por Nick, 2026-11-08)
1. Orden: A motor nuevo (archivo de parámetros con fuente y etiqueta, verificado contra el actual) → B ensayo térmico + calibración térmica → C app Streamlit encima.
2. Numérica del motor: paso dividido — conducción implícita (Euler implícito, sistema disperso) + química integrada exacta por nodo.
3. Horno modelado como el real: masa térmica, resistencias P_max, PID → SSR con ventana de tiempo, pérdidas, intercambio horno-tubo, retardo de termopar.
4. App: Streamlit local. PID se sintoniza en Python dentro de la app; MATLAB/Simulink verifica y sirve para el micro.

## Datos disponibles
- [Dato] GIEM 28ago2604: humedad 61.2 % bh; cenizas 2.31 % bs; pérdida por calcinación 650 °C 97.7 % bs; CO 49.4 % bs; N org 0.418 % bs; C/N 118.2.
- [Dato] FTIR (590–4000 cm⁻¹, %T): Café grano, Pirolizado 1-2, Pirolizado sedimento. Solo cualitativo.
- [Supuesto, sin fuente] Composición celulosa 12 / hemicelulosa 35 / lignina 28 / lípidos 15 % bs; h_comb = 90 W/m²K; evaporación por Arrhenius.
- Falta: curvas de termopar, masas de productos, TGA.

## Pendientes
- Spec del motor nuevo (Claude, en curso).
- Respuestas de Nick a la PREGUNTA del 2026-11-08 19:33.
- Plan del ensayo térmico (termopar pared + centro; corrida en vacío y con café).
- Manual Max-Therma MC-5438: tiempo de ciclo SSR y rangos PID.

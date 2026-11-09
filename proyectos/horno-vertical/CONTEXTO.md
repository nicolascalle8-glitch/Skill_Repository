# CONTEXTO — Horno vertical

Actualizado: 2026-11-08 21:55 (Bogotá, Claude Opus 5.5). Lee solo esto y las últimas 5 entradas de BITACORA.md para arrancar. El historial completo está en HANDOVER.md; ábrelo solo si Nick pregunta por algo del pasado.

## En una frase
Modelo 2D (r, z) del reactor vertical de pirólisis de residuo de café (práctica GIEM UdeA/EIA), con cinética RAC + TGL, para usarlo como "tuner" del horno real: calibrar el modelo → sintonizar el PID → escoger la receta. El motor (A) está terminado y en `main`; sigue la calibración (B), y la app (C) le toca a Cursor.

## Tu siguiente tarea
Subproyecto B: plan del ensayo térmico. Termopar en la pared del tubo y en el centro del lecho; una corrida en vacío y otra con café. Decir qué parámetros del motor se calibran con cada corrida (C_h, UA_p, h_c, ε, R_contacto_extra, k del lecho) y cómo se evita que h_c y k del lecho se confundan (riesgo de identificabilidad del spec §11).

## Hechos clave (exactos)
- Repo: github.com/nicolascalle8-glitch/PyrolysisReactorCoffee, rama `main` (commit ed907cf, PR #2). Público.
- Mac: `~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/01_Horno_Vertical/` con `datos/`, `modelos/PyrolysisReactorCoffee/` (clon con git y `.venv`), `modelos/barrido_motor.py` y `resultados/`.
- Interfaz pública (fija): `from motor import cargar_parametros, simular, simular_lote`. `Resultado` tiene:
  - `rendimientos`
  - `historia` (t, T_horno, T_set, T_pared, T_lecho_superficie, T_centro, T_termopar_control, masa_residual, u)
  - `mapas`, `balance_masa`, `balance_energia`, `confiable`, `supuestos`, `avisos`, `a_csv()`
  - Gráficas: `motor.graficas.graficar`. 0D tipo TGA: `motor.cinetica.tga.simular_0d`.
- Parámetros en `parametros/base.toml`, 58 claves con unidad, etiqueta, fuente y rango. Se cambian con `cargar_parametros(ruta, {"grupo.nombre": valor})`.
- Modo del horno: `horno.modo = "ideal"` (retardo τ = 200 s, como legacy) o `"fisico"` (C_h, UA_p, P_max = 2500 W, PID → SSR `promedio`/`onoff`).
- Valores de arranque del modo físico, todos [Por validar]: C_h = 20000 J/K, UA_p = 5 W/K, Kp = 0.02 1/K, Ki = 1e-4, Kd = 0, t_ciclo = 2 s, t_muestreo = 1 s. Con ellos el horno no alcanza 10 °C/min (P_max/C_h = 7.5 K/min).
- Termopar de control: cara externa del tubo, z = 0.10 m, τ = 10 s [Supuesto].
- Geometría base [Supuesto]: R_lecho 25 mm, acero 2.5 mm, L 0.20 m. Malla 14 + 4 nodos radiales, 20 axiales.
- Caso base (10 °C/min, 500 °C, 30 min, 8 % de humedad): biochar 24.22 / bio-oil 39.60 / gas 20.31 / agua 15.88 % de la carga. Tarda 1.4 s en el M4.
- Barrido de 30 casos (T_final 400–600, rampa 5–20, humedad 8–15 %): biochar 20.3–25.8 %. La T final es lo que más pesa. La humedad solo diluye (en base seca el biochar no cambia). La rampa casi no pesa (< 0.5 pp), y eso es propiedad del régimen `lecho_fijo`: hay que contrastarlo con una corrida real. Archivo: `resultados/barrido_20261108_2148.csv`.
- Datos del GIEM (28ago2604) [Dato]: humedad 61.2 % bh, cenizas 2.31 % bs, pérdida por calcinación a 650 °C 97.7 % bs, CO 49.4 % bs, N 0.418 % bs, C/N 118.2.
- FTIR (Café grano, Pirolizado 1-2, Pirolizado sedimento): solo cualitativo.
- Composición en base seca:
  - celulosa 12.4 y lignina 23.9 % [Dato, Ballesteros et al. 2014, Tabla 1]
  - hemicelulosa 35 [Supuesto]
  - lípidos 15 [Por validar]
  - otros 11.39 [Calculado]
- Densidad aparente 380 kg/m³ [Por validar]; Guendouz 2023 da 387.
- h_c = 90 W/m²K incluye la radiación (ε = 0 en la base). R_contacto_extra = 0.011 m²K/W [Calculado].

## Decisiones vigentes (no reabrir)
1. Orden: A motor → B ensayo térmico y calibración → C app Streamlit.
2. Numérica: paso dividido, conducción implícita (solver de banda) + química exacta por nodo, dt adaptativo.
3. Horno modelado como el real (masa térmica, P_max, PID → SSR, pérdidas, intercambio horno–tubo, termopar con retardo).
4. App en Streamlit local. El PID se sintoniza en Python; MATLAB/Simulink verifica y sirve para el microcontrolador.
5. Spec del motor: docs/specs/2026-11-08-motor-nuevo-design.md. Los datos del GIEM y del FTIR no se suben (repo público).
6. legacy/ borrado (en git, commit c2acaae). La referencia de legacy está en tests/referencia/.
7. Composición de Ballesteros 2014 para celulosa y lignina. Para comparar contra legacy, usar COMPOSICION_LEGACY de tests/test_simulador.py.
8. R_contacto_extra = 0.011 m²K/W hasta calibrarlo en B.

## Restricciones
- En el Mac, trabajar solo dentro de `01_Horno_Vertical`. Nada de IA local en estos chats (eso es la Línea 2).
- La shell de Claude en el Mac es una VM Linux de 4 núcleos. Las corridas pesadas van en la Terminal de macOS con `modelos/PyrolysisReactorCoffee/.venv/bin/python`.
- Borrar, mover, unir a main o cambiar una decisión: solo con aprobación de Nick (PROPUESTA en la bitácora).
- Cada número con su fuente y su etiqueta. No inventar propiedades.

## Pendientes abiertos
- [ ] Plan del ensayo térmico — Claude (chat B)
- [ ] Manual del MC-5438: tiempo de ciclo del SSR, unidades y rangos del PID, autotune — Perplexity → Nick
- [ ] PREGUNTA del 2026-11-08 19:33: masas y temperaturas de "Pirolizado 1-2"; ¿"Café grano" es el residuo del GIEM? — Nick
- [ ] Medir lípidos (Soxhlet) y densidad a 8 % de humedad; confirmar N = 0.418 % con el GIEM — Nick
- [ ] Menores de la revisión del motor (lista en HANDOVER §3, notas para B), empezando por el aviso de horno saturado — Claude (B)
- [ ] App Streamlit — Cursor/Copilot (tarea en la bitácora, PREGUNTA 19:36)

## Criterio de cierre
- [x] A: motor en main, 8 pruebas del spec en verde (contenedor, macOS y MATLAB)
- [ ] B: modelo calibrado contra las dos corridas del ensayo (RMS de T_pared y T_centro con su criterio, a definir en el spec de B)
- [ ] C: app Streamlit que calibra, sintoniza el PID y compara recetas usando solo la interfaz pública
- [ ] Sintonía del PID verificada en MATLAB/Simulink antes de llevarla al horno

## Preguntas abiertas
- ¿Dónde está el termopar de control real del MC-5438?
- ¿Cuánto pesa la rampa en el horno real? El modelo dice que casi nada entre 5 y 20 °C/min.

## Cómo quiere trabajar Nick aquí
- Español simple. Respuestas cortas: qué cambió y dónde quedó.
- Comandos de Terminal completos, con el `cd` desde `~`, sin comentarios `#` (zsh los rompe) y con la ruta con espacios entre comillas: `~/Documents/"Documents - MacBook Pro de Nicolas"/Max_Power/...`
- Bitácora en GitHub y en Drive, con la misma entrada. Todo en GitHub al día al cerrar.
- CSV, resultados y logs se leen desde la carpeta del Mac; no se pegan en el chat.

## Cómo se trabaja (ahorro de tokens)
1. Un chat por subproyecto (A, B, C); la Línea 2 (IA local) siempre aparte.
2. Si el chat se alarga, cerrar con `auditor-handover`.
3. Reparto: investigación → Gemini/Perplexity; pantallas de la app → Cursor/Copilot; física, numérica, revisión y verificación → Claude.
4. La bitácora de Drive es grande (~90 mil caracteres): nunca leerla completa. Para insertar, sacar los índices de read_doc con un script y verificar solo lo nuevo.
5. Salidas largas (pytest, logs) a un archivo; leer solo el final.
6. Investigación de otra IA: revisarla, convertirla en ficha en archivos/investigaciones/ y no volver a leer el original.

## Errores que no repetir
- No pegar comentarios `#` en comandos para zsh.
- No sobrescribir ni borrar scripts de Nick sin aprobación explícita: el sistema lo bloquea (pasó con barrido_paralelo.py).
- Investigación de otras IAs: verificar fuente por fuente antes de usarla. Gemini tuvo 6 errores de atribución.
- En Google Docs, insertar párrafos con "\n" y no con saltos verticales: si no, la entrada queda toda como título.

## Mapa de archivos (abrir solo cuando la tarea lo pida)
| Archivo | Qué tiene | Abrir cuando |
|---|---|---|
| PyrolysisReactorCoffee/docs/specs/2026-11-08-motor-nuevo-design.md | Spec del motor (8 pruebas, riesgos) | Cambiar o extender el motor |
| PyrolysisReactorCoffee/parametros/base.toml | Parámetros con fuente | Calibrar o cambiar valores |
| PyrolysisReactorCoffee/README.md | Instalar, correr un caso, un lote, pruebas | Usar el motor |
| PyrolysisReactorCoffee/matlab/verificacion/README.md | Prueba 7 en MATLAB | Cambiar la conducción |
| archivos/investigaciones/datos-cafe-reactor-2026-11.md | Valores del café y del reactor verificados, por validar y descartados (de la investigación de Gemini) | Buscar una propiedad con fuente o calibrar en B |
| HANDOVER.md | Trazabilidad e historial de decisiones | Nick pregunte cuándo o por qué cambió algo |

## Glosario
- RAC + TGL: esquema cinético Ranzi–Anca-Couce 2017 + triglicéridos (Debiagi 2015).
- Modo ideal / físico: horno como retardo al setpoint / horno con balance de energía, PID y SSR.
- Prueba 2: comparación del motor contra legacy (caso base); prueba 7: verificación en MATLAB.
- bs / bh: base seca / base húmeda. pp: puntos porcentuales.

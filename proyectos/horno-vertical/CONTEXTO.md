# CONTEXTO — Horno vertical

Actualizado: 2026-11-09 08:50 (Bogotá, Claude Opus 5.5). Lee solo esto y las últimas 5 entradas de BITACORA.md para arrancar. El historial completo está en HANDOVER.md; ábrelo solo si Nick pregunta por algo del pasado.

## En una frase
Modelo 2D (r, z) del reactor vertical de pirólisis de residuo de café (práctica GIEM UdeA/EIA), con cinética RAC + TGL, para usarlo como "tuner" del horno real: calibrar el modelo → sintonizar el PID → escoger la receta. El motor (A) está terminado y en `main`. El plan de la calibración (B) está aprobado; faltan el script de ajuste y el ensayo real. La app (C) le toca a Cursor.

## Tu siguiente tarea
Subproyecto B en **una sola sesión de Claude Code en el Mac**, rama `ensayo-termico` de PyrolysisReactorCoffee (spec docs/specs/2026-11-08-ensayo-termico-design.md, commit 657a86b).
1. Spec: quitar "borrador" y anotar las aprobaciones 9–11.
2. Agregar `horno.modo = "medido"` (T_horno(t) leído de un CSV), con su prueba.
3. Script de ajuste en calibracion/. Corrida 1: modelo 0D del tubo (C_tubo·dT_pared/dt = h_ext·A·(T_horno − T_pared), mismo h_ext del motor). Corrida 2: motor en modo "medido". Mínimos cuadrados sobre T_pared y T_centro en los tramos del spec §4.
4. Probarlo con datos sintéticos (motor con valores conocidos + 1 K de ruido): recuperar C_h, UA_p, h_c, ε, k_virgen_0 y k_char_0, y reportar la correlación R_contacto–k.
5. Commit y push en ensayo-termico (no unir a main). Bitácora en GitHub y en Drive en una sola pasada.

## Hechos clave (exactos)
- Repo: github.com/nicolascalle8-glitch/PyrolysisReactorCoffee, rama `main` (commit ed907cf, PR #2). Público. Rama de B: `ensayo-termico` (657a86b).
- Mac: `~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/01_Horno_Vertical/` con `datos/`, `modelos/PyrolysisReactorCoffee/` (clon con git y `.venv`), `modelos/barrido_motor.py` y `resultados/`.
- Interfaz pública (fija): `from motor import cargar_parametros, simular, simular_lote`. `Resultado`: `rendimientos`, `historia` (t, T_horno, T_set, T_pared, T_lecho_superficie, T_centro, T_termopar_control, masa_residual, u), `mapas`, `balance_masa`, `balance_energia`, `confiable`, `supuestos`, `avisos`, `a_csv()`.
- Parámetros en `parametros/base.toml`, 58 claves con unidad, etiqueta, fuente y rango. Se cambian con `cargar_parametros(ruta, {"grupo.nombre": valor})`.
- Modo del horno: `horno.modo = "ideal"` (retardo τ = 200 s, como legacy) o `"fisico"` (C_h, UA_p, P_max = 2500 W, PID → SSR `promedio`/`onoff`).
- Valores de arranque del modo físico, todos [Por validar]: C_h = 20000 J/K, UA_p = 5 W/K, Kp = 0.02 1/K, Ki = 1e-4, Kd = 0, t_ciclo = 2 s, t_muestreo = 1 s. Con ellos el horno no alcanza 10 °C/min (P_max/C_h = 7.5 K/min).
- Termopar de control: cara externa del tubo, z = 0.10 m, τ = 10 s [Supuesto].
- Geometría base [Supuesto]: R_lecho 25 mm, acero 2.5 mm, L 0.20 m. Malla 14 + 4 nodos radiales, 20 axiales.
- Caso base, barrido de 30 casos, datos del GIEM, FTIR, composición y densidad: `archivos/hechos-cafe-y-barrido-2026-11.md` (abrir para cinética o recetas; no hacen falta para la calibración térmica).
- h_c = 90 W/m²K incluye la radiación (ε = 0 en la base). R_contacto_extra = 0.011 m²K/W [Calculado].
- Plan del ensayo: corrida 1 tubo vacío → C_h, UA_p, h_c, ε. Corrida 2 café (10 °C/min, 500 °C, 30 min, enfriamiento) con eso fijo → k_virgen_0 (25–200 °C), k_char_0 (enfriamiento), R_contacto (débil, ≈10 % de la resistencia del lecho). Aparte: τ de termopares y P_max real. Termopares a z = 0.10 m: pared externa, centro, aire del horno. CSV a 1 s en 01_Horno_Vertical/datos/ensayo_termico/ (t_s, T_horno_C, T_pared_C, T_centro_C, T_control_C, T_set_C, u_ssr_pct, T_amb_C).
- [Calculado] Tubo de acero 326 J/K; τ del tubo ≈ 105 s (≈17 K de retraso a 10 °C/min); Biot del lecho ≈ 9; con ε = 0.7, h_rad ≈ 8 W/m²K a 100 °C y ≈ 73 a 500 °C.
- MC-5438 (ficha archivos/investigaciones/controlador-mc5438-2026-11.md): modo manual (OutL) sin paso a paso documentado; Modbus RTU por RS-485 (opción G = 2) sin códigos de función; unidad de P1 no documentada; nivel PROG puede requerir al distribuidor (alternativa rAmP); sin USB. Horno "Max-Therma": sin datos en la web.

## Decisiones vigentes (no reabrir)
1. Orden: A motor → B ensayo térmico y calibración → C app Streamlit.
2. Numérica: paso dividido, conducción implícita (solver de banda) + química exacta por nodo, dt adaptativo.
3. Horno modelado como el real (masa térmica, P_max, PID → SSR, pérdidas, intercambio horno–tubo, termopar con retardo).
4. App en Streamlit local. El PID se sintoniza en Python; MATLAB/Simulink verifica y sirve para el microcontrolador.
5. Spec del motor: docs/specs/2026-11-08-motor-nuevo-design.md. Los datos del GIEM y del FTIR no se suben (repo público).
6. legacy/ borrado (en git, commit c2acaae). La referencia de legacy está en tests/referencia/.
7. Composición de Ballesteros 2014 para celulosa y lignina. Para comparar contra legacy, usar COMPOSICION_LEGACY de tests/test_simulador.py.
8. R_contacto_extra = 0.011 m²K/W hasta calibrarlo en B.
9. Criterio de cierre de B: RMS T_pared ≤ 5 K (las dos corridas); RMS T_centro ≤ 10 K fuera de la pirólisis y ≤ 20 K en ella.
10. Corrida en vacío con modelo 0D del tubo en calibracion/; no se toca el motor para eso.
11. Se agrega horno.modo = "medido" al motor.
12. Un solo escritor por rama: ensayo-termico = una sesión de Claude Code; app-streamlit = Cursor, solo app/.

## Restricciones
- En el Mac, trabajar solo dentro de `01_Horno_Vertical`. Nada de IA local en estos chats (eso es la Línea 2).
- La shell de Claude en el Mac es una VM Linux de 4 núcleos. Las corridas pesadas van en la Terminal de macOS con `modelos/PyrolysisReactorCoffee/.venv/bin/python`.
- Borrar, mover, unir a main o cambiar una decisión: solo con aprobación de Nick (PROPUESTA en la bitácora).
- Cada número con su fuente y su etiqueta. No inventar propiedades.

## Pendientes abiertos
- [ ] Script de ajuste + modo "medido" + prueba sintética — Claude Code (Mac)
- [ ] Foto de la placa del horno y de la etiqueta del controlador (MC-5438-BCD-EFG) — Nick
- [ ] En el equipo: entrar a manual y fijar OutL; ¿PROG abierto?; unidad de P1 — Nick
- [ ] Termopares K ×3, registrador de 1 s, adaptador USB–RS-485 — Nick / GIEM
- [ ] Menores de la revisión del motor (HANDOVER §3, notas para B), empezando por el aviso de horno saturado — Claude Code (B)
- Pendientes de química (Pirolizado 1-2, lípidos, densidad, N): en HANDOVER §1 — Nick
- [ ] App Streamlit — Cursor/Copilot (tarea en la bitácora, PREGUNTA 19:36)
- [ ] Actualizar 01_Horno_Vertical/BRIEF.md del Mac (está viejo) — Claude (B)

## Criterio de cierre
- [x] A: motor en main, 8 pruebas del spec en verde (contenedor, macOS y MATLAB)
- [ ] B: modelo calibrado contra las dos corridas del ensayo (criterio: decisión 9)
- [ ] C: app Streamlit que calibra, sintoniza el PID y compara recetas usando solo la interfaz pública
- [ ] Sintonía del PID verificada en MATLAB/Simulink antes de llevarla al horno

## Preguntas abiertas
- ¿Dónde está el termopar de control real del MC-5438?
- ¿Cuánto pesa la rampa en el horno real? Lo responde una corrida 3 a 20 °C/min (opcional en el spec de B).

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
- Un prompt de investigación que Nick pega es para otra IA: revisarlo, no ejecutarlo.
- No hacer commits de Claude en el Mac (sin credenciales; git deja locks). Lo que no quede en GitHub o Drive se dice claro como pendiente.
- No pegar comentarios `#` en comandos para zsh.
- Antes de crear algo en el Mac, confirmar la ruta real (`Documents - MacBook Pro de Nicolas`, no `~/Documents/Max_Power`).
- Un solo auditor por vez escribiendo CONTEXTO/HANDOVER.
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
| archivos/investigaciones/controlador-mc5438-2026-11.md | Ficha del MC-5438 | PID, modo manual, Modbus, registro del ensayo |
| PyrolysisReactorCoffee (rama ensayo-termico)/docs/specs/2026-11-08-ensayo-termico-design.md | Spec de B | Trabajar en B |
| archivos/investigaciones/datos-cafe-reactor-2026-11.md | Valores del café y del reactor verificados, por validar y descartados (de la investigación de Gemini) | Buscar una propiedad con fuente o calibrar en B |
| HANDOVER.md | Trazabilidad e historial de decisiones | Nick pregunte cuándo o por qué cambió algo |

## Glosario
- RAC + TGL: Ranzi–Anca-Couce 2017 + triglicéridos (Debiagi 2015). Modo ideal / físico: horno como retardo / con balance de energía, PID y SSR. bs / bh: base seca / húmeda.

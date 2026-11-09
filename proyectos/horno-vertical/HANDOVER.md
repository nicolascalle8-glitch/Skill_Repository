# HANDOVER — Horno vertical (pirólisis de café, práctica GIEM UdeA/EIA)

Última actualización: 2026-11-09 08:50 (Bogotá)
Chat de origen: Project "MacBook's Power": chat "Línea 1 horno vertical" (diseño, 19:11–22:10), chat del subproyecto A (motor nuevo, 19:57–21:55) y chat del subproyecto B (plan del ensayo térmico, 2026-11-08 22:06 – 2026-11-09 08:50)
Auditoría más reciente: 🟡 66/100 (chat B, 2026-11-09) · 🟢 78/100 (chat A) · 🟡 71/100 (chat de diseño)

---

## 1. Estado actual

### Qué es el proyecto
Modelo 2D (r, z) del reactor vertical de pirólisis de residuo de café (SCG) de la práctica de Nick en el GIEM. Cinética RAC + TGL. La meta es usarlo como "tuner" del horno real: calibrar el modelo con termopares, sintonizar el PID del MC-5438 y escoger la receta (rampa, T final, meseta). Tres subproyectos: A motor nuevo, B ensayo térmico y calibración, C app Streamlit.

### Dónde vamos
- **A (motor) — cerrado.** Paquete `motor/` en PyrolysisReactorCoffee, rama `main` (PR #2, commit ed907cf). Pasan las 8 pruebas del spec y las 84 de pytest, en el contenedor y en el Mac. legacy/ borrado.
- **C (app) — desbloqueado.** La interfaz quedó fija y le toca a Cursor/Copilot.
- **B (calibración) — plan aprobado, falta el script de ajuste.** Spec docs/specs/2026-11-08-ensayo-termico-design.md en la rama `ensayo-termico` (commit 657a86b, en GitHub). Nick aprobó sus 3 propuestas (2026-11-09 08:40). Siguiente: script de ajuste en calibracion/ probado con datos sintéticos, en una sola sesión de Claude Code en el Mac.
- **Controlador MC-5438:** investigado (Perplexity + Claude, 2026-11-09). Ficha: archivos/investigaciones/controlador-mc5438-2026-11.md. El horno "Max-Therma" no aparece en la web.

### Decisiones vigentes
| Fecha | Decisión | Por qué | Quién la tomó |
|---|---|---|---|
| 2026-11-08 | Orden A motor → B calibración → C app | Primero un motor verificado | Nick |
| 2026-11-08 | Paso dividido: conducción implícita + química exacta por nodo | El esquema explícito obligaba a dt ≈ 0.3 s | Nick |
| 2026-11-08 | Horno como el real (C_h, UA_p, P_max, PID → SSR, termopar con retardo) | Tuner del horno real | Nick |
| 2026-11-08 | App en Streamlit local; el PID se sintoniza en Python; MATLAB verifica y sirve para el micro | Reparto de herramientas | Nick |
| 2026-11-08 19:53 | Spec del motor aprobado (docs/specs/2026-11-08-motor-nuevo-design.md) | — | Nick |
| 2026-11-08 21:17 | Borrar legacy/ y reemplazar la copia vieja del Mac | El motor pasó la sección 9 | Nick |
| 2026-11-08 21:17 | Composición: celulosa 12.4 y lignina 23.9 % bs (Ballesteros 2014) | Revisión de la investigación de Gemini | Nick |
| 2026-11-08 21:17 | lecho.R_contacto_extra = 0.011 m²K/W [Calculado] | Resistencia efectiva de legacy al quitar el término que dependía de la malla | Propuso Claude, aprobó Nick |
| 2026-11-08 21:30 | Unir motor-nuevo a main | Dejar todo al día en GitHub | Nick |
| 2026-11-08 | Datos del GIEM y FTIR no se suben (repo público) | El reporte trae datos personales | Nick |
| 2026-11-09 08:40 | Criterio de cierre de B: RMS T_pared ≤ 5 K (las dos corridas); RMS T_centro ≤ 10 K fuera de la pirólisis y ≤ 20 K en ella | Propuesta del spec de B | Propuso Claude, aprobó Nick |
| 2026-11-09 08:40 | Corrida en vacío con un modelo 0D del tubo en calibracion/ (no se toca el motor) | El motor no tiene modo tubo vacío | Propuso Claude, aprobó Nick |
| 2026-11-09 08:40 | Agregar horno.modo = "medido" (T_horno(t) leído del CSV del ensayo) | Separa el horno del tubo en la corrida con café | Propuso Claude, aprobó Nick |
| 2026-11-08 22:30 aprox. | Un solo escritor por rama: ensayo-termico = una sesión de Claude Code; app-streamlit = Cursor, solo app/ | Evitar reprocesos y trabajo cruzado | Propuso Claude; Nick lo pidió así (pocos chats y ramas) |

### Hitos
| Fecha | Hito | Estado |
|---|---|---|
| 2026-11-08 19:20 | Modelo traído al Mac; una corrida de legacy medida (25 s en la VM); primer barrido en paralelo | ✅ |
| 2026-11-08 19:33 | Proyecto registrado en Skill_Repository + bitácora en Drive; datos de datos/ revisados (la composición 12/35/28/15 no venía del GIEM) | ✅ |
| 2026-11-08 19:36 | Tareas para Gemini, Perplexity y Cursor en la bitácora; reglas de ahorro de tokens | ✅ |
| 2026-11-08 19:55 | Spec del motor escrito (panel de asesores: opción 3, horno físico, identificabilidad) | ✅ |
| 2026-11-08 20:02 | Plan del motor (11 tareas) | ✅ |
| 2026-11-08 20:54 | Motor implementado + revisión por otro agente (6 hallazgos importantes corregidos) | ✅ |
| 2026-11-08 21:11 | 78 pruebas en macOS; caso base 1.4 s en el M4 | ✅ |
| 2026-11-08 21:15 | Prueba 7 en MATLAB real: 0.349 K (límite 4.75) | ✅ |
| 2026-11-08 21:30 | legacy/ borrado, composición Ballesteros, validaciones Bok/Inayat portadas (84 pruebas) | ✅ |
| 2026-11-08 21:36 | Unido a main (PR #2); Mac en main | ✅ |
| 2026-11-08 21:48 | Barrido de 30 casos en el Mac: 8.4 s (x9.3) | ✅ |
| — | App Streamlit (C) | 🔜 Cursor/Copilot |
| 2026-11-08 22:15 | Spec del ensayo térmico (B), rama ensayo-termico (657a86b) | ✅ |
| 2026-11-09 08:27 | Investigación del MC-5438 (Perplexity) + faltantes (Claude) | ✅ |
| 2026-11-09 08:40 | Nick aprueba las 3 propuestas del spec de B | ✅ |
| — | Script de ajuste con datos sintéticos (B) | 🔜 Claude Code en el Mac |
| — | Ensayo real (2 corridas) | 🔜 Nick, en el laboratorio |

### Pendientes
| Pendiente | Responsable | Fecha límite | Bloqueado por |
|---|---|---|---|
| ~~Plan del ensayo térmico~~ → hecho (spec en ensayo-termico) | — | — | — |
| ~~Datos del MC-5438~~ → ficha archivos/investigaciones/controlador-mc5438-2026-11.md | — | — | — |
| Script de ajuste en calibracion/ (0D del tubo + horno.modo = "medido"), probado con datos sintéticos | Claude Code (Mac) | — | — |
| Actualizar el spec de B: quitar "borrador" y anotar las 3 aprobaciones | Claude Code (Mac) | — | — |
| Foto de la placa del horno y de la etiqueta del controlador (código MC-5438-BCD-EFG; G = 2 es RS-485) | Nick | — | — |
| En el equipo: cómo entrar a manual y fijar OutL; ¿nivel PROG abierto?; unidad de P1 | Nick | — | — |
| Conseguir 3 termopares tipo K con vaina, registrador de 1 s y adaptador USB–RS-485 (si G = 2) | Nick / GIEM | — | — |
| Responder la PREGUNTA del 19:33 (masas y temperaturas de "Pirolizado 1-2"; ¿"Café grano" = residuo del GIEM?) | Nick | — | — |
| Medir lípidos (Soxhlet, hexano) y densidad aparente a 8 % de humedad | Nick / GIEM | — | — |
| Confirmar con el GIEM N = 0.418 % bs (la literatura da 2.3–2.8 %) | Nick | — | — |
| Menores de la revisión (ver Errores/Notas abajo) | Claude (B) | — | — |
| App Streamlit con la interfaz pública | Cursor/Copilot | — | — |
| Actualizar BRIEF.md del Mac (01_Horno_Vertical/BRIEF.md todavía dice "falta traer el modelo") | Claude (B) | — | — |
| Borrar las ramas motor-nuevo y claude/determined-curie-2btbhr de PyrolysisReactorCoffee (las dos ya están dentro de main) | Nick (aprobar) | — | — |

### Preguntas abiertas
- ¿Dónde está físicamente el termopar de control del MC-5438? El modelo lo pone en la cara externa del tubo.
- Valores reales de C_h, UA_p y emisividad del horno: se sacan del ensayo térmico.
- Craqueo de alquitranes en fase gas: desacuerdo del panel (20:00 aprox.). Prof. Térmicas lo quiere en el modelo; Ing. Simulación dice que no hace falta hasta tener rendimientos medidos. Lo resuelve medir el bio-oil de una corrida real a 500–550 °C. Fuera del spec del motor (§10).
- Sensibilidad a la rampa: el barrido de 5 a 20 °C/min casi no cambia los rendimientos (< 0.5 pp). Es propiedad del régimen `lecho_fijo` del modelo y hay que contrastarla con una corrida real.

### No volver a discutir
- Numérica (paso dividido, Euler implícito, solver de banda): verificada con Bessel, MATLAB y convergencia.
- Borrar legacy/: hecho y aprobado. La referencia vive en tests/referencia/ y en git (commit c2acaae).
- Composición de Ballesteros: aprobada. Para comparar contra legacy, usar COMPOSICION_LEGACY de tests/test_simulador.py.
- R_contacto_extra = 0.011: aprobado; se recalibra en B, no antes.
- Emisividad = 0 en la base: h_c = 90 ya incluye la radiación (legacy). Separarlos es trabajo de B.
- Plan del ensayo (qué se calibra con cada corrida, por qué h_c y k no se confunden) y las 3 aprobaciones del 2026-11-09.
- Horno "Max-Therma" en la web: dos búsquedas sin resultado. Sale de la placa o del GIEM.

### Archivos, links y entregables
| Qué | Dónde | Notas |
|---|---|---|
| Código del motor | github.com/nicolascalle8-glitch/PyrolysisReactorCoffee, rama main | motor/, parametros/base.toml, tests/, matlab/verificacion/ |
| Spec y plan del motor | docs/specs/2026-11-08-motor-nuevo-design.md, docs/plans/2026-11-08-motor-nuevo.md | — |
| Copia de trabajo en el Mac | ~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee | .venv propio; `git pull` para actualizar |
| Barrido en paralelo | 01_Horno_Vertical/modelos/barrido_motor.py | Salida en 01_Horno_Vertical/resultados/ |
| Barrido de 30 casos | 01_Horno_Vertical/resultados/barrido_20261108_2148.csv | biochar 20.3–25.8 %, bio-oil 35.8–39.6 % |
| Investigación de Gemini | Drive: Proyectos IA / horno-vertical / Investigación — datos del café y del reactor | Revisada: 6 errores de atribución (bitácora 20:11) |
| Bitácora | GitHub proyectos/horno-vertical/BITACORA.md + Drive (id en registry/DRIVE.yml) | Entradas del 2026-11-08 |
| Datos del laboratorio | 01_Horno_Vertical/datos/ (GIEM 28ago2604.pdf, FTIR CSV) | No van al repo |
| Spec del ensayo térmico (B) | PyrolysisReactorCoffee, rama ensayo-termico: docs/specs/2026-11-08-ensayo-termico-design.md | 657a86b |
| Ficha del MC-5438 | proyectos/horno-vertical/archivos/investigaciones/controlador-mc5438-2026-11.md | Resume los dos Docs de Drive |
| Investigaciones MC-5438 + PDFs | Drive: Proyectos IA / horno-vertical / investigaciones (folder 1hPOFZqmEttY3lUTJa2bdGmhnS9NIeavr) | Doc Perplexity 1lairm_wl…; Doc Claude 1ZswMN3e…; manual oficial, Terwin, STI |

### Preferencias de trabajo para este proyecto
- Español simple y directo; cifras con fuente y etiqueta ([Dato], [Supuesto], [Por validar], [Calculado]).
- Pruebas primero; no decir que algo funciona sin correrlo.
- Borrar, mover, unir a main o cambiar decisiones: solo con aprobación de Nick (PROPUESTA en la bitácora).
- Comandos para la Terminal de macOS: completos (con el `cd` desde ~), sin comentarios `#`, y la ruta con espacios entre comillas.
- Bitácora siempre en GitHub y en Drive, en la misma entrada.
- "Todo en GitHub absolutamente actualizado" al cerrar.

---

## 2. Mensaje de arranque para el chat nuevo

> Subproyecto B del horno vertical, en Claude Code en mi Mac. Lee solo `proyectos/horno-vertical/CONTEXTO.md` de `nicolascalle8-glitch/Skill_Repository` y las últimas 5 entradas de su BITACORA.md, más `docs/specs/2026-11-08-ensayo-termico-design.md` de este repo. Trabaja solo en la rama `ensayo-termico`. No reabras decisiones vigentes. Tarea: la del CONTEXTO ("Tu siguiente tarea").

---

## 3. Historial de actualizaciones

### 2026-11-09 08:50 — 🟡 66/100 (chat del subproyecto B)
- **Nuevo:** spec del ensayo térmico (rama ensayo-termico, 657a86b). Corrida 1 vacío → C_h, UA_p, h_c, ε; corrida 2 café → k_virgen_0 (25–200 °C), k_char_0 (enfriamiento), R_contacto (débil). Aparte: τ de termopares y P_max real.
- **Nuevo:** Nick aprobó las 3 propuestas (criterio RMS, tubo vacío 0D, horno.modo = "medido").
- **Nuevo:** investigación del MC-5438 (Perplexity + Claude) → ficha en archivos/investigaciones/. Lo importante: nivel PROG puede requerir al distribuidor; modo manual existe sin paso a paso; Modbus RTU sin códigos de función; unidad de P1 no documentada; sin USB.
- **Auditoría del chat B:** 66/100. Se desvió: Claude ejecutó como suyo un prompt de investigación pensado para otra IA (rompe el reparto) en vez de revisar la tabla de Perplexity. También dejó el push al Mac sin credenciales y la copia de Drive a medias, y Nick tuvo que preguntar. Las decisiones vigentes se respetaron.
- **Cerrado:** plan del ensayo térmico; datos del MC-5438 (En curso de Perplexity); PROPUESTA 22:40.
- **Cambiado:** nada del motor ni de base.toml.
- **Notas:** git en el Mac (VM de Claude) no puede borrar sus locks: dejó .git/stale-HEAD-lock y .git/stale-maintenance-lock (renombrados), que se pueden borrar. El Mac de Claude no tiene credenciales de GitHub: los commits de Claude van desde la nube o los empuja Claude Code.

### 2026-11-08 22:10 — 🟡 71/100 (chat de diseño "Línea 1 horno vertical")
- **Nuevo:** se suma la trazabilidad del chat de diseño (19:11–22:10): hitos de 19:20 a 19:55, desacuerdo abierto del panel sobre el craqueo de alquitranes y dos pendientes menores (BRIEF.md del Mac, ramas ya unidas).
- **Auditoría del chat de diseño:** 71/100. El chat era largo y con salidas pesadas (lecturas completas del Doc de Drive) y se mezcló con el orden de la cuenta de GitHub. Las decisiones se respetaron. Nick corrigió el rumbo dos veces ("el repositorio que estás usando", "yo organizo GitHub luego").
- **Fuera de este proyecto (no se archiva aquí):** Nick aprobó borrar 5 repos vacíos de su cuenta (Skills_Repository, PirolosisCatalitica, ProyectoPOO, ProyectoPOO1, RefactorizacionCompleta) y lo hace él después. Los repos de Valeria se quedan.
- **Cerrado:** ninguno nuevo. **Cambiado:** nada; el estado y la siguiente tarea (B) del handover de 21:55 siguen igual.

### 2026-11-08 21:55 — 🟢 78/100
- **Nuevo:** primer HANDOVER del proyecto. Subproyecto A cerrado: motor implementado (11 tareas), revisado, verificado en el Mac y en MATLAB, unido a main.
- **Nuevo:** revisión de la investigación de Gemini (bitácora 20:11). Entró la composición de Ballesteros 2014.
- **Nuevo:** barrido_motor.py en el Mac; barrido de 30 casos en 8.4 s.
- **Cerrado:** implementar el motor; PROPUESTA de borrar legacy/; datos de la revisión de Gemini; R_contacto; unir a main; limpieza del Mac.
- **Cambiado:** composición 12/35/28/15 % bs (legacy, sin fuente) → celulosa 12.4 y lignina 23.9 % bs (Ballesteros 2014); hemicelulosa 35 y lípidos 15 siguen sin medir. R_contacto_extra 0.003 → 0.011 m²K/W, porque el motor ya no suma Δr_l/(2k_l), que dependía de la malla.
- **Reemplazado / ya no aplica:** ~~simulador_interactivo.py como modelo vigente~~ → paquete motor/. ~~modelos/barrido_paralelo.py~~ → barrido_motor.py (Nick borró el viejo). ~~Copia del Mac sin git (commit ddb0a63)~~ → clon con git en main.
- **Notas para B** (menores de la revisión, no corregidos):
  - no avisa cuando el horno físico satura: con la base, P_max/C_h = 7.5 K/min, menos que la rampa de 10
  - no avisa si T_final < T_inicial
  - no hay cota de divergencia
  - Resultado no guarda los parámetros que se usaron
  - las variables BLAS no aplican con fork
  - lecho al 70 % de humedad lento (~15 s)
  - "biochar" incluye cenizas
  - graficas.py fuerza Agg
  - el termopar va al nodo más cercano sin aviso
  - la historia usa T_termopar_control en vez de T_termopar_<n>
  - balance_energia es cierre numérico, no físico

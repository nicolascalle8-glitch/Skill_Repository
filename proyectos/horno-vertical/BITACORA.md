# BITÁCORA — Horno vertical (pirólisis de café, práctica GIEM UdeA/EIA)

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra. Copia idéntica en Google Drive: Proyectos IA / horno-vertical / Bitácora — horno-vertical.

## En curso
- (nada)

## Propuestas sin respuesta
- (ninguna)

---

## Entradas

### 2026-11-09 10:13 — Claude Opus 5.5 — HECHO
**Qué:** Software del subproyecto B terminado en la rama ensayo-termico; queda sin unir a main. Decisión de Nick (2026-11-09 09:36): RMS T_horno ≤ 5 K entra al criterio de cierre de la corrida 1, porque es lo único que comprueba C_h y UA_p, la base para sintonizar el PID en C. Se implementó horno.modo = "medido" (HornoMedido lee T_horno(t) de un CSV y lo interpola), se corrió el sintético y se hizo una revisión independiente del diff contra main. Se corrigieron 1 hallazgo crítico y 4 importantes. Aquí se para el software de B; sigue el laboratorio.
**Archivos:** PyrolysisReactorCoffee, rama ensayo-termico, commit 563cc20 (sobre 4ea8f3b): motor/horno.py, motor/simulador.py, motor/parametros.py, parametros/base.toml, calibracion/ajuste_termico.py, calibracion/sintetico.py, tests/test_calibracion.py (nueva) y spec §6 y Aprobación de la decisión 9. Skill_Repository, main: 2147998 (decisión 9 en CONTEXTO.md). Drive: la copia "CONTEXTO — horno-vertical" quedó igual al CONTEXTO de 2147998, con decisiones 9 a 12 y ruta nueva, en el mismo documento. Mac, fuera de git: 01_Horno_Vertical/resultados/calibracion_sintetica/ (corrida1.csv, corrida2.csv, corrida2_T_horno_limpia.csv, calibracion.json).
**Fuentes:** Decisión de Nick en el chat (2026-11-09 09:36). Los valores verdaderos son VERDAD de calibracion/sintetico.py, elegidos a propósito: no son propiedades del horno real. Con datos sintéticos no se valida el horno; solo se prueba que el software recupera valores conocidos. Las tolerancias por parámetro (TOL_PCT: 5 %, y 20 % para R_contacto) las eligió Claude antes de la corrida final; §6 solo pone límites de RMS.
**Verificado:** Pruebas: 102 pasan (84 de antes, 11 de test_modo_medido.py, 7 nuevas de test_calibracion.py), 69 s. Modos ideal y fisico: el revisor comparó main contra la rama (ideal, fisico promedio y fisico onoff) con los mismos pasos, rendimientos e historias. Sintético final, verdadero → recuperado (error): C_h 12000 → 12006 J/K (+0.05 %); UA_p 3 → 3.0008 W/K (+0.03 %); h_c 35 → 34.861 W/m²K (−0.40 %); ε 0.6 → 0.59215 (−1.31 %); k_virgen_0 0.15 → 0.15097 W/mK (+0.64 %); k_char_0 0.11 → 0.1139 W/mK (+3.54 %); R_contacto_extra 0.015 → 0.015834 m²K/W (+5.56 %). Los 7 quedan dentro de TOL_PCT. RMS: corrida 1, T_pared 0.99 K y T_horno 1.00 K; corrida 2, T_pared 1.01 K, T_centro 0.99 K fuera de la pirólisis y 1.53 K en ella: cumple las 5 condiciones de §6. Correlación R_contacto–k: 0.62 con k_virgen_0 y 0.71 con k_char_0, bajo el umbral 0.9 (R_contacto no se deja fijo). La primera corrida, antes de corregir, cumplía los mismos RMS con k_virgen_0 −9.00 %, k_char_0 −17.90 % y R_contacto −34.42 %: el RMS solo no detecta ese sesgo; la causa era dt_max = 20 s en el ajuste. Aun después, el error de k_char_0 y R_contacto es unas 8 y 6 veces su sigma, así que las sigmas son optimistas. Correcciones: paso de tiempo fino en el ajuste; sigma de la corrida 2 con la incertidumbre de h_c y ε; inicio del enfriamiento robusto al sobrepaso del horno (usa u_ssr_pct si existe); el ajuste rechaza corridas donde T_pared o T_centro arrancan a más de 5 K de T_horno; el sintético falla si un parámetro sale de tolerancia. Las correcciones se comprobaron con pruebas y sintético, sin segunda revisión de código. A las 10:05 otra sesión de Claude subió a la rama el mismo trabajo (5e9c3c2) y chocó con este; luego ese commit desapareció de origin, sin que esta sesión lo quitara, y por orden de Nick se subió 563cc20 sin --force. Main sigue en ed907cf.
**Para Nick:** (a) Aprobar o no unir ensayo-termico a main. (b) Laboratorio: MC-5438 (modo manual OutL, nivel PROG, unidad de P1), τ de termopares, P_max y corrida 1 en vacío. Arrancar cada corrida con tubo y lecho en equilibrio con el horno (diferencia ≤ 5 K) o el ajuste la rechaza, y registrar u_ssr_pct. (c) Confirmar si valen las tolerancias de TOL_PCT. (d) Sigue pendiente borrar 01_Horno_Vertical_VIEJO_iCloud cuando lo confirmes. (e) La copia del HANDOVER en Drive sigue con la ruta vieja.
**Para la siguiente IA:** No abrir software de B sin pedido de Nick: lo siguiente es el laboratorio. Un solo escritor por rama (decisión 12). Hallazgos menores de la revisión sin corregir: el informe no trae sol.status del optimizador; si ε no es significativa el spec §4 pide reajustar con ε = 0; no está el paso de valores calibrados a base.toml y la etiqueta "Calibrado" no es válida en motor/parametros.py ("Medido" sí); leer_ensayo falla con BOM o con texto en columnas no requeridas; un TOML externo sin horno.archivo_medido ya no carga; calibracion/README.md está desactualizado. En modo medido el motor arranca tubo y lecho a T_horno(0): por eso el rechazo está en el ajuste. "Tu siguiente tarea" y Pendientes del CONTEXTO no se actualizaron en esta pasada.

### 2026-11-09 09:34 — Claude Opus 5.5 — HECHO
**Qué:** Mudanza del proyecto fuera de iCloud, pedida por Nick. Ruta vieja: ~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/01_Horno_Vertical. Ruta nueva: ~/Developer/Max_Power/01_Horno_Vertical. Motivo: iCloud dañaba el .venv, y eso es la causa más probable de que pytest se colgara. La carpeta vieja no se borró: quedó como 01_Horno_Vertical_VIEJO_iCloud. El subproyecto B sigue a medias: spec listo; ajuste, sintético y prueba del modo medido escritos pero sin ejecutar; horno.modo = "medido" todavía no está en motor/.
**Archivos:** PyrolysisReactorCoffee, rama ensayo-termico: 6714eef (spec aprobado, calibracion/ajuste_termico.py, calibracion/sintetico.py, tests/test_modo_medido.py) y 4ea8f3b (ruta del README). Skill_Repository, main: 787a7c5 (ruta en proyectos/horno-vertical/CONTEXTO.md, líneas 18, 73 y 89, y HANDOVER.md, línea 97). Mac, fuera de git: se copiaron a la ruta nueva datos/ (5 archivos), resultados/ (4), BRIEF.md y modelos/barrido_motor.py, y en estos dos últimos se cambió la ruta solo en la copia nueva. El spec, §6, deja RMS T_horno como dato reportado y fuera del criterio, igual que la decisión 9.
**Fuentes:** Pedido de Nick en el chat (2026-11-09). Los 4.220 duplicados con " 2" y el error "Resource deadlock avoided" son el diagnóstico de Nick; Claude no los contó ni los reprodujo. Claude sí vio el cuelgue: pytest con 0.4 s de CPU en más de 6 minutos en la carpeta vieja.
**Verificado:** Los dos commits de ensayo-termico están en origin. Clon nuevo limpio en esa rama. Copia: 11 archivos, mismo conteo y SHA-256 iguales entre las dos rutas, medido antes de editar BRIEF.md y barrido_motor.py. En la ruta nueva, con .venv recién creado (0 archivos " 2"): 84 pruebas pasan y 1 error esperado (tests/test_modo_medido.py, falta HornoMedido), en 77 s y sin cuelgues; se corrió con --continue-on-collection-errors, porque pytest -q a secas se detiene en ese error. barrido_motor.py --demo: 4 casos, escribió resultados/barrido_20261109_0928.csv. Carpeta vieja renombrada, con su repo en 6714eef. El --exclude='* 2*' pedido también excluía "Captura de pantalla 2026-09-04 170250.png" (no es duplicado): se copió aparte. No se ejecutaron ajuste_termico.py ni sintetico.py, así que no hay parámetros recuperados.
**Para Nick:** (a) Cerrar VS Code y abrirlo en ~/Developer/Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee. (b) Borrar 01_Horno_Vertical_VIEJO_iCloud cuando confirmes que todo está bien. (c) Sigue pendiente decidir si RMS T_horno ≤ 5 K entra al criterio de cierre de la corrida 1 (cambio a la decisión 9).
**Para la siguiente IA:** Trabajar solo en ~/Developer/Max_Power/01_Horno_Vertical. 02_IA_Local no se movió: sigue en la ruta de iCloud, con sus rutas sin cambiar. Sigue el paso 2 del plan de B (horno.modo = "medido" en motor/horno.py, motor/simulador.py, motor/parametros.py y base.toml) y luego correr el sintético. La revisión de código del diff completo va antes del commit final de B. Las copias en Drive del CONTEXTO y del HANDOVER siguen con la ruta vieja. No usar grep -r ni timeout en este Mac sin revisar: grep es ugrep dentro de la shell de Claude y se colgó en la carpeta vieja, y timeout no existe.

### 2026-11-09 08:50 — Claude Opus 5.5 — HECHO
**Qué:** Handover 2026-11-09 — 🟡 66/100. Se cierra el chat del subproyecto B (plan del ensayo térmico). Plan aprobado; lo que sigue va en una sola sesión de Claude Code en el Mac, rama ensayo-termico.
**Archivos:** proyectos/horno-vertical/HANDOVER.md (estado, 4 decisiones nuevas, hitos, pendientes, historial); CONTEXTO.md (reescrito, 1.655 palabras); archivos/investigaciones/controlador-mc5438-2026-11.md (nuevo); archivos/hechos-cafe-y-barrido-2026-11.md (nuevo: hechos sacados del CONTEXTO sin cambios).
**Fuentes:** este chat (2026-11-08 22:06 – 2026-11-09 08:50) y la bitácora.
**Verificado:** El CONTEXTO tiene 1.655 palabras (un poco más que el tope de ~1.500). Las decisiones 9–12 coinciden con las respuestas de Nick de las 08:40.
**Para Nick:** Abrir Claude Code en el Mac con el mensaje de arranque (HANDOVER §2). Este chat ya se puede borrar.
**Para la siguiente IA:** Arrancar con CONTEXTO.md, las últimas 5 entradas y el spec de B. No volver a buscar el horno en la web.

### 2026-11-09 08:32 — Claude Opus 5.5 — HECHO
**Qué:** Datos del MC-5438 que Perplexity dejó como "no encontrado". Siguen sin aparecer: unidad de P1, paso a paso del modo manual, códigos de función Modbus, número de programas, USB. Dato nuevo: abrir el nivel PROG "needs to contact distributor" (manual oficial P.20). Horno "Max-Therma": sin resultados. Se cierra el "En curso" de Perplexity (su Doc: https://docs.google.com/document/d/1lairm_wlDatv9MnkhmZN58nJezyGwt_F1qoirpmV4uI/edit). Nota: Claude hizo esta búsqueda con un prompt pensado para otra IA; quedó así, pero no era su tarea.
**Archivos:** Doc https://docs.google.com/document/d/1ZswMN3ejfi6rCBTDzbaTeR0DSDLTycyiXrMs7Ydrz3Y/edit (Drive, horno-vertical/investigaciones). Ficha que resume los dos Docs: archivos/investigaciones/controlador-mc5438-2026-11.md.
**Fuentes:** manual oficial Maxthermo MC-5x38; manual de Terwin (sí descarga); catálogo de STI-GAS.
**Verificado:** En la ficha se marca qué releyó Claude en la fuente y qué viene solo de Perplexity.
**Para Nick:** Foto de la placa del horno y de la etiqueta del controlador; probar en el equipo el modo manual, el nivel PROG y la unidad de P1.
**Para la siguiente IA:** Usar la ficha, no los Docs.

### 2026-11-08 22:40 — Claude Opus 5.5 — PROPUESTA
**Qué:** Decidir tres puntos del spec de B: (1) criterio de cierre: RMS T_pared ≤ 5 K en las dos corridas, T_centro ≤ 10 K fuera de la pirólisis y ≤ 20 K en ella; (2) corrida en vacío con un modelo 0D del tubo en calibracion/ (no toca el motor) o con un modo "tubo vacío" en el motor; (3) agregar horno.modo = "medido" (T_horno(t) leído del CSV) para separar el horno del tubo en la corrida con café.
**Recomendación:** (1) sí; (2) 0D; (3) sí.
**Para Nick:** Responder sí/no a cada uno. ✅ Aprobado por Nick — 2026-11-09 08:40: (1) sí, (2) modelo 0D en calibracion/, (3) sí

### 2026-11-08 22:40 — Claude Opus 5.5 — HECHO
**Qué:** Plan del ensayo térmico (subproyecto B), borrador. Corrida 1 (tubo vacío) → C_h, UA_p, h_c, ε. Corrida 2 (café, 10 °C/min a 500 °C) con eso fijo → k_virgen_0 (25–200 °C), k_char_0 (enfriamiento final), R_contacto_extra (débil con 2 termopares). Aparte: τ de termopares (agua hirviendo) y P_max real (pinza). h_c y k no se confunden porque h_c sale de la corrida sin lecho.
**Archivos:** PyrolysisReactorCoffee, rama ensayo-termico (solo local en el Mac, commit 657a86b): docs/specs/2026-11-08-ensayo-termico-design.md.
**Fuentes:** base.toml (main, ed907cf), spec del motor §6 y §11. Números de orden de magnitud marcados [Calculado] en el spec.
**Verificado:** Las claves y valores del spec coinciden con base.toml. El motor no tiene modo de tubo vacío ni de T_horno medido (revisado en motor/simulador.py y horno.py). No se corrió ningún ajuste: aún no hay datos.
**Para Nick:** (a) Hacer push de la rama desde la Terminal (el Mac de Claude no tiene credenciales de GitHub). (b) Aprobar la PROPUESTA de arriba. (c) Ver si el MC-5438 deja fijar la salida del SSR a mano y registrar u_ssr_pct. (d) git dejó dos locks renombrados en .git (stale-HEAD-lock, stale-maintenance-lock): se pueden borrar.
**Para la siguiente IA:** Copia en Drive de esta entrada pendiente. Siguiente paso de B: script de ajuste en calibracion/ con datos sintéticos (el motor con valores conocidos + ruido) para probar que el ajuste recupera los parámetros antes de tener datos reales.

### 2026-11-08 22:10 — Claude Opus 5.5 — HECHO
**Qué:** Handover del chat de diseño "Línea 1 horno vertical" — 🟡 71/100. Se suma al handover de 21:55 (chat A) sin cambiar su estado ni su siguiente tarea (B).
**Archivos:** proyectos/horno-vertical/HANDOVER.md (hitos 19:20–19:55, desacuerdo del panel sobre el craqueo de alquitranes, 2 pendientes menores, entrada nueva en el historial); proyectos/horno-vertical/CONTEXTO.md (1 pregunta abierta, 1 pendiente, 2 errores que no repetir; 1.492 palabras). Copias de Drive del CONTEXTO y del HANDOVER actualizadas.
**Fuentes:** Chat "Línea 1 horno vertical" (19:11–22:10) y chat "Motor nuevo horno vertical" (leído desde el chat y la bitácora).
**Verificado:** Mac: modelos/PyrolysisReactorCoffee en main (ed907cf), igual a GitHub y sin cambios sueltos. Las ramas motor-nuevo y claude/determined-curie-2btbhr ya están dentro de main. En el repo público no hay datos del GIEM ni datos personales.
**Para Nick:** Abrir el chat de B con el mensaje de arranque del HANDOVER §2. Después ya se puede borrar este chat ("Línea 1 horno vertical").
**Para la siguiente IA:** Nada cambia para B: arrancar con CONTEXTO.md y las últimas 5 entradas.

### 2026-11-08 22:05 — Claude Opus 5.5 — HECHO
**Qué:** Depuración del Project "MacBook's Power". El arranque de cada chat ya es liviano (~5.300 tokens aprox.). El gasto grande estaba en leer completa la bitácora de Drive: ~20.000 tokens aprox. por cada escritura, y se evita con el hábito nuevo.
**Archivos:**
- proyectos/horno-vertical/archivos/investigaciones/datos-cafe-reactor-2026-11.md (nuevo: ficha con lo verificado, por validar y descartado de la investigación de Gemini)
- proyectos/horno-vertical/CONTEXTO.md (hábitos 4–6 y la ficha en el mapa de archivos)
- memoria del Project: descripción de areas/horno-lecho-vertical.md
**Fuentes:** depurador-recursos; REVISIÓN 20:11.
**Verificado:** Cada cifra de la ficha sale de la REVISIÓN 20:11. El CONTEXTO tiene 1.433 palabras.
**Para Nick:**
- (1) Borrar a mano los chats "M4 Max compute utilization" y "Proyecto: funciones y uso". También "Línea 1 horno vertical", pero después de que su auditor termine (revisión programada a las 22:09), y este chat cuando abras el B.
- (2) Corregir la memoria de la cuenta en un chat normal, fuera del Project: profile.md y varias áreas (fábrica de medias, Arde La Selva, Artequino, Conectar Valores, Q2 Office, memecoins, Assetto Corsa, Dr. Calle, David Córdoba) aparecen como tuyas, pero según contexto-nick son de Juan José; además, coursework.md está vencido.
- (3) Responder en el chat de la Línea 2 si se actualiza lineas/02-ia-local.md.
**Para la siguiente IA:**
- Propiedades del café con fuente: usar la ficha, no el documento de Gemini.
- Bitácora de Drive: nunca leerla completa.

### 2026-11-08 21:55 — Claude Opus 5.5 — HECHO
**Qué:** Handover 2026-11-08 — 🟢 78/100. Se cierra el chat del subproyecto A (motor nuevo).
**Archivos:** proyectos/horno-vertical/HANDOVER.md (nuevo, primer handover); proyectos/horno-vertical/CONTEXTO.md (reescrito).
**Fuentes:** este chat (19:57–21:55) y la bitácora.
**Verificado:** CONTEXTO con menos de 1.500 palabras; las decisiones y los pendientes coinciden con las entradas de hoy.
**Para Nick:** Abrir un chat nuevo en el Project "MacBook's Power" con el mensaje de arranque del HANDOVER §2 (subproyecto B, plan del ensayo térmico). La app (C) va en Cursor/Copilot.
**Para la siguiente IA:** Arrancar leyendo solo CONTEXTO.md y las últimas 5 entradas de esta bitácora. Siguiente tarea: plan del ensayo térmico (B).

### 2026-11-08 21:36 — Claude Opus 5.5 — HECHO
**Qué:** motor-nuevo unido a main en PyrolysisReactorCoffee (PR #2, aprobado por Nick en el chat).
**Archivos:** PyrolysisReactorCoffee main = ed907cf (merge de 7fd829c). En el Mac, modelos/PyrolysisReactorCoffee quedó en la rama main.
**Fuentes:** n/a.
**Verificado:** main contiene motor/, parametros/, tests/, matlab/, docs/, app/, calibracion/ y ya no tiene legacy/. Las 84 pruebas pasaron en ese mismo commit (7fd829c).
**Para Nick:** Para actualizar en la Terminal de macOS: `git pull` dentro de modelos/PyrolysisReactorCoffee.
**Para la siguiente IA:** Trabajar desde main; las ramas nuevas salen de main.

### 2026-11-08 21:30 — Claude Opus 5.5 — HECHO
**Qué:** Se aplicaron las tres aprobaciones de Nick (21:17): (1) se borró legacy/ del repo y se reemplazó en el Mac la copia vieja; (2) entraron a base.toml los datos de la REVISIÓN de Gemini; (3) R_contacto_extra = 0.011 m²K/W queda confirmado.
**Archivos:**
- PyrolysisReactorCoffee, rama motor-nuevo, commit 7fd829c:
  - legacy/ borrado (sigue en el historial, commit c2acaae)
  - tests/referencia/ (curva T_centro de legacy y foto de la química)
  - motor/cinetica/tga.py (muestra 0D)
  - tests/test_validacion_cinetica.py (Bok 2012, Inayat 2022)
  - parametros/base.toml
  - README.md, docs/EVALUACION_CINETICAS.md (nota), spec §3
- Mac:
  - modelos/PyrolysisReactorCoffee = clon nuevo con git (copia vieja borrada)
  - modelos/barrido_motor.py nuevo (barrido en paralelo con el motor); barrido_paralelo.py viejo sin tocar
**Fuentes:** base.toml:
- celulosa 12.4 y lignina 23.9 % bs [Dato]: Ballesteros et al. 2014, Tabla 1
- hemicelulosa 35 [Supuesto], rango 34–39
- lípidos 15 [Por validar]: Atabani 2019, 13.4–21.5
- densidad 380 [Por validar]: Guendouz 2023, 387
- otros 11.39 [Calculado]
- nota de emisividad ≈0.7 (Incropera A.11) [Por validar]
**Verificado:**
- `python -m pytest tests -q` → 84 passed (contenedor). La prueba 2 sigue contra legacy con la composición de legacy y la curva guardada: RMS T_centro 4.5 K.
- Validaciones de cinética portadas: Bok 54.85 ± 3, Inayat 22.5 ± 5, mismos números que legacy.
- Caso base con la composición nueva: biochar 24.22 / bio-oil 39.60 / gas 20.31 / agua 15.88 %. Antes, con la de legacy: 24.93 / 38.95 / 20.23 / 15.90.
- Mac: git en 7fd829c; barrido_motor.py --demo corre (4 casos, 1.9 s, x3.5 con 4 procesos en la VM).
**Para Nick:**
- (a) Crear de nuevo el .venv en macOS: se borró porque apuntaba a la carpeta con el nombre viejo.
- (b) Si quieres, borrar a mano en la Terminal modelos/barrido_paralelo.py y los restos ignorados por git (modelos/PyrolysisReactorCoffee/legacy/, que solo tiene __pycache__, y pirolisis_cafe.egg-info/). El permiso de Claude no alcanzó para sobrescribir ni borrar eso.
- (c) Decidir si se une motor-nuevo a main. ✅ Aprobado por Nick — 2026-11-08 (unido, PR #2)
- Sigue pendiente: medir lípidos (Soxhlet) y densidad a 8 % de humedad; pedir al GIEM que confirme N = 0.418 % bs.
**Para la siguiente IA:**
- Ya no hay legacy/: la referencia de legacy está en tests/referencia/ y en el historial de git.
- El caso base usa la composición de Ballesteros; para comparar con legacy usa COMPOSICION_LEGACY de tests/test_simulador.py.

### 2026-11-08 21:15 — Claude Opus 5.5 — HECHO
**Qué:** Prueba 7 del spec (verificación térmica en MATLAB) corrida por Nick en MATLAB real.
**Archivos:** PyrolysisReactorCoffee, rama motor-nuevo: matlab/verificacion/README.md (resultado anotado).
**Fuentes:** salida de MATLAB que Nick pegó en el chat.
**Verificado:** ode15s en MATLAB contra Euler implícito de Python (dt 0.5 s): error máximo 0.349 K, límite 4.75 K (1 % de 475 K) → PASA. Volúmenes iguales a Python (diferencia relativa 1.58e-11). Coincide con Octave y con el BDF de Python (0.349 K). Con esto pasan las 8 pruebas del spec.
**Para Nick:** Quedan las PROPUESTAS de las 20:54 y confirmar R_contacto_extra = 0.011 m²K/W.
**Para la siguiente IA:** Prueba 7 cerrada; no hace falta repetirla salvo que cambie la conducción o la interfaz.

### 2026-11-08 21:11 — Claude Opus 5.5 — HECHO
**Qué:** Nick corrió el motor nuevo en la Terminal de macOS (M4 Max, Python 3.13): pruebas y velocidad.
**Archivos:** Mac: Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee-motor-nuevo (.venv creado ahí, no se sube).
**Fuentes:** salida de la Terminal que Nick pegó en el chat.
**Verificado:** `.venv/bin/python -m pytest tests -q` → 78 passed en 88 s. Caso base: 1.4 s (prueba 6, meta ≤ 5 s), con biochar 24.93 / bio-oil 38.95 / gas 20.23 / agua 15.90 %, igual que en el contenedor y en legacy. La referencia de legacy (25 s) se midió en la VM y no en macOS, así que "≈18× más rápido" es aproximado.
**Para Nick:** Falta la prueba 7 en MATLAB (matlab/verificacion/README.md) y decidir las PROPUESTAS de las 20:54.
**Para la siguiente IA:** El motor corre nativo en macOS; usar el .venv de esa carpeta para las corridas pesadas.

### 2026-11-08 20:54 — Claude Opus 5.5 — PROPUESTA
**Qué:** (1) Borrar `legacy/` del repo PyrolysisReactorCoffee: el motor ya pasa la sección 9 del spec. (2) En el Mac, reemplazar la copia vieja `modelos/PyrolysisReactorCoffee` (commit ddb0a63, sin git) por la nueva `modelos/PyrolysisReactorCoffee-motor-nuevo` (clon con git, rama motor-nuevo).
**Archivos:** nada todavía.
**Fuentes:** entrada HECHO 20:54 (pruebas 1–8).
**Verificado:** n/a.
**Para Nick:** Aprobar o rechazar cada punto. Antes de borrar legacy/ conviene correr la prueba 7 en MATLAB real y las pruebas en la Terminal de macOS. Si se borra: las pruebas de validación Bok 2012 / Inayat 2022 viven solo en legacy/tests y habría que portarlas antes.
**Para la siguiente IA:** No borrar ni mover nada hasta que Nick apruebe aquí.
✅ Aprobado por Nick — 2026-11-08 (hecho a las 21:30, ver entrada HECHO)

### 2026-11-08 20:54 — Claude Opus 5.5 — HECHO
**Qué:** Motor nuevo implementado (subproyecto A, 11 tareas del plan, con pruebas primero) y revisado por un revisor nuevo. **La interfaz pública quedó fija:** `cargar_parametros`, `simular`, `simular_lote`, `Resultado` (spec §7).
**Archivos:** PyrolysisReactorCoffee, rama motor-nuevo (commits a37bd5b..05cd97d): motor/, parametros/base.toml, tests/ (78 pruebas), matlab/verificacion/, legacy/ (código anterior sin cambios), pyproject.toml, README.md. En el Mac: Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee-motor-nuevo/ (clon con git).
**Fuentes:** spec docs/specs/2026-11-08-motor-nuevo-design.md; legacy simulador_interactivo.py. Todos los parámetros de base.toml traen unidad, etiqueta y fuente; casi todos son [Supuesto] de legacy.
**Verificado:** `python -m pytest tests -q` → 78 passed (3 min 29 s, contenedor Linux).
- (1) Bessel: error ≤ 1 % de ΔT0 en Fo 0.05, 0.2 y 0.5.
- (2) Caso base contra legacy: biochar 24.93 / bio-oil 38.95 / gas 20.23 / agua 15.90 % (legacy 24.93 / 38.94 / 20.23 / 15.90); RMS de T_centro 4.5 K (límite 10).
- (3) 16 casos: masa ≤ 3e-13 %, energía ≤ 1e-8 % (es cierre numérico).
- (4) dt/2: rendimientos 0.005 pp, T_centro 1.3 K RMS.
- (5) Malla ×2: rendimientos 0.001 pp, T 0.8 K RMS.
- (6) Velocidad: 2.1 s el caso base en la VM del Mac (legacy 25 s en la misma VM), ≈12 veces más rápido.
- (7) MATLAB: probado con GNU Octave, ode15s contra Python 0.349 K (límite 4.75 K), PASA; falta MATLAB real.
- (8) Parámetros malos: ErrorParametro con el nombre del parámetro.
- Revisión final por otro agente: 0 críticos, 6 importantes, todos corregidos con su prueba.
**Para Nick:**
- (a) En la Terminal de macOS, dentro de modelos/PyrolysisReactorCoffee-motor-nuevo: `python3 -m venv .venv && .venv/bin/pip install -e ".[pruebas]" && .venv/bin/python -m pytest tests -q`.
- (b) Prueba 7 en MATLAB: ver matlab/verificacion/README.md y pegar el número aquí.
- (c) Decisión que tomó Claude y que conviene que revises: lecho.R_contacto_extra pasó de 0.003 a 0.011 m²K/W [Calculado]. Legacy sumaba una resistencia que dependía de la malla; 0.011 es su valor efectivo y B lo calibra. ✅ Aprobado por Nick — 2026-11-08
- (d) PROPUESTA de arriba (borrar legacy/).
**Para la siguiente IA:**
- CURSOR/COPILOT: ya puedes hacer tu tarea (PREGUNTA 2026-11-08 19:36). Usa SOLO `from motor import cargar_parametros, simular, simular_lote` y los campos de `Resultado`:
  - `rendimientos`
  - `historia`, con claves t, T_horno, T_set, T_pared, T_lecho_superficie, T_centro, T_termopar_control, masa_residual, u
  - `mapas`, `balance_masa`, `balance_energia`, `confiable`, `supuestos`, `avisos`, `a_csv()`
  - las gráficas con `motor.graficas.graficar`
  - Para mostrar etiquetas y fuentes: `p.supuestos()` y `p.info(clave)`.
  - No tocar motor/, parametros/ ni tests/ existentes.
- Claude (B): pendientes menores de la revisión, en el ledger del commit 05cd97d:
  - aviso cuando el horno físico satura (con los valores de arranque, P_max/C_h = 7.5 K/min, el horno no alcanza la rampa de 10 °C/min)
  - T_final < T_inicial sin aviso
  - guardar los parámetros en Resultado
  - variables BLAS con fork

### 2026-11-08 20:11 — Claude Opus 5.5 — REVISIÓN
**Qué:** Revisé fuente por fuente la investigación de Gemini (6 temas). Sirve como base, pero no se puede copiar tal cual al modelo.
**Archivos:** Drive: Proyectos IA / horno-vertical / Investigación — datos del café y del reactor (solo lectura).
**Fuentes:** Ballesteros 2014 (Tabla 1 leída), Oliva 2022, Taleb 2020, Zuluaga 2024, Ben Abdallah 2023, Choi 2020, Debiagi 2015, Gupta 2003 (abstract), Guendouz 2023, Cardoso 2018, Nasr 2023 (citado como "Aouadja"), NASA CR-1431, Incropera A.11, Kordoghli 2026, Semaan 2022.
**Verificado:**
- Bien: composición de Ballesteros (celulosa 12.4, hemicelulosa 39.1, lignina 23.9 % bs), TGA de Ben Abdallah y Zuluaga, cinética TGL (A = 7e12 1/s, E = 191.2 kJ/mol), cp y k de char de Gupta (madera blanda) y ρ = 387 kg/m³ de Guendouz (SCG seco).
- 6 errores de atribución:
  - La "Tabla 389" de NASA CR-1431 no existe en ese documento.
  - El 27 % de Taleb es lignina aislada, no Klason, así que no respalda el 28 %.
  - "Aouadja 2023" es en realidad Nasr et al., sobre materiales de construcción.
  - El hilo caliente de Guendouz se usó en el concreto, no en el café.
  - Las áreas DTG de Ben Abdallah están mal copiadas: el artículo da 3.9 / 10.5 / 48.9.
  - Los ácidos grasos a 197–362 °C no aparecen en Zuluaga.
- Además mezcla datos de madera y de grano tostado como si fueran de SCG.
**Para Nick:**
- PROPUESTA: bajar la lignina a 24 % bs (Ballesteros 2014). ✅ Aprobado por Nick — 2026-11-08 (quedó 23.9 %, el número exacto de la fuente)
- Medir lípidos (Soxhlet, hexano) y la densidad aparente a 8 % de humedad.
- Pedir al GIEM que confirme N = 0.418 % bs (la literatura da 2.3–2.8 %).
- Separar la radiación (ε ≈ 0.7, por validar) de h_c: con ε = 0.7, h_rad va de ≈26 W/m²K a 300 °C a ≈89 a 600 °C.
- Unificar h: legacy config.py y matlab/param.m usan 85; simulador_interactivo.py usa 90.
**Para la siguiente IA:**
- No usar las emisividades de NASA CR-1431 ni los datos de "Aouadja". Buscar TPRC Vol. 7 (Touloukian & DeWitt 1970) para AISI 304 oxidado.
- No mezclar la composición NREL (Ballesteros) con las fracciones CRECK de Choi 2020.
- Nada de esto cambió base.toml todavía: espera la aprobación de Nick y el subproyecto B.

### 2026-11-08 20:02 — Claude Opus 5.5 — HECHO
**Qué:** Plan de implementación del motor nuevo: 11 tareas con pruebas primero (ordenar repo, parámetros, malla, propiedades, conducción implícita con Bessel, cinética, horno/PID/SSR, simulador contra legacy, dt adaptativo y convergencia, lote y gráficas, verificación MATLAB).
**Archivos:** PyrolysisReactorCoffee, rama motor-nuevo: docs/plans/2026-11-08-motor-nuevo.md (commit a37bd5b).
**Fuentes:** Spec docs/specs/2026-11-08-motor-nuevo-design.md, aprobado por Nick.
**Verificado:** Auto-revisión del plan contra el spec (cobertura de las 8 pruebas, nombres e interfaces consistentes).
**Para Nick:** Abrir un chat nuevo en el Project "MacBook's Power" con el mensaje de arranque que dejó Claude, y correr ahí la implementación.
**Para la siguiente IA:** Implementar en la rama motor-nuevo siguiendo el plan tarea por tarea (executing-plans), en un chat nuevo. Cursor/Copilot sigue en espera hasta la Tarea 10.

### 2026-11-08 19:56 — Gemini — HECHO
**Qué:** Investigación bibliográfica con fuentes revisadas por pares de los 6 temas de datos del café (SCG) y del reactor que el modelo tenía como [Supuesto]: composición, análisis elemental y poder calorífico, propiedades del lecho, emisividad del AISI 304, TGA/DTG en N₂ y cinética de lípidos (TGL).
**Archivos:** Google Drive (Proyectos IA / horno-vertical): Investigación — datos del café y del reactor (https://docs.google.com/document/d/1V0surrX-eTDgg7Mrz_901qPwmTgXFKbSZSs947Y-8B8/edit).
**Fuentes:** 25+ artículos, manuales e informes con DOI/URL (lista completa en el Doc y en la copia de esta entrada en Drive).
**Verificado:** Según Gemini, todos los valores salen de tablas primarias; lo que no encontró quedó como "no encontrado".
**Para Nick:** Avisar a Claude para la revisión.
**Para la siguiente IA:** Revisar las 6 tablas. (Copiada al repo por Claude Opus 5.5 el 2026-11-08 20:54 desde la bitácora de Drive; ver la REVISIÓN de las 20:11.)

### 2026-11-08 19:55 — Claude Opus 5.5 — PROPUESTA
**Qué:** Spec del motor nuevo (subproyecto A): estructura ordenada del repo PyrolysisReactorCoffee (motor/, parametros/, legacy/…), módulos, paso dividido calor implícito + química, horno físico con PID y SSR, archivo de parámetros con unidad/etiqueta/fuente, interfaz pública y 8 pruebas de verificación con criterios.
**Archivos:** PyrolysisReactorCoffee, rama motor-nuevo: docs/specs/2026-11-08-motor-nuevo-design.md (commit 60b5c0f).
**Fuentes:** Decisiones de Nick en el chat (2026-11-08); legacy simulador_interactivo.py; reporte GIEM 28ago2604.
**Verificado:** Revisión propia del spec (sin huecos ni contradicciones); el código no existe todavía.
**Para Nick:** Leer el spec y aprobarlo o pedir cambios. Con la aprobación sigue el plan de implementación.
**Para la siguiente IA:** No implementar nada del motor hasta que Nick apruebe el spec. Cursor/Copilot sigue en espera.
✅ Aprobado por Nick — 2026-11-08 19:53

### 2026-11-08 19:36 — Claude Opus 5.5 — HECHO
**Qué:** Reglas del proyecto para ahorrar tokens (todas las IAs).
**Archivos:** proyectos/horno-vertical/CONTEXTO.md (sección "Cómo se trabaja").
**Fuentes:** depurador-recursos y selector-ia, revisión del 2026-11-08.
**Verificado:** n/a.
**Para Nick:** (1) Un chat por subproyecto: A motor, B calibración, C app; la Línea 2 (IA local) siempre aparte. (2) Cuando un chat se alargue (respuestas lentas, olvida cosas), cerrarlo con auditor-handover y abrir otro que arranque leyendo CONTEXTO.md. (3) Al abrir un chat, decir solo "trabajemos en horno-vertical, subproyecto X": la IA lee CONTEXTO y las últimas 5 entradas, no todo. (4) CSV, resultados y logs no se pegan en el chat: se dejan en la carpeta y la IA los lee. (5) Corridas pesadas en la Terminal de macOS; Claude solo prepara scripts. (6) Investigar → Gemini/Perplexity; código repetitivo de la app → Cursor/Copilot; Claude para física, numérica, revisión y verificación.
**Para la siguiente IA:** Respetar el reparto del punto 6. El estado vive en CONTEXTO.md, no en el doc del Project de claude.ai (cada cambio al doc rompe el caché de todos los chats).

### 2026-11-08 19:36 — Claude Opus 5.5 — PREGUNTA
**Qué:** Tarea para CURSOR o COPILOT (modelo Auto). EN ESPERA: no empezar todavía.
**Archivos:** Repo PyrolysisReactorCoffee, rama del motor nuevo (la crea Claude).
**Fuentes:** Spec del motor y de la app (los escribe Claude; Nick los aprueba).
**Verificado:** n/a.
**Para Nick:** Cuando Claude anuncie en esta bitácora que la interfaz del motor quedó fija, abrir el repo en Cursor/Copilot y pedirle: "Haz la tarea de Cursor de la bitácora horno-vertical".
**Para la siguiente IA:** CURSOR/COPILOT: construir las pantallas de la app Streamlit (entradas de parámetros, gráficas, carga del CSV del termopar) usando SOLO la interfaz pública del paquete motor/. No tocar la física, la numérica ni parametros.toml. Cada pantalla con su prueba. Al terminar, entrada HECHO en esta bitácora.

### 2026-11-08 19:36 — Claude Opus 5.5 — PREGUNTA
**Qué:** Tarea para PERPLEXITY (gratis, Pro Search si hay). Datos del controlador Max-Therma / MaxThermo MC-5438 del horno.
**Archivos:** ninguno (Perplexity no tiene acceso; Nick pega la respuesta en el chat de Claude).
**Fuentes:** Manual o ficha del fabricante primero; foros solo marcados como [Por validar].
**Verificado:** n/a (lo revisa Claude).
**Para Nick:** Pegar en Perplexity el bloque que dejó Claude en el chat y traer la respuesta al chat del motor/calibración.
**Para la siguiente IA:** PERPLEXITY: busca el manual del MC-5438 y responde en tabla con URL: tipo de salida para SSR (voltaje), tiempo de ciclo de la salida (valor por defecto y rango), parámetros PID y sus unidades (banda P en % o °C, I y D en s), rangos de cada uno, autotune (cómo funciona), programas de rampa/meseta (cuántos pasos), tipo de termopar aceptado y precisión. Cierra con tu entrada de bitácora en un bloque de código con el formato de CONTRATO.md §7.

### 2026-11-08 19:36 — Claude Opus 5.5 — PREGUNTA
**Qué:** Tarea para GEMINI (Deep Research, modelo Argon o Pro). Investigar con fuente los datos del café y del reactor que el modelo hoy tiene como [Supuesto].
**Archivos:** Gemini crea en Drive, carpeta Proyectos IA / horno-vertical, el Doc "Investigación — datos del café y del reactor".
**Fuentes:** Solo artículos revisados por pares, libros o fichas técnicas. Cada valor con autor, año, DOI o URL, tabla o página, y el método de medida.
**Verificado:** n/a (lo revisa Claude con una entrada REVISIÓN).
**Para Nick:** Abrir Gemini Deep Research, pegar el link de esta bitácora y decirle: "Haz la tarea de Gemini de la bitácora horno-vertical".
**Para la siguiente IA:** GEMINI: (1) Composición del residuo de café usado (spent coffee grounds) en base seca: celulosa, hemicelulosa, lignina (y si hay, ácido-soluble/insoluble), lípidos, proteína, extractivos. (2) Análisis elemental C, H, O, N y poder calorífico. (3) Propiedades del lecho de café molido: densidad aparente, porosidad, conductividad térmica efectiva y cp vs. temperatura. (4) Emisividad del acero inoxidable AISI 304 oxidado entre 300 y 600 °C. (5) TGA/DTG de residuo de café en N2 a 5–20 °C/min: temperaturas de pico, pérdida de masa por etapa, residuo a 600–700 °C. (6) Cinética de pirólisis de lípidos o aceite de café si existe. Entrega una tabla por tema: parámetro | valor | unidad | rango entre fuentes | fuente exacta | método. Si no encuentras algo, escribe "no encontrado"; no inventes ni redondees. Al terminar, escribe tu entrada HECHO arriba, debajo de "Entradas", con este mismo formato.

### 2026-11-08 19:33 — Claude Opus 5.5 — PREGUNTA
**Qué:** Datos que faltan para calibrar el modelo con el horno real.
**Archivos:** ninguno.
**Fuentes:** revisión de Max_Power/01_Horno_Vertical/datos/ (Mac de Nick).
**Verificado:** n/a.
**Para Nick:** (1) ¿"Café grano" del FTIR es el mismo residuo de tinto del reporte GIEM 28ago2604? (2) Masas de la corrida "Pirolizado 1-2": café cargado, biochar obtenido, rampa y T final. (3) Cualquier registro de temperatura de esa corrida. (4) Fuente de la composición celulosa/hemicelulosa/lignina/lípidos (12/35/28/15 %).
**Para la siguiente IA:** no tratar esa composición como dato del GIEM: el reporte no la trae.

### 2026-11-08 19:33 — Claude Opus 5.5 — HECHO
**Qué:** Se abre el proyecto. Modelo traído al Mac, corrida medida, barrido en paralelo probado, datos revisados y plan aprobado por Nick (A motor nuevo → B calibración térmica → C app Streamlit).
**Archivos:** proyectos/horno-vertical/CONTEXTO.md, BITACORA.md; en el Mac: Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee/ (copia del repo, commit ddb0a63) y modelos/barrido_paralelo.py.
**Fuentes:** repo nicolascalle8-glitch/PyrolysisReactorCoffee (docs/EVALUACION_CINETICAS.md); reporte GIEM 28ago2604 (7-sep-2026); FTIR muestras 013/014/015 (4-sep-2026).
**Verificado:** caso base (10 °C/min, 500 °C, 30 min, 8 % humedad) corrido en la VM del Mac: 25 s, biochar 24.93 %, bio-oil 38.94 %, gas 20.23 %, agua 15.90 %, balance 100.000 % (igual al informe). Barrido demo 4 casos con 4 procesos: x3.1.
**Para Nick:** nada (el plan ya lo aprobó en el chat).
**Para la siguiente IA:** la shell de Claude en el Mac es una VM Linux de 4 núcleos y ~3 GB; las corridas grandes van en la Terminal de macOS. El GIEM solo reporta humedad 61.2 % bh, cenizas 2.31 % bs, pérdida por calcinación 650 °C 97.7 % bs, CO 49.4 % bs, N 0.418 % bs, C/N 118.2.

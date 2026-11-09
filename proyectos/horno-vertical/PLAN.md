# PLAN — Horno vertical: puesta a punto del reactor

Actualizado: 2026-11-09 (Bogotá). Este archivo es lo único que hay que leer para trabajar en el horno. Si algo no está aquí, no está decidido.

## Qué es el proyecto

**Etapa 1 (ahora): poner a punto el reactor vertical de lecho fijo del GIEM.** Medir cómo se comporta el horno, calibrar el modelo 2D con esas medidas y sintonizar el PID para que el horno siga la rampa que se le pida.

**Etapa 2 (después): pirólisis catalítica con zeolitas**, que es el objetivo de la propuesta I+D ("evaluar la eficiencia de las zeolitas jerárquicas en la pirólisis catalítica de residuos de café"). No arranca hasta cerrar la etapa 1.

Por qué en ese orden: para decir que la zeolita cambió el bio-oil hay que comparar corridas con y sin catalizador que tengan la misma historia térmica, y esa historia hay que conocerla y controlarla. Eso es la etapa 1. (Decisión de Nick, 2026-11-09.)

## Reglas de trabajo

1. **Una sola fuente de verdad:** este PLAN.md. Un chat nuevo lee esto y las últimas 3 entradas de BITACORA.md. Nada más.
2. **Un solo chat de IA en el horno a la vez.** Antes de abrir otro, se cierra el anterior.
3. **Solo se trabaja en el paso marcado AHORA.** La IA no adelanta pasos ni abre trabajo nuevo sin pedido de Nick.
4. **Software congelado hasta tener la corrida 1 real.** Nada de app, refactors ni mejoras mientras tanto.
5. **Antes de aprobar algo, tres preguntas:** ¿acerca al objetivo? ¿con qué dato real se valida? ¿qué se rompe si está mal?
6. **Bitácora corta:** una entrada por sesión, 3 líneas (hecho / verificado / sigue). Solo en GitHub. En Drive no hay copias, solo un LÉEME con el link.
7. Cada número con su fuente y su etiqueta ([Dato], [Supuesto], [Por validar], [Calculado]). Borrar, mover, unir a main o cambiar una decisión: solo con aprobación de Nick.

## Pasos en orden

Estado: ✅ hecho · ▶ AHORA · ⏳ después

### Etapa 1 — Reactor

| # | Paso | Dueño | Entregable | Estado |
|---|---|---|---|---|
| 0 | Motor 2D (A) y software de calibración (B), probados con datos sintéticos | IA | `main` (ed907cf) y rama `ensayo-termico` (563cc20) | ✅ |
| 1 | **Conocer el equipo:** foto de la placa del horno y de la etiqueta del controlador (código MC-5438-BCD-EFG). En el equipo: cómo entrar a manual y fijar la salida (OutL), si el nivel PROG está abierto, la unidad de P1 y dónde está físicamente el termopar de control | Nick | Fotos y respuestas en la bitácora | ▶ AHORA |
| 2 | **Conseguir instrumentos:** 3 termopares tipo K con vaina, registrador a 1 s y adaptador USB–RS-485 (si el código trae G = 2) | Nick / GIEM | Lista de lo que hay y lo que falta | ▶ AHORA (en paralelo con 1) |
| 3 | **Datos de la carga:** humedad real del café que entra al horno (el GIEM midió 61.2 % bh [Dato]; el modelo usa 8–15 % [Supuesto]). Masa cargada, biochar, rampa y T final de "Pirolizado 1-2". ¿"Café grano" es el mismo residuo del reporte GIEM? | Nick | Respuestas en la bitácora | ▶ AHORA (en paralelo con 1) |
| 4 | **Corrida 1, tubo vacío.** Arrancar con tubo y horno a la misma temperatura (diferencia < 5 K). Termopares: aire del horno, pared externa del tubo (z = 0.10 m). Registrar la salida del SSR. CSV a 1 s con columnas `t_s, T_horno_C, T_pared_C, T_centro_C, T_control_C, T_set_C, u_ssr_pct, T_amb_C` en `01_Horno_Vertical/datos/ensayo_termico/` | Nick | CSV de la corrida 1 | ⏳ |
| 5 | **Ajuste de la corrida 1:** `calibracion/ajuste_termico.py` → C_h, UA_p, h_c, ε. Cierra si RMS T_pared ≤ 5 K y RMS T_horno ≤ 5 K. Si cierra, Nick decide unir `ensayo-termico` a `main` | IA | Valores calibrados con su rango | ⏳ |
| 6 | **Corrida 2, con café** (10 °C/min, 500 °C, 30 min, enfriamiento libre), con termopar también en el centro del lecho. Ajuste → k_virgen_0, k_char_0, R_contacto. Cierra con la decisión 9 | Nick, luego IA | CSV + valores calibrados | ⏳ |
| 7 | **Sintonizar el PID** con el modelo calibrado (Python), verificar en MATLAB/Simulink y probar en el horno. El criterio de "sigue bien la rampa" se fija con Nick al llegar aquí | IA, luego Nick | Kp, Ki, Kd probados en el horno | ⏳ |
| 8 | **Corrida de validación** a 20 °C/min que no se usa para ajustar | Nick | CSV + comparación modelo vs medida | ⏳ |

**La etapa 1 cierra** cuando el modelo reproduce la corrida 8 y el PID sigue la rampa en el horno real.

### Etapa 2 — Zeolitas (no arrancar antes de cerrar la etapa 1)

| # | Paso | Dueño |
|---|---|---|
| 9 | Definir con el GIEM y el tutor: catalizador in-situ (mezclado) o ex-situ (lecho aparte), zeolita (Y o ZSM-5 jerárquica), relación catalizador/biomasa, temperatura del lecho catalítico, cómo y dónde se analiza el bio-oil | Nick |
| 10 | Agregar al modelo solo lo que pida el paso 9 (por ejemplo, lecho de catalizador, temperatura y tiempo de residencia de los vapores) | IA |
| 11 | Corridas con y sin zeolita con la misma receta térmica | Nick |

**En pausa:** la app Streamlit (antes "subproyecto C"). Se retoma solo si después del paso 7 hace falta.

## Decisiones vigentes (no reabrir)

1. Orden: etapa 1 (reactor) → etapa 2 (zeolitas). Dentro de la etapa 1: motor → calibración con datos reales → PID. (Nick, 2026-11-09)
2. Numérica: paso dividido, conducción implícita (solver de banda) + química exacta por nodo, dt adaptativo. Verificada con Bessel, MATLAB y convergencia.
3. Horno modelado como el real: masa térmica, P_max, PID → SSR, pérdidas, intercambio horno–tubo y termopar con retardo.
4. El PID se sintoniza en Python; MATLAB/Simulink verifica y sirve para el microcontrolador.
5. Los datos del GIEM y del FTIR no se suben a GitHub (el repo PyrolysisReactorCoffee es público).
6. Composición: celulosa 12.4 y lignina 23.9 % bs (Ballesteros 2014). R_contacto_extra = 0.011 m²K/W hasta calibrarlo.
7. Corrida en vacío con un modelo 0D del tubo en `calibracion/`; corrida con café con `horno.modo = "medido"`.
8. **Criterio de cierre de la calibración (decisión 9):** RMS T_pared ≤ 5 K (las dos corridas); RMS T_horno ≤ 5 K (corrida 1); RMS T_centro ≤ 10 K fuera de la pirólisis y ≤ 20 K en ella.
9. Un solo chat de IA en el horno a la vez; app en pausa; documentos: solo PLAN.md + BITACORA.md corta. (Nick, 2026-11-09)

## Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Código | github.com/nicolascalle8-glitch/PyrolysisReactorCoffee: `main` = motor; `ensayo-termico` = calibración (sin unir) |
| Carpeta de trabajo en el Mac | `~/Developer/Max_Power/01_Horno_Vertical/` (datos/, modelos/, resultados/). La copia `01_Horno_Vertical_VIEJO_iCloud` no se usa |
| Corridas pesadas | Terminal de macOS con `modelos/PyrolysisReactorCoffee/.venv/bin/python` |
| Fichas técnicas | `archivos/` (controlador MC-5438, datos del café, caso base y barrido) |
| Manuales del MC-5438 | Drive: Proyectos IA / horno-vertical / investigaciones |
| Historial hasta 2026-11-09 | `archivo/` (CONTEXTO, HANDOVER y bitácora larga). Solo si Nick pregunta por el pasado |

## Hechos que se necesitan para los pasos 4 y 5

- Geometría base [Supuesto]: R_lecho 25 mm, acero 2.5 mm, L 0.20 m. Hay que medir la real antes del paso 5.
- Con los valores de arranque (P_max 2500 W, C_h 20000 J/K, ambos [Por validar]) el horno no alcanza 10 °C/min: P_max/C_h = 7.5 K/min [Calculado]. La corrida 1 dice si es así.
- Tubo de acero ≈ 326 J/K y τ ≈ 105 s, o sea ≈ 17 K de retraso a 10 °C/min [Calculado].
- Controlador MC-5438: el manual no documenta el paso a paso del modo manual (OutL), ni la unidad de P1, ni los códigos Modbus. Por eso el paso 1 es en el equipo.

## Pendientes menores del software (no tocar antes del paso 5)

- No existe el paso de los valores calibrados a `base.toml`, y la etiqueta "Calibrado" no es válida (usar "Medido").
- `leer_ensayo` falla con BOM o con texto en columnas no requeridas. Revisar con el primer CSV real.
- Si ε no es significativa, el spec pide reajustar con ε = 0.
- El informe no trae el estado del optimizador. `calibracion/README.md` está viejo.
- Las sigmas del ajuste son optimistas (el error real fue 6–8 veces la sigma en el sintético).

## Preguntas abiertas (se resuelven con datos reales)

- ¿Dónde está el termopar de control? El modelo lo pone en la cara externa del tubo.
- La rampa casi no cambia los rendimientos en el modelo (< 0.5 pp). Contrastar con la corrida 8.
- ¿Hace falta el craqueo de alquitranes en fase gas? Solo se sabe midiendo el bio-oil.

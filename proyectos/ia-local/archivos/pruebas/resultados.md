# Resultados de modelos locales

Detalle de cada corrida y respuestas completas en los archivos con fecha de esta carpeta.

## Velocidad

Mac en uso normal (no en reposo). LM Studio 0.4.28, motor mlx-llm 1.14.0.

| Fecha | Modelo | Cuantización | Motor | Contexto | tok/s | Primera palabra, prompt corto | Primera palabra, 6801 tokens de entrada | Carga | Memoria |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-08 | Qwen 3.6-27B | 4 bits | MLX | 16384 | 26.0–28.6 | ~0.5 s | 28–31 s | 19.8 s en frío, 7.9 s después | 14.98 GiB (modelo, según LM Studio) |

La memoria extra del sistema medida con vm_stat dio 13.1 GB en una corrida y 23.5 GB en otra. Esa cifra incluye al resto del Mac, así que es solo orientativa.

## Calidad: Qwen 3.6-27B

Corrida de 2026-11-08_2108, límite de 4096 tokens. Las 4 respuestas terminaron solas. Son solo 4 prompts: sirve de primera impresión, no de veredicto.

Tiempo real por respuesta: 1 a 2.4 minutos. Entre 46 % y 79 % del texto generado es razonamiento previo, en inglés. La respuesta final sale en español.

| Prompt | Tokens | Juicio | Qué se comprobó |
|---|---|---|---|
| explicar_codigo | 1763 | Bien | Encontró el índice fuera de rango y dio tres correcciones válidas. |
| razonar_fisica | 3337 | Bien, con reparos | T = 477.46 N·m y J correctos. 38.0 MPa correcto. La cifra exacta que da (38 000 745 Pa) no lo es: son 37 995 444 Pa. Dice "diseño seguro" comparando esfuerzo cortante con fluencia a tensión (~250 MPa), sin usar la fluencia en cortante (~0.577·Sy ≈ 144 MPa), concentradores ni fatiga. |
| escribir_codigo | 3825 | Núcleo bien, ejemplo con fallos | Ver abajo. |
| contexto_largo | 3819 | Análisis bien, un fallo grave | Encontró bien el patrón (factor y divisor) y `paso(n, t, q)` da el valor correcto. Las funciones `paso_i` generadas con lambda son incorrectas (ver abajo). |

### Fallos encontrados

1. **contexto_largo, bug comprobado al ejecutarlo.** El lazo `lambda t, q=i: paso(i, t, q)` hace que todas las funciones usen `i = 149`. `paso_5(100)` da 102.34; el original da 88.71. El propio modelo había dicho riesgo de errores "cero". También dice ~450 líneas y son 600.
2. **escribir_codigo, tiempo final.** Por redondeo, `dt = 125.00000000000001` y `nt` queda en 8: el ejemplo se detiene en 875 s, no en los 1000 s pedidos. Comprobado con la misma aritmética.
3. **escribir_codigo, gráfica.** `contourf(X, T_surf, T_history.T)` usa la matriz traspuesta: X es (8, 21) y Z sería (21, 8). Debería fallar. No se ejecutó, porque este Python no tiene numpy ni matplotlib.
4. **escribir_codigo, redacción.** Dice "incondicionalmente inestable si r > 0.5". La expresión correcta es "condicionalmente estable: requiere r ≤ 0.5".

El esquema numérico sí está bien: traducido sin numpy, con 8 pasos hasta 1000 s, queda a menos de 2.3 °C de la solución analítica de medio semi-infinito en los primeros 9 nodos, con una malla gruesa.

## Conexión a VS Code (2026-11-08)

VS Code 1.145.2, proveedor integrado Custom Endpoint, contexto 32768 (entrada 24576 + salida 8192).

| Comprobación | Estado |
|---|---|
| El servidor acepta una petición tipo VS Code (streaming y herramientas) | Bien: llamó a `read_file` correctamente en 5.0 s |
| El modelo aparece en el selector de VS Code | Bien, en modo **Local**, pestaña "LM Studio (local)" |
| Responde dentro del chat de VS Code | Bien: el registro de LM Studio muestra 3 peticiones de `qwen3.6-27b-mlx`, sin errores |
| Tiempo de la primera respuesta real | ~3 min 10 s para explicar un archivo de 31 líneas (primera petición: 114 s) |

El chat venía en modo Copilot, donde el modelo local no aparece. Hay que usar el modo Local (abajo, en el panel de chat) y elegir "L3-37 (local)", el nombre visible de Qwen 3.6-27B desde el 9 nov. Comprobar que el selector lo muestre: en Auto responde Copilot, no Qwen.

No es 100 % local: aun con Qwen elegido, VS Code generó el título de la conversación con `gpt-4o-mini` en la nube de Copilot.

### Conclusión provisional

Sirve para explicar código y razonar física. El código que genera hay que probarlo siempre antes de usarlo: 2 de las 2 respuestas que escribieron código nuevo extenso traían algún fallo.

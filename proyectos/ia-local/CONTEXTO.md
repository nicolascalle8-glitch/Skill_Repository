# CONTEXTO — IA local en el M4 Max (Línea 2 de Max_Power)

Actualizado: 2026-11-08 21:40 (Bogotá). Lee solo esto para arrancar. Reglas: CONTRATO.md del repo.

## En una frase
Montar y usar modelos de IA locales en el MacBook Pro M4 Max de Nick. Complementa a Gemini y a Cursor/Copilot, no los reemplaza. El horno vertical es otra línea (`horno-vertical`): no mezclar.

## Tu siguiente tarea
Objetivo 3: tutor local que busque en los PDF y apuntes de Nick (Çengel, Shigley, Mott, clases) y explique con el porqué físico. Antes de instalar o descargar algo, decirle a Nick qué es, cuánto pesa y dónde queda, y esperar su sí.

## Hechos clave
Todo medido en el Mac de Nick el 2026-11-08, con el Mac en uso normal. Detalle en `archivos/pruebas/resultados.md`.

- Equipo: M4 Max, 48 GB, macOS 27.0.1. Límite de GPU por defecto.
- Servidor: LM Studio 0.4.28, motor mlx-llm 1.14.0, puerto 1234.
- Modelo: Qwen 3.6-27B, MLX, 4 bits. Clave `qwen3.6-27b-mlx`, 16.08 GB, SHA-256 verificado contra Hugging Face.
- Velocidad: 26.0–28.6 tok/s. Primera palabra ~0.5 s (28–31 s con 6801 tokens de entrada). Carga 7.9–19.8 s. Memoria 14.98 GiB.
- Calidad, 4 prompts: explica y razona bien. El código nuevo que escribió traía fallos (detalle en resultados.md), así que siempre hay que probarlo.
- VS Code 1.145.2: conectado con el proveedor Custom Endpoint. Comprobado en el registro de LM Studio.

## Cómo se usa
1. Correr `archivos/config/encender_qwen.sh` (en el Mac está en `Max_Power/02_IA_Local/config/`).
2. En el chat de VS Code: modo **Local** y modelo **Qwen 3.6-27B (local)**. Si el selector dice Auto, responde Copilot.
3. Al terminar: `~/.lmstudio/bin/lms unload --all && ~/.lmstudio/bin/lms server stop`.

## Decisiones vigentes (no reabrir)
- LM Studio como servidor, con Qwen 3.6-27B como primer modelo — Nick dijo sí el 2026-11-08.
- El modelo local va en VS Code. Antigravity sigue con sus modelos en la nube — Nick eligió VS Code el 2026-11-08.

## Restricciones
- Nada de sudo ni cambios del sistema (como `iogpu.wired_limit_mb`) sin explicar el riesgo y pedir permiso.
- Medir de verdad y anotar en `pruebas/`: modelo, cuantización, motor, contexto, tok/s, tiempo al primer token, memoria y fecha.
- Explicarle cada paso a Nick: está aprendiendo esta parte.
- Tras cada cambio, actualizar este repo y la carpeta de Drive `Proyectos IA / ia-local` (orden de Nick).

## Limitaciones conocidas
- En VS Code es lento: una respuesta real tardó ~3 min, por las instrucciones largas que añade el editor.
- No es 100 % local: VS Code genera el título del chat con `gpt-4o-mini` en la nube de Copilot.
- Según la documentación de VS Code, los modelos locales no sirven para el autocompletado.
- En el Mac el modelo se ve por `~/.lmstudio/models/nick/Qwen3.6-27B-4bit-MLX`, con enlaces a `mlx-community/Qwen3.6-27B-4bit`. La descarga original quedó trabada en LM Studio y no se indexaba.

## Pendientes abiertos
- [ ] Objetivo 3: tutor local con los PDF y apuntes — siguiente.
- [ ] Objetivo 4: tareas en lote (comentar código, borradores de talleres, Whisper).
- [ ] Medir los otros candidatos si hacen falta: Qwen 3.6-35B-A3B (20.4 GB), DeepSeek-R1-Distill-32B (18.4 GB), Gemma 4 26B-A4B (15.4 GB).
- [ ] Ubicar `lineas/02-ia-local.md`: el BRIEF dice que manda sobre él, pero no está en el repo ni en Drive — Nick.

## Dónde están las cosas
- Repo: `proyectos/ia-local/` (CONTEXTO, BITACORA, `archivos/`).
- Drive: `Proyectos IA / ia-local`, con ids en `registry/DRIVE.yml`.
- Mac: `Max_Power/02_IA_Local/` (BRIEF, CLAUDE.md, `config/`, `pruebas/`).

## Criterio de cierre
- [x] Servidor instalado y primer modelo medido.
- [x] Modelo de programación conectado a VS Code.
- [ ] Tutor local responde con base en los PDF y citando la fuente.
- [ ] Tareas en lote funcionando, medidas y anotadas.

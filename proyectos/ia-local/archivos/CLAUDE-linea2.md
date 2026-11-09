# CLAUDE.md — Línea 2: IA local en el M4 Max

Esta carpeta es SOLO para montar y usar modelos de IA locales en el MacBook Pro M4 Max.
Lee primero `BRIEF.md` (objetivo, lo que se sabe, candidatos y primer paso).
Si el BRIEF y el doc del proyecto (lineas/02-ia-local.md) no coinciden, manda el del proyecto.

## Quién soy
Nick, estudiante de último semestre de Ingeniería Mecánica (EIA, Medellín).
Estoy aprendiendo esta parte (servidores de modelos, terminal, Python), así que:
- Escríbeme en español simple y directo; términos técnicos y código pueden ir en inglés.
- Explica cada paso: qué hace el comando, por qué, y qué debería salir.
- El código va comentado, con cómo correrlo.

## Reglas
1. **Nada del horno.** El horno vertical va en `../01_Horno_Vertical` (Línea 1). No leer, no tocar, no mezclar.
2. **Trabaja solo dentro de esta carpeta.** Las apps y los modelos van donde cada programa los pone,
   pero avísame la ruta antes.
3. **Antes de instalar o descargar algo**, dime qué es, cuánto pesa y dónde queda. Espera mi sí.
   Los modelos pesan 15–20 GB cada uno; revisa el disco libre antes.
4. **Nada de sudo ni cambios del sistema** (por ejemplo subir `iogpu.wired_limit_mb`) sin explicarme
   el riesgo y pedirme permiso.
5. **Medir de verdad.** Las velocidades del BRIEF son publicadas; anota las reales en `pruebas/`
   (modelo, cuantización, motor MLX/GGUF, tamaño de contexto, tok/s de generación, tiempo al primer token,
   memoria usada, fecha). Un archivo por prueba o una tabla en `pruebas/resultados.md`.
6. **Configuración en `config/`**: scripts, ajustes del servidor y del editor (VS Code / Antigravity).
7. **Siempre compartir con Claude chat y Gemini (orden de Nick, 8 nov 2026).** Ninguna IA recuerda lo que hizo otra.
   Cada vez que cambie algo de esta línea, al terminar hay que actualizar la memoria compartida:
   - GitHub, repo `nicolascalle8-glitch/Skill_Repository`: `proyectos/ia-local/` (CONTEXTO, BITACORA y archivos).
   - Google Drive: `Proyectos IA / ia-local` (bitácora con la entrada idéntica a la de GitHub, y copias de los documentos).
   El cómo está en la skill `colaboracion-ias` y en `shared/BITACORA-DRIVE.md` del repo. Antes de empezar, leer lo que hayan dejado las otras IAs.

## Carpetas
- `BRIEF.md` — copia del brief de la línea
- `config/` — configuración y scripts
  - `revisar_mac.sh` revisa qué hay instalado (solo lee) y escribe `pruebas/00_inventario.txt`
  - `medir_modelo.py` mide un modelo de LM Studio con prompts fijos (carga, TTFT, tok/s, memoria)
  - `encender_qwen.sh` enciende el servidor y carga Qwen para usarlo en VS Code
  - `vscode_chatLanguageModels.json` copia de la configuración del modelo local en VS Code
- `pruebas/` — mediciones de velocidad y calidad; el resumen está en `pruebas/resultados.md`

## Estado (8 nov 2026, 21:40)
- macOS 27.0.1, M4 Max, 48 GB, límite GPU por defecto (`iogpu.wired_limit_mb` = 0). Disco libre: ~744 GB.
- Homebrew instalado. Python 3.13 (python.org), sin MLX, torch, numpy ni Whisper.
- LM Studio 0.4.28 instalado, motor mlx-llm 1.14.0. Ollama no instalado.
- Modelo: Qwen 3.6-27B MLX 4 bits (`qwen3.6-27b-mlx`), 16.08 GB, verificado con SHA-256.
  Vive en `~/.lmstudio/models/nick/Qwen3.6-27B-4bit-MLX`, con enlaces a `mlx-community/Qwen3.6-27B-4bit`.
  La entrada `nick/` se creó porque la descarga original quedó trabada en LM Studio y no se indexaba.
- Medido: 26–28 tok/s, primera palabra ~0.5 s (28–31 s con 6801 tokens de entrada), 14.98 GiB.
- Calidad (4 prompts): explica y razona bien; su código nuevo hay que probarlo siempre.
- VS Code conectado (Custom Endpoint) y comprobado en el registro de LM Studio.
  Para usarlo: correr `config/encender_qwen.sh`, poner el chat en modo **Local** y elegir **Qwen 3.6-27B (local)**.
  Si el selector dice Auto, responde Copilot. Una respuesta real tardó ~3 min. Los títulos del chat siguen yendo a la nube de Copilot.
- Antigravity IDE: sin soporte oficial confirmado para modelos locales; se deja con sus modelos en la nube.

## Por dónde seguir
1. Hecho: inventario, instalación, medición de Qwen 27B y conexión a VS Code.
2. Medir los otros candidatos del BRIEF si hacen falta (cada uno pesa 15–20 GB: pedir permiso antes).
3. Objetivo 3: tutor local con los PDF y apuntes de Nick.
4. Objetivo 4: tareas largas en lote.

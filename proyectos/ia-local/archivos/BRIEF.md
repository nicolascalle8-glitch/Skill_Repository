# Línea 2 — IA local en el M4 Max

Solo para montar y usar modelos de IA locales. El horno va en la otra línea (01_Horno_Vertical). No mezclar.
Copia del doc del proyecto: lineas/02-ia-local.md (si cambian, manda el del proyecto).
Carpeta de trabajo: ~/Documents/Documents - MacBook Pro de Nicolas/Max_Power/02_IA_Local

## Objetivo
1. Instalar un servidor de modelos locales (LM Studio y/o Ollama con soporte MLX) y medir la velocidad real en el Mac.
2. Dejar un modelo de programación conectado a VS Code / Antigravity para explicar, comentar y probar código sin límite de uso.
3. Después: un tutor local que busque en los PDF y apuntes de Nick (Çengel, Shigley, Mott, clases) y explique con el porqué físico.
4. Después: tareas largas en lote (comentar código, generar borradores de talleres, transcribir asesorías con Whisper).

## Lo que se sabe
- Mac: M4 Max, 16 CPU, 40 GPU, 48 GB de memoria unificada, ~546 GB/s.
- macOS deja a la GPU unos ~36 GB (75 %) por defecto; se puede subir, pero no hace falta para modelos de ~20 GB.
- Candidatos (velocidades publicadas, falta medirlas):
  - Qwen 3.6-35B-A3B (MoE, 4 bits, ~20 GB, ~35–55 tok/s): uso general
  - Qwen 3.6-27B (denso, 4 bits, ~17 GB, ~18–28 tok/s): programar
  - Gemma 4 26B-A4B (~15 GB, ~30–45 tok/s): contexto largo
  - DeepSeek-R1-Distill-32B (~20 GB): razonamiento y matemáticas
- Modelos de 70B o más no caben bien.
- No reemplaza a Gemini ni a Cursor/Copilot; los complementa.

## Reglas
- Antes de instalar o descargar algo (son archivos de 15–20 GB), decir qué y cuánto pesa.
- Medir y anotar los resultados reales en pruebas/.
- Explicar cada paso, porque Nick está aprendiendo esta parte.

## Carpetas
- config/ — configuración del servidor y del editor
- pruebas/ — mediciones de velocidad y calidad

## Primer paso (hecho el 8 nov 2026)
Revisar qué hay instalado en el Mac (Homebrew, Python, LM Studio, Ollama), proponer la instalación y medir el primer modelo.

## Estado (8 nov 2026)
- Objetivos 1 y 2 cumplidos: LM Studio con Qwen 3.6-27B (MLX, 4 bits) medido a 26–28 tok/s y conectado a VS Code.
- Sigue el objetivo 3 (tutor local). Detalle en `CLAUDE.md` y `pruebas/resultados.md`.
- Compartido con Claude chat y Gemini: repo Skill_Repository, `proyectos/ia-local/`, y Drive, `Proyectos IA / ia-local`.

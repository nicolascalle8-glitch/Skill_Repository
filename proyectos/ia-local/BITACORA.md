# BITÁCORA — IA local en el M4 Max

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra.

## En curso
<!-- una línea por tarea abierta: IA — qué — desde AAAA-MM-DD HH:MM -->
- (nada)

## Propuestas sin respuesta
<!-- enlace corto a cada PROPUESTA que espera a Nick -->
- (ninguna)

---

## Entradas

### 2026-11-09 08:10 — Claude Opus 5.5 — HECHO
**Qué:** La IA local ahora se llama L3-37 en VS Code, por pedido de Nick: es la droide de Star Wars cuya mente queda en la computadora del Halcón Milenario, y sigue la serie de sus equipos. El modelo sigue siendo Qwen 3.6-27B.
**Archivos:** proyectos/ia-local/CONTEXTO.md y archivos/ (config/vscode_chatLanguageModels.json, config/encender_qwen.sh, CLAUDE-linea2.md, pruebas/resultados.md).
**Fuentes:** pedido de Nick en el chat; la referencia a L3-37 viene de la película Solo (2018).
**Verificado:** JSON válido y copiado a la configuración real de VS Code; sintaxis del script revisada con bash -n. No verificado en pantalla: VS Code estaba en otro escritorio y la captura no mostraba cambios recientes.
**Para Nick:** revisar que el selector de VS Code diga L3-37 (local), reiniciando VS Code si no cambia; y decir si el proyecto también cambia de nombre (sigue como ia-local).
**Para la siguiente IA:** L3-37 es solo el nombre visible. La clave técnica sigue siendo qwen3.6-27b-mlx y el grupo LM Studio (local) no se renombró, porque VS Code los usa para identificar el modelo.

### 2026-11-08 21:40 — Claude Opus 5.5 — HECHO
**Qué:** Se crea el proyecto ia-local en el repo y en Drive. Quedan instalado LM Studio, medido Qwen 3.6-27B (26–28 tok/s) y conectado a VS Code, y compartidos los documentos con Claude chat y Gemini.
**Archivos:** proyectos/ia-local/CONTEXTO.md, BITACORA.md y archivos/ (BRIEF, CLAUDE-linea2, config, pruebas); proyectos/README.md; registry/DRIVE.yml.
**Fuentes:** mediciones propias en archivos/pruebas/; tamaños y SHA-256 de Hugging Face (mlx-community/Qwen3.6-27B-4bit); documentación de VS Code sobre modelos personalizados.
**Verificado:** SHA-256 de los 3 archivos del modelo contra Hugging Face. El registro de LM Studio muestra las peticiones de VS Code a qwen3.6-27b-mlx sin errores. El código del modelo se probó solo en parte, porque este Python no tiene numpy ni matplotlib.
**Para Nick:** confirmar el nombre ia-local, y decir dónde está lineas/02-ia-local.md (no aparece en el repo ni en Drive).
**Para la siguiente IA:** sigue el objetivo 3, el tutor local. En VS Code hay que usar el modo Local y comprobar que el selector diga Qwen; en Auto responde Copilot. Antes de descargar algo, pedirle permiso a Nick.

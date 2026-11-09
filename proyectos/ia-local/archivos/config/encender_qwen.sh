#!/bin/bash
# encender_qwen.sh - Linea 2 (IA local)
# Que hace: enciende el servidor de LM Studio y carga Qwen 3.6-27B para usarlo en VS Code.
# Ocupa unos 15 GB de memoria hasta que lo apagues.
#
# Como correrlo (en Terminal):
#   bash ~/Documents/"Documents - MacBook Pro de Nicolas"/Max_Power/02_IA_Local/config/encender_qwen.sh
# Para apagarlo y liberar la memoria:
#   ~/.lmstudio/bin/lms unload --all && ~/.lmstudio/bin/lms server stop
# Que deberia salir: "Listo" y una tabla con el modelo en estado IDLE.

set -e
LMS="$HOME/.lmstudio/bin/lms"
MODELO="qwen3.6-27b-mlx"

# El contexto es cuanto texto cabe en la conversacion. Debe ser igual o mayor que
# maxInputTokens + maxOutputTokens de vscode_chatLanguageModels.json (24576 + 8192).
CONTEXTO=32768

# 1) Enciende el servidor local en el puerto 1234 (solo si esta apagado)
"$LMS" server start

# 2) Carga el modelo solo si no esta ya en memoria, usando toda la GPU
if ! "$LMS" ps --json | grep -q "\"$MODELO\""; then
  "$LMS" load "$MODELO" --gpu max --context-length "$CONTEXTO" -y
fi

# 3) Muestra el estado final
"$LMS" ps
echo "Listo. En VS Code elige 'Qwen 3.6-27B (local)' en el selector de modelos del chat."

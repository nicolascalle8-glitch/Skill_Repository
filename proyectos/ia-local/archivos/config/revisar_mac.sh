#!/bin/bash
# revisar_mac.sh — Línea 2 (IA local)
# Qué hace: SOLO LEE el estado del Mac (no instala ni borra nada) y guarda
# el resultado en pruebas/00_inventario.txt para que Claude lo lea.
# Cómo correrlo: abre Terminal y pega:
#   bash ~/Documents/"Documents - MacBook Pro de Nicolas"/Max_Power/02_IA_Local/config/revisar_mac.sh

BASE="$HOME/Documents/Documents - MacBook Pro de Nicolas/Max_Power/02_IA_Local"
OUT="$BASE/pruebas/00_inventario.txt"

{
echo "=== Fecha"; date

# 1) Equipo: chip, memoria, versión de macOS
echo; echo "=== Equipo"
sw_vers
sysctl -n machdep.cpu.brand_string
echo "Memoria (GB): $(( $(sysctl -n hw.memsize) / 1073741824 ))"
# Límite de memoria para la GPU (0 = valor por defecto de macOS, ~75 %)
echo "iogpu.wired_limit_mb: $(sysctl -n iogpu.wired_limit_mb 2>/dev/null || echo 'n/a')"

# 2) Espacio en disco: cada modelo pesa 15-20 GB
echo; echo "=== Disco libre"
df -h / | tail -1

# 3) Homebrew (gestor de paquetes de macOS)
echo; echo "=== Homebrew"
if command -v brew >/dev/null; then brew --version | head -1; brew list --formula 2>/dev/null | tr '\n' ' '; echo; else echo "NO instalado"; fi

# 4) Python y librerías de IA para Apple (MLX)
echo; echo "=== Python"
for p in python3 python3.12 python3.11 python3.13; do command -v $p >/dev/null && echo "$p -> $(command -v $p) $($p --version 2>&1)"; done
python3 -m pip list 2>/dev/null | grep -iE "mlx|torch|whisper|transformers" || echo "sin mlx/torch/whisper"

# 5) Servidores de modelos locales
echo; echo "=== LM Studio"
ls -d /Applications/LM\ Studio.app 2>/dev/null || echo "app NO instalada"
[ -d "$HOME/.lmstudio" ] && { echo "carpeta ~/.lmstudio existe"; du -sh "$HOME/.lmstudio/models" 2>/dev/null; }
command -v lms >/dev/null && lms ls 2>/dev/null
echo; echo "=== Ollama"
ls -d /Applications/Ollama.app 2>/dev/null || echo "app NO instalada"
command -v ollama >/dev/null && { ollama --version; ollama list 2>/dev/null; }

# 6) Editores donde se conectará el modelo
echo; echo "=== Editores"
ls -d "/Applications/Visual Studio Code.app" /Applications/Antigravity*.app /Applications/Cursor.app 2>/dev/null
command -v code >/dev/null && code --list-extensions 2>/dev/null | grep -iE "continue|cline|copilot|roo" 
} > "$OUT" 2>&1

echo "Listo. Resultado guardado en: $OUT"

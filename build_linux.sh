#!/bin/bash
# Stealth Clicker Pro - Linux Application Builder
set -e

cd "$(dirname "$0")"

echo "========================================================"
echo "   Stealth Clicker Pro - Building Linux Application"
echo "========================================================"

python3 scripts/build_app.py

if [ -f "dist/StealthClickerPro" ]; then
    chmod +x dist/StealthClickerPro
    echo ""
    echo "[✓] Executable compiled successfully at dist/StealthClickerPro"
    echo "[i] To install desktop shortcut, run: ./scripts/install_linux.sh"
fi

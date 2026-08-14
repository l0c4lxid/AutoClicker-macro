#!/bin/bash
# Stealth Clicker Pro - Linux Desktop Launcher Installer
set -e

cd "$(dirname "$0")"

BIN_SRC="dist/StealthClickerPro"
if [ ! -f "$BIN_SRC" ]; then
    echo "[!] Binary dist/StealthClickerPro not found. Building now..."
    python3 build_app.py
fi

INSTALL_DIR="$HOME/.local/bin"
APP_DIR="$HOME/.local/share/applications"
ICON_DIR="$HOME/.local/share/icons"

mkdir -p "$INSTALL_DIR" "$APP_DIR" "$ICON_DIR"

cp dist/StealthClickerPro "$INSTALL_DIR/stealthclickerpro"
chmod +x "$INSTALL_DIR/stealthclickerpro"

if [ -f "assets/icon.png" ]; then
    cp assets/icon.png "$ICON_DIR/stealthclickerpro.png"
fi

DESKTOP_FILE="$APP_DIR/stealthclickerpro.desktop"

cat << EOF > "$DESKTOP_FILE"
[Desktop Entry]
Version=1.0
Type=Application
Name=Stealth Clicker Pro
Comment=Cross-Platform Auto Clicker with Anti-Cheat Evasion
Exec=$INSTALL_DIR/stealthclickerpro
Icon=$ICON_DIR/stealthclickerpro.png
Terminal=false
Categories=Utility;Gaming;
EOF

chmod +x "$DESKTOP_FILE"

echo "========================================================"
echo " [✓] Stealth Clicker Pro successfully installed!"
echo " 📍 Binary location : $INSTALL_DIR/stealthclickerpro"
echo " 🎨 Desktop Entry   : $DESKTOP_FILE"
echo "--------------------------------------------------------"
echo " You can now search for 'Stealth Clicker Pro' in your Linux application menu!"
echo "========================================================"

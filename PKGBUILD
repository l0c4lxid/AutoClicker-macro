# Maintainer: l0c4lxid <syaidxandhika@gmail.com>
pkgname=stealth-clicker-pro
pkgver=3.2.0
pkgrel=1
pkgdesc="Modern Cyberpunk Cross-Platform Auto Clicker with Anti-Cheat Evasion"
arch=('x86_64')
url="https://github.com/l0c4lxid/AutoClicker-macro"
license=('MIT')
depends=('python' 'python-pynput' 'tk' 'xdotool' 'ydotool')
makedepends=('python-pillow' 'pyinstaller')
provides=('stealth-clicker-pro')
conflicts=('stealth-clicker-pro-git')

build() {
  cd "$startdir"
  python scripts/generate_assets.py

  pyinstaller \
    --name=StealthClickerPro \
    --onefile \
    --windowed \
    --add-data=assets:assets \
    --hidden-import=pynput \
    --hidden-import=pynput.keyboard._xorg \
    --hidden-import=pynput.mouse._xorg \
    --hidden-import=tkinter \
    --noconfirm --clean \
    main.py
}

package() {
  cd "$startdir"

  # Install binary executable
  install -Dm755 dist/StealthClickerPro "$pkgdir/usr/bin/stealthclickerpro"

  # Install application icon
  install -Dm644 assets/icon.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/stealthclickerpro.png"

  # Install desktop application launcher entry
  mkdir -p "$pkgdir/usr/share/applications"
  cat << EOF > "$pkgdir/usr/share/applications/stealthclickerpro.desktop"
[Desktop Entry]
Version=1.0
Type=Application
Name=Stealth Clicker Pro
Comment=Cross-Platform Auto Clicker with Anti-Cheat Evasion
Exec=stealthclickerpro
Icon=stealthclickerpro
Terminal=false
Categories=Utility;Gaming;
EOF
  chmod 644 "$pkgdir/usr/share/applications/stealthclickerpro.desktop"
}

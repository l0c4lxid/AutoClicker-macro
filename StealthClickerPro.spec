# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')],
    hiddenimports=['pynput', 'pynput.keyboard._xorg', 'pynput.mouse._xorg', 'tkinter', 'autoclicker', 'autoclicker.utils', 'autoclicker.utils.platform', 'autoclicker.core', 'autoclicker.core.engine', 'autoclicker.core.listeners', 'autoclicker.ui', 'autoclicker.ui.app', 'autoclicker.ui.theme', 'autoclicker.ui.pages', 'autoclicker.ui.pages.dashboard', 'autoclicker.ui.pages.anticheat', 'autoclicker.ui.pages.presets', 'autoclicker.ui.pages.settings', 'autoclicker.utils.config', 'autoclicker.utils.sound'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='StealthClickerPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

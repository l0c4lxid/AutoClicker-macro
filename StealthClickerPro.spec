# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

project_dir = os.path.abspath(os.path.dirname('.'))
assets_dir = os.path.join(project_dir, 'assets')

datas = []
if os.path.exists(assets_dir):
    datas.append((assets_dir, 'assets'))

hidden_imports = [
    'pynput',
    'pynput.keyboard',
    'pynput.mouse',
    'tkinter',
    'tkinter.ttk',
    'ctypes',
    'autoclicker',
    'autoclicker.core',
    'autoclicker.core.engine',
    'autoclicker.core.listeners',
    'autoclicker.ui',
    'autoclicker.ui.app',
    'autoclicker.ui.theme',
    'autoclicker.ui.pages',
    'autoclicker.ui.pages.dashboard',
    'autoclicker.ui.pages.anticheat',
    'autoclicker.ui.pages.presets',
    'autoclicker.ui.pages.settings',
    'autoclicker.utils',
    'autoclicker.utils.platform',
    'autoclicker.utils.sound',
]

if sys.platform.startswith('win'):
    hidden_imports.extend(['pynput.keyboard._win32', 'pynput.mouse._win32', 'ctypes.wintypes'])
else:
    hidden_imports.extend(['pynput.keyboard._xorg', 'pynput.mouse._xorg'])

a = Analysis(
    ['main.py'],
    pathex=[project_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'scipy', 'numpy', 'pandas', 'unittest', 'email', 'html', 'http', 'xml'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

icon_path = os.path.join(assets_dir, 'icon.ico') if sys.platform.startswith('win') else os.path.join(assets_dir, 'icon.png')
if not os.path.exists(icon_path):
    icon_path = None

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
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
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
)

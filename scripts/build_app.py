# -*- coding: utf-8 -*-
"""
Stealth Clicker Pro - Application Builder
Compiles the application into a single standalone executable file for Windows (.exe) or Linux.
"""

import os
import sys
import subprocess
import shutil

def run_cmd(cmd, description):
    print(f"\n[>] {description}...")
    print(f"    Running: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"[X] Error executing: {description}")
        sys.exit(res.returncode)
    print(f"[+] Success: {description}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    os.chdir(project_root)

    print("========================================================")
    print("   [*] Stealth Clicker Pro - Standalone App Builder")
    print("========================================================")

    # 1. Install required packages
    req_file = os.path.join(project_root, "requirements.txt")
    run_cmd([sys.executable, "-m", "pip", "install", "-r", req_file], "Checking & Installing Dependencies")

    # 2. Generate Icon Assets
    assets_script = os.path.join(script_dir, "generate_assets.py")
    if os.path.exists(assets_script):
        run_cmd([sys.executable, assets_script], "Generating Cyberpunk Icon Assets")

    # 3. Build Executable with PyInstaller using StealthClickerPro.spec
    spec_file = os.path.join(project_root, "StealthClickerPro.spec")
    if os.path.exists(spec_file):
        cmd = [sys.executable, "-m", "PyInstaller", spec_file, "--noconfirm", "--clean"]
    else:
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--name=StealthClickerPro",
            "--onefile",
            "--windowed",
            "--add-data=assets;assets" if sys.platform.startswith("win") else "--add-data=assets:assets",
            "--hidden-import=pynput",
            "--hidden-import=pynput.keyboard._win32",
            "--hidden-import=pynput.mouse._win32",
            "--hidden-import=pynput.keyboard._xorg",
            "--hidden-import=pynput.mouse._xorg",
            "--hidden-import=tkinter",
            "--noconfirm", "--clean",
            "main.py"
        ]
        if os.path.exists(os.path.join(project_root, "assets", "icon.ico")) and sys.platform.startswith("win"):
            cmd.insert(-1, f"--icon={os.path.join(project_root, 'assets', 'icon.ico')}")
    run_cmd(cmd, "Compiling Executable with PyInstaller")

    # 4. Verify Built Executable
    dist_dir = os.path.join(project_root, "dist")
    exe_name = "StealthClickerPro.exe" if sys.platform.startswith("win") else "StealthClickerPro"
    exe_path = os.path.join(dist_dir, exe_name)

    print("\n========================================================")
    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print(" [+] BUILD SUCCESSFUL!")
        print(f" [*] Executable location : {exe_path}")
        print(f" [*] Executable size     : {size_mb:.2f} MB")
        print("--------------------------------------------------------")
        print(" Application can now be launched directly without Python!")
    else:
        print(f" [!] Build finished, but output file missing at: {exe_path}")
    print("========================================================\n")

if __name__ == "__main__":
    main()

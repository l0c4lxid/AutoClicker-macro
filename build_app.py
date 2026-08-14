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
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)

    print("========================================================")
    print("   [*] Stealth Clicker Pro - Standalone App Builder")
    print("========================================================")

    # 1. Install required packages
    run_cmd([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], "Checking & Installing Dependencies")

    # 2. Generate Icon Assets
    assets_script = os.path.join(project_root, "generate_assets.py")
    if os.path.exists(assets_script):
        run_cmd([sys.executable, assets_script], "Generating Cyberpunk Icon Assets")

    # 3. Build Executable with PyInstaller using StealthClickerPro.spec
    spec_file = os.path.join(project_root, "StealthClickerPro.spec")
    run_cmd([sys.executable, "-m", "PyInstaller", spec_file, "--noconfirm", "--clean"], "Compiling Executable with PyInstaller")

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

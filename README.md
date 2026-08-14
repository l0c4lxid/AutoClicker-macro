# 🛡️ Stealth Clicker Pro v2.5

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-brightgreen.svg)](https://github.com/l0c4lxid/AutoClicker-macro)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)
[![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-cyan.svg)](https://docs.python.org/3/library/tkinter.html)

**Stealth Clicker Pro** adalah aplikasi Auto Clicker modern, ringan, dan *cross-platform* (Windows & Linux) yang dirancang dengan antarmuka **Cyberpunk Dark Mode & Soft Light Mode**, dilengkapi fitur **Anti-Cheat Stealth Evasion** (*Human Mode Jitter* ±8% & *Windows SendInput Low-Level API*).

---

## ✨ Fitur Utama

- 🎨 **Dual Theme System (Dark Mode & Light Mode)**
  - Tampilan **Cyberpunk Dark Mode** (Neon Cyan & Obsidian Black) dan **Soft Light Mode** (Sky Blue & Crisp Slate) yang dapat diubah secara *real-time*.
- 🛡️ **Anti-Cheat & Stealth Evasion**
  - **Human Mode Jitter**: Mengacak jeda klik sebesar ±8% dan durasi penekanan (25-50ms) untuk meniru kebiasaan manusia & menghindari pembacaan pola bot.
  - **Low-Level Windows SendInput API**: Menggunakan Win32 DirectInput driver injection untuk melewati deteksi anti-cheat game.
  - **Window Title Disguise**: Menyamarkan judul jendela aplikasi di Taskbar (*Task Manager, Calculator, Notepad, Windows Settings*) untuk menghindari pembacaan nama proses telemetry.
- ⌨️ **Global Hotkey & Mouse Macro Support**
  - Mengontrol Start/Stop menggunakan tombol khusus keyboard (`F6`, `F8`, `F9`, `F10`, `F11`, `Space`) maupun tombol macro mouse (`Mouse Side X1/X2`, `Middle Mouse`).
- 🚨 **Emergency Panic Break [ ESC ]**
  - Menghentikan seluruh ikatan *clicking thread* seketika hanya dengan menekan `[ ESC ]` (atau `F12` / `Pause Break`).
- ⚡ **Presets & Profile Presets**
  - Pilihan preset kecepatan instan: `50ms` (Fast CPS), `100ms` (Gaming), `500ms` (Anti-Detect Stealth), `1000ms`, `2000ms`.
- 🐧 **100% Cross-Platform (Windows & Linux)**
  - Kompatibel penuh di Windows 10/11 dan distro Linux (CachyOS, Arch Linux, Ubuntu, Debian, Fedora).

---

## 📁 Struktur Proyek (Clean Modular Architecture)

Proyek ini disusun secara rapi dan modular sesuai standar pembuatan aplikasi Python & CI/CD profesional:

```text
AutoClicker-macro/
├── main.py                     # Entry point utama aplikasi
├── autoclicker.py              # Backward-compatible wrapper entry
├── requirements.txt            # Dependensi Python aplikasi & build
├── StealthClickerPro.spec      # Spesifikasi PyInstaller build
├── run_autoclicker.bat         # Launcher 1-Klik (Windows)
├── run_autoclicker.sh          # Launcher 1-Klik (Linux)
├── build_windows.bat           # Builder Executable 1-Klik (Windows)
├── build_linux.sh              # Builder Executable 1-Klik (Linux)
├── .gitignore                  # Konfigurasi Git ignore
├── README.md                   # Dokumentasi Resmi Aplikasi
│
├── assets/                     # Branding & Ikon Aplikasi
│   ├── icon.ico                # Ikon aplikasi format ICO (Windows)
│   └── icon.png                # Ikon aplikasi format PNG (Linux & App)
│
├── autoclicker/                # Core Python Package
│   ├── core/                   # Engine & Listener logic
│   │   ├── engine.py           # AutoClicker clicking thread & jitter algorithm
│   │   └── listeners.py        # Global pynput keyboard & mouse listeners
│   ├── ui/                     # Tkinter UI Components
│   │   ├── app.py              # Window manager & page switcher
│   │   ├── theme.py            # Dark Mode & Light Mode color engine
│   │   └── pages/              # Halaman UI (Dashboard, AntiCheat, Presets, Settings)
│   └── utils/                  # Utility helpers
│       ├── platform.py         # OS detection & Win32 SendInput structures
│       └── sound.py            # Cross-platform sound beep helper
│
├── scripts/                    # Script Pembantu Build & Installer
│   ├── generate_assets.py      # Generator otomatis ikon Cyberpunk
│   ├── build_app.py            # Builder executable cross-platform
│   ├── install_linux.sh        # Installer shortcut desktop (.desktop) Linux
│   ├── installer_windows.iss   # Script Inno Setup installer wizard (.exe)
│   └── install_requirements.bat# Script otomatis instalasi pip requirements
│
└── .github/                    # CI/CD GitHub Actions Automation
    └── workflows/
        └── build-release.yml   # Workflow otomatisasi build & release GitHub
```

---

## 📦 Menjalankan Sebagai Aplikasi Standalone (Tanpa Install Python!)

Aplikasi **Stealth Clicker Pro** kini dapat dikompilasi dan dijalankan secara langsung sebagai aplikasi desktop bawaan (`.exe` untuk Windows & Standalone Binary untuk Linux) tanpa perlu menginstal Python di komputer target.

### 1. Download Langsung dari GitHub Releases
Buka halaman [GitHub Releases](https://github.com/l0c4lxid/AutoClicker-macro/releases) untuk mengunduh versi siap pakai:
- 🪟 **`StealthClickerPro-Windows-x64.exe`** (Untuk Windows 10/11)
- 🐧 **`StealthClickerPro-Linux-x64.tar.gz`** (Untuk CachyOS, Arch, Ubuntu, Fedora)

### 2. Membangun Aplikasi Executable Sendiri (1-Klik Build)

#### Di Windows (`.exe` Standalone):
Cukup klik ganda file `build_windows.bat` atau jalankan di terminal:
```powershell
python scripts/build_app.py
# atau double-click: build_windows.bat
```
Hasil executable akan secara otomatis dibuat di folder `dist/StealthClickerPro.exe`.

#### Di Linux (CachyOS / Arch / Ubuntu):
Jalankan script pembangun aplikasi berikut di Terminal:
```bash
chmod +x build_linux.sh scripts/install_linux.sh
./build_linux.sh
```
Hasil binary executable dibuat di `dist/StealthClickerPro`.

### 3. Memasang ke Application Launcher Linux (`.desktop`)
Agar aplikasi muncul di menu aplikasi Linux dengan ikon Cyberpunk:
```bash
./scripts/install_linux.sh
```

### 4. Membuat Windows Setup Installer (`.exe` Setup)
Menggunakan [Inno Setup Compiler](https://jrsoftware.org/isinfo.php):
1. Buka file `scripts/installer_windows.iss` di Inno Setup.
2. Klik **Compile** (`Ctrl + F9`).
3. File installer `StealthClickerPro_Setup.exe` akan siap didistribusikan.

### 5. 🤖 Automated Build & GitHub Releases (CI/CD)
Setiap kali Anda melakukan push commit baru ke branch `main` atau menambahkan release tag (`v*`), GitHub Actions akan secara otomatis mengompilasi file executable Windows & Linux lalu mengunggahnya ke halaman **GitHub Releases**.

---

## 🚀 Panduan Jalur Pengembang (Python Source Code)

### 1. Prasyarat
Pastikan Anda telah menginstal **Python 3.8** atau versi yang lebih baru.

### 2. Kloning Repository
```bash
git clone https://github.com/l0c4lxid/AutoClicker-macro.git
cd AutoClicker-macro
```

### 3. Instalasi Dependensi
```bash
pip install -r requirements.txt
# atau double-click: scripts/install_requirements.bat
```

### 4. Menjalankan Aplikasi
- **Di Windows**:
  ```powershell
  python main.py
  # atau double-click: run_autoclicker.bat
  ```
- **Di Linux**:
  ```bash
  chmod +x run_autoclicker.sh
  ./run_autoclicker.sh
  ```

---

## 🎮 Panduan Tombol Pintas (Hotkey Reference)

| Perintah | Hotkey Default | Opsi Alternatif |
| :--- | :--- | :--- |
| **Start / Stop Clicker** | `Mouse Side (X1/X2)` | `F6`, `F8`, `F9`, `F10`, `F11`, `Space`, `Middle Mouse` |
| **Emergency Panic Break** | `ESC` | `F12`, `Pause/Break` |
| **Toggle Light / Dark Mode** | `🌙 Dark Mode` (Tombol Sidebar) | Switch warna otomatis |

---

## 📜 Lisensi

Proyek ini dirilis di bawah lisensi **[MIT License](LICENSE)**. Bebas digunakan, dimodifikasi, dan didistribusikan secara komersial maupun non-komersial.

---

<p align="center">
Dibuat dengan ❤️ & Python Tkinter
</p>

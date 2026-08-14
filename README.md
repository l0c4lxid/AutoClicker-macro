# 🛡️ Stealth Clicker Pro v2.5

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-brightgreen.svg)](https://github.com/)
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
  - Kompatibel penuh di Windows 10/11 dan distro Linux (Ubuntu, Debian, Fedora, Arch Linux).

---

## 📁 Struktur Proyek (Modular Architecture)

Proyek ini disusun secara modular sesuai standar pembuatan aplikasi Python profesional:

```text
Apps/
├── main.py                     # Entry point utama aplikasi
├── autoclicker.py              # Backward-compatible wrapper
├── autoclicker/                # Core Python package
│   ├── core/                   # Engine & input listener logic
│   │   ├── engine.py           # AutoClicker clicking thread & jitter algorithm
│   │   └── listeners.py        # Global pynput keyboard & mouse listeners
│   ├── ui/                     # Tkinter UI Components
│   │   ├── app.py              # Window manager & page switcher
│   │   ├── theme.py            # Dark Mode & Light Mode color engine
│   │   └── pages/              # Tab Halaman UI
│   │       ├── dashboard.py    # Main Dashboard Page
│   │       ├── anticheat.py    # Stealth & Anti-Cheat Page
│   │       ├── presets.py      # Saved Presets Page
│   │       └── settings.py     # General Settings Page
│   └── utils/                  # Utility helpers
│       ├── platform.py         # OS detection & Win32 SendInput structures
│       └── sound.py            # Cross-platform sound beep helper
├── requirements.txt            # Dependensi Python
├── run_autoclicker.bat         # Launcher Script (Windows)
├── run_autoclicker.sh          # Launcher Script (Linux)
├── .gitignore                  # Git ignore configuration
└── README.md                   # Dokumentasi Aplikasi
```

---

## 🚀 Panduan Instalasi & Penggunaan

### 1. Prasyarat
Pastikan Anda telah menginstal **Python 3.8** atau versi yang lebih baru.

### 2. Kloning Repository
```bash
git clone https://github.com/username/stealth-clicker-pro.git
cd stealth-clicker-pro
```

### 3. Instalasi Dependensi
```bash
pip install -r requirements.txt
```

---

## 💻 Cara Menjalankan

### Di Windows:
Cukup jalankan melalui Terminal atau double-click file batch launcher:
```powershell
python main.py
# atau double click: run_autoclicker.bat
```

### Di Linux (Ubuntu / Debian / Arch / Fedora):
```bash
chmod +x run_autoclicker.sh
./run_autoclicker.sh
# atau: python3 main.py
```

> **Catatan Pengguna Linux:**
> Jika global hotkey memerlukan akses perangkat input di lingkungan X11/Wayland, pastikan user Anda sudah dimasukkan ke dalam group `input`:
> ```bash
> sudo usermod -aG input $USER
> ```

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

<p center>
Dibuat dengan ❤️ & Python Tkinter
</p>

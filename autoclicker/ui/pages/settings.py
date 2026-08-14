# -*- coding: utf-8 -*-
import tkinter as tk
from autoclicker.utils.platform import IS_WINDOWS, IS_LINUX

class SettingsPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.theme.colors["bg"])
        self.app = app
        self._build_ui()

    def _build_ui(self):
        colors = self.app.theme.colors

        self.st_header_lbl = tk.Label(
            self,
            text="GENERAL SETTINGS",
            font=("Segoe UI", 13, "bold"),
            fg=colors["text_main"],
            bg=colors["bg"]
        )
        self.st_header_lbl.pack(anchor="w", pady=(0, 16))

        self.st_card = tk.Frame(self, bg=colors["card_bg"], highlightbackground=colors["card_border"], highlightthickness=1)
        self.st_card.pack(fill="x", pady=8)

        self.st_card_inner = tk.Frame(self.st_card, bg=colors["card_bg"])
        self.st_card_inner.pack(fill="x", padx=16, pady=16)

        platform_str = "Windows (DirectInput SendInput API)" if IS_WINDOWS else ("Linux (X11/pynput Engine)" if IS_LINUX else "macOS / Generic Unix")

        info = (
            f"• Stealth Clicker Pro v2.5 Cross-Platform Edition\n"
            f"• Operating System Detected: {platform_str}\n"
            f"• Hotkey Listeners powered by pynput\n"
            f"• Emergency Break Key: Immediate thread interrupt\n\n"
            f"Press [ ESC ] anytime to emergency break.\n\n"
            f"Linux Installation Notes:\n"
            f"If global hotkeys require permissions on Linux X11/Wayland:\n"
            f"1. Run with python3 main.py\n"
            f"2. Ensure user is in 'input' group: sudo usermod -aG input $USER"
        )

        self.st_info_lbl = tk.Label(
            self.st_card_inner,
            text=info,
            font=("Segoe UI", 9),
            fg=colors["text_muted"],
            bg=colors["card_bg"],
            justify="left"
        )
        self.st_info_lbl.pack(anchor="w")

    def apply_theme(self):
        colors = self.app.theme.colors
        self.config(bg=colors["bg"])
        self.st_header_lbl.config(fg=colors["text_main"], bg=colors["bg"])
        self.st_card.config(bg=colors["card_bg"], highlightbackground=colors["card_border"])
        self.st_card_inner.config(bg=colors["card_bg"])
        self.st_info_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

class AntiCheatPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.theme.colors["bg"])
        self.app = app
        self._build_ui()

    def _build_ui(self):
        colors = self.app.theme.colors

        self.ac_header_lbl = tk.Label(
            self,
            text="ANTI-CHEAT STEALTH PROFILES",
            font=("Segoe UI", 13, "bold"),
            fg=colors["tertiary_purple"],
            bg=colors["bg"]
        )
        self.ac_header_lbl.pack(anchor="w", pady=(0, 16))

        self.ac_card = tk.Frame(
            self,
            bg=colors["card_bg"],
            highlightbackground=colors["card_border"],
            highlightthickness=1
        )
        self.ac_card.pack(fill="x", pady=8)

        self.ac_card_inner = tk.Frame(self.ac_card, bg=colors["card_bg"])
        self.ac_card_inner.pack(fill="x", padx=16, pady=16)

        # Title disguise row
        self.disguise_title = tk.Label(
            self.ac_card_inner,
            text="🕵  Window Title Disguise (Evasion):",
            font=("Segoe UI", 10, "bold"),
            fg=colors["text_main"],
            bg=colors["card_bg"]
        )
        self.disguise_title.pack(anchor="w", pady=(0, 6))

        self.disguise_sub = tk.Label(
            self.ac_card_inner,
            text="Changes taskbar & window title to evade process telemetry scanners.",
            font=("Segoe UI", 8),
            fg=colors["text_muted"],
            bg=colors["card_bg"]
        )
        self.disguise_sub.pack(anchor="w", pady=(0, 10))

        disguise_options = [
            "Normal (Auto Clicker)",
            "System Host Process",
            "Calculator",
            "Notepad - Untitled",
            "Windows Settings",
            "Task Manager"
        ]
        self.disguise_menu = ttk.OptionMenu(
            self.ac_card_inner,
            self.app.disguise_title_var,
            self.app.disguise_title_var.get(),
            *disguise_options,
            style="Custom.TMenubutton"
        )
        self.disguise_menu.pack(anchor="w", pady=(0, 14))

        # Sound beep options
        self.sound_cb = tk.Checkbutton(
            self.ac_card_inner,
            text="🔊  Play Audio Beep on Start / Stop toggle",
            variable=self.app.sound_enabled_var,
            font=("Segoe UI", 9),
            fg=colors["text_main"],
            bg=colors["card_bg"],
            activebackground=colors["card_bg"],
            activeforeground=colors["primary_container"],
            selectcolor=colors["surface_dim"],
            cursor="hand2"
        )
        self.sound_cb.pack(anchor="w", pady=4)

    def apply_theme(self):
        colors = self.app.theme.colors
        self.config(bg=colors["bg"])
        self.ac_header_lbl.config(fg=colors["tertiary_purple"], bg=colors["bg"])
        self.ac_card.config(bg=colors["card_bg"], highlightbackground=colors["card_border"])
        self.ac_card_inner.config(bg=colors["card_bg"])
        self.disguise_title.config(fg=colors["text_main"], bg=colors["card_bg"])
        self.disguise_sub.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.sound_cb.config(
            fg=colors["text_main"],
            bg=colors["card_bg"],
            activebackground=colors["card_bg"],
            activeforeground=colors["primary_container"],
            selectcolor=colors["surface_dim"]
        )

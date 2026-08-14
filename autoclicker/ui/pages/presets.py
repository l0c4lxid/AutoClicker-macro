# -*- coding: utf-8 -*-
import tkinter as tk

class PresetsPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.theme.colors["bg"])
        self.app = app
        self._build_ui()

    def _build_ui(self):
        colors = self.app.theme.colors

        self.pr_header_lbl = tk.Label(
            self,
            text="SAVED PRESETS & PROFILES",
            font=("Segoe UI", 13, "bold"),
            fg=colors["primary_container"],
            bg=colors["bg"]
        )
        self.pr_header_lbl.pack(anchor="w", pady=(0, 16))

        presets_list = [
            ("⚡ Ultra Fast CPS (50ms)", "50", "Ideal for fast spamming clickers & rapid fire."),
            ("🎯 Balanced Gaming (100ms)", "100", "Optimal for Minecraft, Roblox & Action RPGs."),
            ("🛡 Anti-Detect Stealth (500ms)", "500", "Standard safe human clicking speed."),
            ("⏱ Slow Automation (1000ms)", "1000", "1 click per second for background work."),
            ("⌛ Long Interval (2000ms)", "2000", "2 seconds delay for idle AFK scripts.")
        ]

        self.preset_cards_widgets = []
        for title, val, desc in presets_list:
            card = tk.Frame(self, bg=colors["card_bg"], highlightbackground=colors["card_border"], highlightthickness=1)
            card.pack(fill="x", pady=6)

            card_inner = tk.Frame(card, bg=colors["card_bg"])
            card_inner.pack(fill="x", padx=14, pady=10)

            t_lbl = tk.Label(card_inner, text=title, font=("Segoe UI", 10, "bold"), fg=colors["primary"], bg=colors["card_bg"])
            t_lbl.pack(anchor="w")

            d_lbl = tk.Label(card_inner, text=desc, font=("Segoe UI", 8), fg=colors["text_muted"], bg=colors["card_bg"])
            d_lbl.pack(anchor="w", pady=(2, 6))

            load_btn = tk.Button(
                card_inner,
                text="Load Preset",
                font=("Segoe UI", 8, "bold"),
                bg=colors["btn_default_bg"],
                fg=colors["primary_container"],
                bd=0,
                cursor="hand2",
                command=lambda v=val: [self.app.select_preset(v), self.app.switch_tab("dashboard")]
            )
            load_btn.pack(anchor="e")
            self.preset_cards_widgets.append((card, card_inner, t_lbl, d_lbl, load_btn))

    def apply_theme(self):
        colors = self.app.theme.colors
        self.config(bg=colors["bg"])
        self.pr_header_lbl.config(fg=colors["primary_container"], bg=colors["bg"])
        for p_card, p_inner, t_lbl, d_lbl, load_btn in self.preset_cards_widgets:
            p_card.config(bg=colors["card_bg"], highlightbackground=colors["card_border"])
            p_inner.config(bg=colors["card_bg"])
            t_lbl.config(fg=colors["primary"], bg=colors["card_bg"])
            d_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
            load_btn.config(
                bg=colors["btn_default_bg"],
                fg=colors["primary_container"],
                activebackground=colors["card_hover"],
                activeforeground=colors["primary"]
            )

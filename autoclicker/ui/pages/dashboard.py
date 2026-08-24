# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from autoclicker.utils.platform import IS_WINDOWS

class DashboardPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.theme.colors["bg"])
        self.app = app
        self._build_ui()

    def _build_ui(self):
        colors = self.app.theme.colors

        self.container = tk.Frame(self, bg=colors["bg"])
        self.container.pack(fill="both", expand=True)

        # Header Title
        self.header_lbl = tk.Label(
            self.container,
            text="STEALTH CLICKER DASHBOARD",
            font=("Segoe UI", 13, "bold"),
            fg=colors["primary"],
            bg=colors["bg"]
        )
        self.header_lbl.pack(anchor="w", pady=(0, 8))

        # A. EMERGENCY BANNER BADGE
        self.banner = tk.Frame(
            self.container,
            bg=colors["secondary_bg"],
            highlightbackground=colors["secondary_border"],
            highlightthickness=1
        )
        self.banner.pack(fill="x", pady=(0, 10))

        self.banner_lbl = tk.Label(
            self.banner,
            text="⚠  EMERGENCY BREAK: Press [ ESC ] to immediately stop all operations!",
            font=("Segoe UI", 9, "bold"),
            fg=colors["error_red"],
            bg=colors["secondary_bg"],
            pady=6,
            padx=10
        )
        self.banner_lbl.pack(anchor="w")

        # B. STATUS CARD
        self.status_card = tk.Frame(
            self.container,
            bg=colors["card_bg"],
            highlightbackground=colors["error_red"],
            highlightthickness=1
        )
        self.status_card.pack(fill="x", pady=(0, 10))

        self.status_inner = tk.Frame(self.status_card, bg=colors["card_bg"])
        self.status_inner.pack(fill="x", padx=14, pady=12)

        self.status_icon = tk.Label(self.status_inner, text="🔴", font=("Segoe UI", 20), bg=colors["card_bg"])
        self.status_icon.pack(side="left", padx=(0, 12))

        self.status_txt_box = tk.Frame(self.status_inner, bg=colors["card_bg"])
        self.status_txt_box.pack(side="left", fill="both", expand=True)

        self.status_text = tk.Label(
            self.status_txt_box,
            text="STATUS: OFF",
            font=("Segoe UI", 13, "bold"),
            fg=colors["error_red"],
            bg=colors["card_bg"],
            anchor="w"
        )
        self.status_text.pack(fill="x")

        self.status_sub = tk.Label(
            self.status_txt_box,
            text="Press Trigger Shortcut to Start Auto Clicker",
            font=("Segoe UI", 8),
            fg=colors["text_muted"],
            bg=colors["card_bg"],
            anchor="w"
        )
        self.status_sub.pack(fill="x")

        # C. CORE CONFIGURATION PANEL
        self.config_card = tk.Frame(
            self.container,
            bg=colors["card_bg"],
            highlightbackground=colors["card_border"],
            highlightthickness=1
        )
        self.config_card.pack(fill="x", pady=(0, 10))

        self.config_inner = tk.Frame(self.config_card, bg=colors["card_bg"])
        self.config_inner.pack(fill="x", padx=14, pady=12)

        # Interval Row
        self.interval_header = tk.Label(
            self.config_inner,
            text="⏱  Click Interval (ms)",
            font=("Segoe UI", 9, "bold"),
            fg=colors["text_muted"],
            bg=colors["card_bg"]
        )
        self.interval_header.pack(anchor="w", pady=(0, 4))

        self.interval_input_row = tk.Frame(self.config_inner, bg=colors["card_bg"])
        self.interval_input_row.pack(fill="x", pady=(0, 6))

        self.interval_entry = tk.Entry(
            self.interval_input_row,
            textvariable=self.app.interval_ms_var,
            font=("Consolas", 11, "bold"),
            bg=colors["entry_bg"],
            fg=colors["primary_container"],
            insertbackground=colors["primary"],
            bd=1,
            relief="solid",
            highlightbackground=colors["card_border"],
            width=10,
            justify="center"
        )
        self.interval_entry.pack(side="left", ipady=3)

        self.interval_unit_lbl = tk.Label(
            self.interval_input_row,
            text="ms  (1000 ms = 1 sec)",
            font=("Segoe UI", 8),
            fg=colors["text_muted"],
            bg=colors["card_bg"]
        )
        self.interval_unit_lbl.pack(side="left", padx=8)

        # Preset Buttons Row
        self.preset_row = tk.Frame(self.config_inner, bg=colors["card_bg"])
        self.preset_row.pack(fill="x", pady=(0, 8))

        self.preset_btns = {}
        presets = [("50ms", "50"), ("100ms", "100"), ("500ms", "500"), ("1000ms", "1000"), ("2000ms", "2000")]
        for label, val in presets:
            btn = tk.Button(
                self.preset_row,
                text=label,
                font=("Consolas", 9, "bold"),
                bg=colors["primary_container"] if val == "500" else colors["btn_default_bg"],
                fg=colors["on_primary"] if val == "500" else colors["text_main"],
                bd=1,
                relief="solid",
                highlightbackground=colors["primary_container"] if val == "500" else colors["card_border"],
                activebackground=colors["card_hover"],
                activeforeground=colors["primary"],
                cursor="hand2",
                command=lambda v=val: self.app.select_preset(v)
            )
            btn.pack(side="left", padx=(0, 6), ipady=2, ipadx=8)
            self.preset_btns[val] = btn

        # Separator line
        self.config_sep = tk.Frame(self.config_inner, bg=colors["card_border"], height=1)
        self.config_sep.pack(fill="x", pady=8)

        # Trigger Shortcut & Click Type Grid
        self.trig_grid = tk.Frame(self.config_inner, bg=colors["card_bg"])
        self.trig_grid.pack(fill="x", pady=2)

        # Row 1: Trigger Shortcut
        self.trig_lbl = tk.Label(self.trig_grid, text="⌨  Trigger Shortcut:", font=("Segoe UI", 9, "bold"),
                                 fg=colors["text_muted"], bg=colors["card_bg"], width=18, anchor="w")
        self.trig_lbl.grid(row=0, column=0, sticky="w", pady=4)

        trig_options = ["F", "Space", "F6", "F8", "F9", "F10", "F11", "Mouse Side (X1/X2)", "Middle Mouse"]
        self.trig_menu = ttk.OptionMenu(self.trig_grid, self.app.hotkey_var, self.app.hotkey_var.get(), *trig_options, style="Custom.TMenubutton")
        self.trig_menu.grid(row=0, column=1, sticky="w", pady=4)

        # Row 2: Emergency Key
        self.em_lbl = tk.Label(self.trig_grid, text="🚨  Emergency Key:", font=("Segoe UI", 9, "bold"),
                               fg=colors["error_red"], bg=colors["card_bg"], width=18, anchor="w")
        self.em_lbl.grid(row=1, column=0, sticky="w", pady=4)

        em_options = ["ESC", "F12", "Pause/Break"]
        self.em_menu = ttk.OptionMenu(self.trig_grid, self.app.emergency_key_var, self.app.emergency_key_var.get(), *em_options, style="Custom.TMenubutton")
        self.em_menu.grid(row=1, column=1, sticky="w", pady=4)

        # Row 3: Action Category Mode (Mouse vs Keyboard)
        self.act_lbl = tk.Label(self.trig_grid, text="⚡  Action Type:", font=("Segoe UI", 9, "bold"),
                                fg=colors["text_muted"], bg=colors["card_bg"], width=18, anchor="w")
        self.act_lbl.grid(row=2, column=0, sticky="w", pady=4)

        self.act_mode_frame = tk.Frame(self.trig_grid, bg=colors["card_bg"])
        self.act_mode_frame.grid(row=2, column=1, sticky="w", pady=4)

        self.mouse_mode_rb = tk.Radiobutton(
            self.act_mode_frame, text="Mouse Click", value="Mouse",
            variable=self.app.action_mode_var, font=("Segoe UI", 9, "bold"),
            fg=colors["text_main"], bg=colors["card_bg"], activebackground=colors["card_bg"],
            activeforeground=colors["primary_container"], selectcolor=colors["surface_dim"],
            cursor="hand2", command=self._on_action_mode_toggle
        )
        self.mouse_mode_rb.pack(side="left", padx=(0, 12))

        self.kb_mode_rb = tk.Radiobutton(
            self.act_mode_frame, text="Keyboard Key", value="Keyboard",
            variable=self.app.action_mode_var, font=("Segoe UI", 9, "bold"),
            fg=colors["text_main"], bg=colors["card_bg"], activebackground=colors["card_bg"],
            activeforeground=colors["primary_container"], selectcolor=colors["surface_dim"],
            cursor="hand2", command=self._on_action_mode_toggle
        )
        self.kb_mode_rb.pack(side="left", padx=(0, 12))

        # Row 4: Mouse Click Options
        self.click_lbl = tk.Label(self.trig_grid, text="🖱  Mouse Button:", font=("Segoe UI", 9, "bold"),
                                  fg=colors["text_muted"], bg=colors["card_bg"], width=18, anchor="w")

        self.click_radio_frame = tk.Frame(self.trig_grid, bg=colors["card_bg"])

        self.click_rbs = []
        for c_type in ["Left", "Right", "Middle"]:
            rb = tk.Radiobutton(
                self.click_radio_frame,
                text=c_type,
                value=c_type,
                variable=self.app.click_type_var,
                font=("Segoe UI", 9, "bold"),
                fg=colors["text_main"],
                bg=colors["card_bg"],
                activebackground=colors["card_bg"],
                activeforeground=colors["primary_container"],
                selectcolor=colors["surface_dim"],
                cursor="hand2"
            )
            rb.pack(side="left", padx=(0, 12))
            self.click_rbs.append(rb)

        # Row 5: Keyboard Key Options
        self.kb_lbl = tk.Label(self.trig_grid, text="⌨  Key to Press:", font=("Segoe UI", 9, "bold"),
                               fg=colors["text_muted"], bg=colors["card_bg"], width=18, anchor="w")

        self.kb_opts_frame = tk.Frame(self.trig_grid, bg=colors["card_bg"])

        self.kb_preset_row = tk.Frame(self.kb_opts_frame, bg=colors["card_bg"])
        self.kb_preset_row.pack(anchor="w", pady=(0, 4))

        self.kb_preset_btns = []
        kb_presets = ["F", "Space", "Enter", "Tab", "E", "Q", "W", "A", "S", "D"]
        for kp in kb_presets:
            btn = tk.Button(
                self.kb_preset_row, text=kp, font=("Consolas", 8, "bold"),
                bg=colors["btn_default_bg"], fg=colors["primary"], bd=1, relief="solid",
                highlightbackground=colors["card_border"], cursor="hand2",
                command=lambda k=kp: self.app.custom_key_var.set(k)
            )
            btn.pack(side="left", padx=(0, 4), ipady=1, ipadx=5)
            self.kb_preset_btns.append(btn)

        self.custom_key_row = tk.Frame(self.kb_opts_frame, bg=colors["card_bg"])
        self.custom_key_row.pack(anchor="w", pady=(2, 0))

        self.custom_key_lbl = tk.Label(self.custom_key_row, text="Custom Key:", font=("Segoe UI", 8),
                                       fg=colors["text_muted"], bg=colors["card_bg"])
        self.custom_key_lbl.pack(side="left", padx=(0, 6))

        self.custom_key_entry = tk.Entry(
            self.custom_key_row, textvariable=self.app.custom_key_var,
            font=("Consolas", 10, "bold"), bg=colors["entry_bg"], fg=colors["primary_container"],
            insertbackground=colors["primary"], bd=1, relief="solid", highlightbackground=colors["card_border"],
            width=8, justify="center"
        )
        self.custom_key_entry.pack(side="left")

        self._on_action_mode_toggle()

        # D. ANTI-CHEAT / STEALTH QUICK SUMMARY PANEL
        self.stealth_card = tk.Frame(
            self.container,
            bg=colors["card_bg"],
            highlightbackground=colors["tertiary_purple_dark"],
            highlightthickness=1
        )
        self.stealth_card.pack(fill="x", pady=(0, 10))

        self.purple_accent = tk.Frame(self.stealth_card, bg=colors["tertiary_purple"], width=4)
        self.purple_accent.pack(side="left", fill="y")

        self.stealth_inner = tk.Frame(self.stealth_card, bg=colors["card_bg"])
        self.stealth_inner.pack(side="left", fill="both", expand=True, padx=12, pady=10)

        self.stealth_title = tk.Label(
            self.stealth_inner,
            text="🛡  Anti-Cheat Stealth Features",
            font=("Segoe UI", 9, "bold"),
            fg=colors["tertiary_purple"],
            bg=colors["card_bg"]
        )
        self.stealth_title.pack(anchor="w", pady=(0, 4))

        self.human_cb = tk.Checkbutton(
            self.stealth_inner,
            text="🧠  Human Mode Jitter (Randomizes delay by ±8% to simulate human click timing)",
            variable=self.app.human_mode_var,
            font=("Segoe UI", 8),
            fg=colors["text_main"],
            bg=colors["card_bg"],
            activebackground=colors["card_bg"],
            activeforeground=colors["tertiary_purple"],
            selectcolor=colors["surface_dim"],
            anchor="w",
            cursor="hand2"
        )
        self.human_cb.pack(fill="x", pady=1)

        sendinput_txt = "⚙  Low-Level Windows API (DirectInput compatible for game hook evasion)" if IS_WINDOWS else "⚙  Low-Level Clicking Engine (Cross-Platform Fallback Enabled)"
        self.sendinput_cb = tk.Checkbutton(
            self.stealth_inner,
            text=sendinput_txt,
            variable=self.app.sendinput_mode_var,
            font=("Segoe UI", 8),
            fg=colors["text_main"],
            bg=colors["card_bg"],
            activebackground=colors["card_bg"],
            activeforeground=colors["tertiary_purple"],
            selectcolor=colors["surface_dim"],
            anchor="w",
            cursor="hand2"
        )
        self.sendinput_cb.pack(fill="x", pady=1)

        # E. PRIMARY ACTIONS & COUNTER PANEL
        self.action_panel = tk.Frame(self.container, bg=colors["bg"])
        self.action_panel.pack(fill="x", pady=(0, 6))

        self.counter_row = tk.Frame(self.action_panel, bg=colors["bg"])
        self.counter_row.pack(fill="x", pady=(0, 6))

        self.counter_title_lbl = tk.Label(self.counter_row, text="Total Clicks:", font=("Segoe UI", 9, "bold"),
                                          fg=colors["text_muted"], bg=colors["bg"])
        self.counter_title_lbl.pack(side="left")

        self.counter_lbl = tk.Label(self.counter_row, text="0", font=("Consolas", 13, "bold"),
                                    fg=colors["primary_container"], bg=colors["bg"])
        self.counter_lbl.pack(side="left", padx=8)

        self.reset_btn = tk.Button(
            self.counter_row,
            text="🔄  Reset Counter",
            font=("Segoe UI", 8, "bold"),
            bg=colors["btn_default_bg"],
            fg=colors["text_muted"],
            activebackground=colors["card_hover"],
            activeforeground=colors["text_main"],
            bd=0,
            cursor="hand2",
            command=self.app.reset_counter
        )
        self.reset_btn.pack(side="right", ipadx=8, ipady=2)

        # START/STOP MAIN BUTTON
        self.main_action_btn = tk.Button(
            self.action_panel,
            text="▶  START AUTO CLICKER",
            font=("Segoe UI", 11, "bold"),
            bg=colors["primary_container"],
            fg=colors["on_primary"],
            activebackground="#0369a1" if not self.app.theme.is_dark_mode else "#00daf3",
            activeforeground=colors["on_primary"],
            bd=0,
            cursor="hand2",
            command=self.app.toggle_clicking
        )
        self.main_action_btn.pack(fill="x", ipady=10, pady=(0, 6))

        # EMERGENCY STOP BUTTON
        self.emergency_stop_btn = tk.Button(
            self.action_panel,
            text="🛑  EMERGENCY STOP (ESC)",
            font=("Segoe UI", 9, "bold"),
            bg=colors["error_bg"],
            fg=colors["on_error"],
            activebackground="#b91c1c" if not self.app.theme.is_dark_mode else colors["secondary_border"],
            activeforeground="#ffffff",
            bd=1,
            relief="solid",
            highlightbackground=colors["secondary_border"],
            cursor="hand2",
            command=self.app.emergency_stop
        )
        self.emergency_stop_btn.pack(fill="x", ipady=6)

    def _on_action_mode_toggle(self):
        mode = self.app.action_mode_var.get()
        if mode == "Mouse":
            self.kb_lbl.grid_forget()
            self.kb_opts_frame.grid_forget()
            self.click_lbl.grid(row=3, column=0, sticky="w", pady=4)
            self.click_radio_frame.grid(row=3, column=1, sticky="w", pady=4)
        else:
            self.click_lbl.grid_forget()
            self.click_radio_frame.grid_forget()
            self.kb_lbl.grid(row=3, column=0, sticky="w", pady=4)
            self.kb_opts_frame.grid(row=3, column=1, sticky="w", pady=4)

    def apply_theme(self):
        colors = self.app.theme.colors
        self.config(bg=colors["bg"])
        self.container.config(bg=colors["bg"])
        self.header_lbl.config(fg=colors["primary"], bg=colors["bg"])

        self.banner.config(bg=colors["secondary_bg"], highlightbackground=colors["secondary_border"])
        self.banner_lbl.config(fg=colors["error_red"], bg=colors["secondary_bg"])

        if not self.app.engine.running:
            self.status_card.config(bg=colors["card_bg"], highlightbackground=colors["error_red"])
            self.status_inner.config(bg=colors["card_bg"])
            self.status_txt_box.config(bg=colors["card_bg"])
            self.status_icon.config(bg=colors["card_bg"])
            self.status_text.config(fg=colors["error_red"], bg=colors["card_bg"])
            self.status_sub.config(fg=colors["text_muted"], bg=colors["card_bg"])
        else:
            self.status_card.config(bg=colors["active_cyan_bg"], highlightbackground=colors["primary_container"])
            self.status_inner.config(bg=colors["active_cyan_bg"])
            self.status_txt_box.config(bg=colors["active_cyan_bg"])
            self.status_icon.config(bg=colors["active_cyan_bg"])
            self.status_text.config(fg=colors["primary_container"], bg=colors["active_cyan_bg"])
            self.status_sub.config(fg=colors["text_main"], bg=colors["active_cyan_bg"])

        self.config_card.config(bg=colors["card_bg"], highlightbackground=colors["card_border"])
        self.config_inner.config(bg=colors["card_bg"])
        self.interval_header.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.interval_input_row.config(bg=colors["card_bg"])
        self.interval_entry.config(
            bg=colors["entry_bg"],
            fg=colors["primary_container"],
            insertbackground=colors["primary"],
            highlightbackground=colors["card_border"]
        )
        self.interval_unit_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.preset_row.config(bg=colors["card_bg"])
        self.config_sep.config(bg=colors["card_border"])
        self.trig_grid.config(bg=colors["card_bg"])
        self.trig_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.em_lbl.config(fg=colors["error_red"], bg=colors["card_bg"])
        self.act_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.act_mode_frame.config(bg=colors["card_bg"])
        self.mouse_mode_rb.config(
            fg=colors["text_main"], bg=colors["card_bg"], activebackground=colors["card_bg"],
            activeforeground=colors["primary_container"], selectcolor=colors["surface_dim"]
        )
        self.kb_mode_rb.config(
            fg=colors["text_main"], bg=colors["card_bg"], activebackground=colors["card_bg"],
            activeforeground=colors["primary_container"], selectcolor=colors["surface_dim"]
        )
        self.click_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.click_radio_frame.config(bg=colors["card_bg"])

        for rb in self.click_rbs:
            rb.config(
                fg=colors["text_main"],
                bg=colors["card_bg"],
                activebackground=colors["card_bg"],
                activeforeground=colors["primary_container"],
                selectcolor=colors["surface_dim"]
            )

        self.kb_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.kb_opts_frame.config(bg=colors["card_bg"])
        self.kb_preset_row.config(bg=colors["card_bg"])
        for btn in getattr(self, "kb_preset_btns", []):
            btn.config(
                bg=colors["btn_default_bg"], fg=colors["primary"],
                highlightbackground=colors["card_border"]
            )
        self.custom_key_row.config(bg=colors["card_bg"])
        self.custom_key_lbl.config(fg=colors["text_muted"], bg=colors["card_bg"])
        self.custom_key_entry.config(
            bg=colors["entry_bg"], fg=colors["primary_container"],
            insertbackground=colors["primary"], highlightbackground=colors["card_border"]
        )

        self.update_preset_button_styles(self.app.interval_ms_var.get())

        self.stealth_card.config(bg=colors["card_bg"], highlightbackground=colors["tertiary_purple_dark"])
        self.purple_accent.config(bg=colors["tertiary_purple"])
        self.stealth_inner.config(bg=colors["card_bg"])
        self.stealth_title.config(fg=colors["tertiary_purple"], bg=colors["card_bg"])

        self.human_cb.config(
            fg=colors["text_main"],
            bg=colors["card_bg"],
            activebackground=colors["card_bg"],
            activeforeground=colors["tertiary_purple"],
            selectcolor=colors["surface_dim"]
        )
        self.sendinput_cb.config(
            fg=colors["text_main"],
            bg=colors["card_bg"],
            activebackground=colors["card_bg"],
            activeforeground=colors["tertiary_purple"],
            selectcolor=colors["surface_dim"]
        )

        self.action_panel.config(bg=colors["bg"])
        self.counter_row.config(bg=colors["bg"])
        self.counter_title_lbl.config(fg=colors["text_muted"], bg=colors["bg"])
        self.counter_lbl.config(fg=colors["primary_container"], bg=colors["bg"])
        self.reset_btn.config(
            bg=colors["btn_default_bg"],
            fg=colors["text_muted"],
            activebackground=colors["card_hover"],
            activeforeground=colors["text_main"]
        )

        if not self.app.engine.running:
            self.main_action_btn.config(
                bg=colors["primary_container"],
                fg=colors["on_primary"],
                activebackground="#0369a1" if not self.app.theme.is_dark_mode else "#00daf3",
                activeforeground=colors["on_primary"]
            )
        else:
            self.main_action_btn.config(
                bg=colors["card_bright"],
                fg="#ffffff" if not self.app.theme.is_dark_mode else colors["text_main"],
                activebackground=colors["card_hover"],
                activeforeground=colors["primary_container"]
            )

        self.emergency_stop_btn.config(
            bg=colors["error_bg"],
            fg=colors["on_error"],
            activebackground="#b91c1c" if not self.app.theme.is_dark_mode else colors["secondary_border"],
            activeforeground="#ffffff",
            highlightbackground=colors["secondary_border"]
        )

    def update_preset_button_styles(self, active_val: str):
        colors = self.app.theme.colors
        if not hasattr(self, "preset_btns"):
            return
        for val, btn in self.preset_btns.items():
            if val == active_val:
                btn.config(
                    bg=colors["primary_container"],
                    fg=colors["on_primary"],
                    highlightbackground=colors["primary_container"]
                )
            else:
                btn.config(
                    bg=colors["btn_default_bg"],
                    fg=colors["text_main"],
                    highlightbackground=colors["card_border"]
                )

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
from autoclicker.ui.theme import ThemeManager
from autoclicker.ui.pages import DashboardPage, AntiCheatPage, PresetsPage, SettingsPage
from autoclicker.core.engine import AutoClickerEngine
from autoclicker.core.listeners import GlobalInputListeners
from autoclicker.utils.platform import IS_WINDOWS, IS_LINUX, set_window_icon

class AutoClickerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Stealth Clicker Pro")
        self.root.geometry("860x780")
        self.root.minsize(800, 700)
        set_window_icon(self.root)

        # Core logic engine
        self.engine = AutoClickerEngine()
        self.engine.on_count_update = self._on_count_update
        self.engine.on_state_change = self._on_state_change

        # Settings variables
        self.interval_ms_var = tk.StringVar(value="500")
        self.action_mode_var = tk.StringVar(value="Mouse")  # "Mouse" or "Keyboard"
        self.click_type_var = tk.StringVar(value="Left")
        self.custom_key_var = tk.StringVar(value="f")
        self.hotkey_var = tk.StringVar(value="F")
        self.emergency_key_var = tk.StringVar(value="ESC")
        self.sound_enabled_var = tk.BooleanVar(value=True)

        # Stealth & Anti-Cheat variables
        self.human_mode_var = tk.BooleanVar(value=True)
        self.sendinput_mode_var = tk.BooleanVar(value=True)
        self.disguise_title_var = tk.StringVar(value="Normal (Auto Clicker)")

        # Theme system
        self.theme = ThemeManager(is_dark_mode=True)

        # Build GUI
        self.root.configure(bg=self.theme.colors["bg"])
        self._setup_custom_styles()
        self._create_widgets()

        # Traces & Handlers (set up after widgets & pages initialization)
        self.disguise_title_var.trace_add("write", self._apply_window_disguise)
        self.hotkey_var.trace_add("write", self._update_button_text)
        self.interval_ms_var.trace_add("write", self._on_interval_change)

        # Global input listeners
        self.listeners = GlobalInputListeners(
            get_hotkey_func=lambda: self.hotkey_var.get(),
            get_emergency_key_func=lambda: self.emergency_key_var.get(),
            on_toggle_func=lambda: self.root.after(0, self.toggle_clicking),
            on_emergency_func=lambda: self.root.after(0, self.emergency_stop)
        )
        self.listeners.start()

        # Window close protocol
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _setup_custom_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('default')

    def _update_ttk_styles(self):
        colors = self.theme.colors
        self.style.configure(
            "Custom.TMenubutton",
            background=colors["surface_dim"],
            foreground=colors["primary"],
            bordercolor=colors["card_border"],
            darkcolor=colors["surface_dim"],
            lightcolor=colors["surface_dim"],
            arrowcolor=colors["primary"],
            font=("Segoe UI", 9, "bold"),
            padding=(10, 5)
        )
        self.style.map(
            "Custom.TMenubutton",
            background=[("active", colors["card_hover"])],
            foreground=[("active", colors["primary_container"])]
        )

    def _create_widgets(self):
        colors = self.theme.colors
        self.main_container = tk.Frame(self.root, bg=colors["bg"])
        self.main_container.pack(fill="both", expand=True)

        # SIDEBAR
        self.sidebar = tk.Frame(
            self.main_container,
            bg=colors["surface_dim"],
            width=220,
            highlightbackground=colors["card_border"],
            highlightthickness=1
        )
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)
        self.sidebar.pack_propagate(False)

        # Branding
        self.brand_frame = tk.Frame(self.sidebar, bg=colors["surface_dim"])
        self.brand_frame.pack(fill="x", padx=16, pady=(20, 24))

        self.brand_logo = tk.Label(
            self.brand_frame,
            text="⚡ STEALTH",
            font=("Segoe UI", 14, "bold"),
            fg=colors["primary_container"],
            bg=colors["surface_dim"]
        )
        self.brand_logo.pack(anchor="w")

        self.brand_sub = tk.Label(
            self.brand_frame,
            text="CLICKER PRO",
            font=("Segoe UI", 11, "bold"),
            fg=colors["text_muted"],
            bg=colors["surface_dim"]
        )
        self.brand_sub.pack(anchor="w")

        # Sidebar Tabs
        self.nav_buttons = {}
        nav_items = [
            ("dashboard", "❖  Dashboard"),
            ("anticheat", "🛡  Anti-Cheat"),
            ("presets", "⚡  Presets"),
            ("settings", "⚙  Settings")
        ]

        self.current_tab = "dashboard"

        for key, label in nav_items:
            btn = tk.Button(
                self.sidebar,
                text=label,
                font=("Segoe UI", 9, "bold"),
                anchor="w",
                padx=16,
                pady=10,
                bd=0,
                cursor="hand2",
                bg=colors["active_cyan_bg"] if key == "dashboard" else colors["surface_dim"],
                fg=colors["primary_container"] if key == "dashboard" else colors["text_muted"],
                activebackground=colors["card_hover"],
                activeforeground=colors["primary"],
                command=lambda k=key: self.switch_tab(k)
            )
            btn.pack(fill="x", padx=10, pady=3)
            self.nav_buttons[key] = btn

        # Sidebar Footer
        self.sidebar_footer = tk.Frame(self.sidebar, bg=colors["surface_dim"])
        self.sidebar_footer.pack(side="bottom", fill="x", padx=10, pady=16)

        self.theme_toggle_btn = tk.Button(
            self.sidebar_footer,
            text="🌙  Dark Mode",
            font=("Segoe UI", 9, "bold"),
            bd=1,
            relief="solid",
            highlightbackground=colors["card_border"],
            bg=colors["btn_default_bg"],
            fg=colors["text_main"],
            activebackground=colors["card_hover"],
            activeforeground=colors["primary_container"],
            cursor="hand2",
            command=self.toggle_theme
        )
        self.theme_toggle_btn.pack(fill="x", ipady=6, pady=(0, 12))

        os_name = "Windows" if IS_WINDOWS else ("Linux" if IS_LINUX else "Cross-Platform")
        self.version_lbl = tk.Label(
            self.sidebar_footer,
            text=f"v3.0 Pro Modular\nEngine: {os_name} Native",
            font=("Segoe UI", 8),
            fg=colors["text_muted"],
            bg=colors["surface_dim"],
            justify="left"
        )
        self.version_lbl.pack(anchor="w")

        # MAIN CONTENT AREA
        self.content_area = tk.Frame(self.main_container, bg=colors["bg"])
        self.content_area.pack(side="right", fill="both", expand=True, padx=20, pady=16)

        # Pages
        self.pages = {
            "dashboard": DashboardPage(self.content_area, self),
            "anticheat": AntiCheatPage(self.content_area, self),
            "presets": PresetsPage(self.content_area, self),
            "settings": SettingsPage(self.content_area, self)
        }

        self.switch_tab("dashboard")

    def switch_tab(self, tab_key: str):
        colors = self.theme.colors
        self.current_tab = tab_key
        for k, btn in self.nav_buttons.items():
            if k == tab_key:
                btn.config(bg=colors["active_cyan_bg"], fg=colors["primary_container"])
            else:
                btn.config(bg=colors["surface_dim"], fg=colors["text_muted"])

        for page_name, page_frame in self.pages.items():
            if page_name == tab_key:
                page_frame.pack(fill="both", expand=True)
            else:
                page_frame.pack_forget()

    def toggle_theme(self):
        self.theme.toggle()
        self._apply_theme()

    def _apply_theme(self):
        colors = self.theme.colors
        self._update_ttk_styles()

        self.root.config(bg=colors["bg"])
        self.main_container.config(bg=colors["bg"])
        self.sidebar.config(bg=colors["surface_dim"], highlightbackground=colors["card_border"])
        self.brand_frame.config(bg=colors["surface_dim"])
        self.brand_logo.config(fg=colors["primary_container"], bg=colors["surface_dim"])
        self.brand_sub.config(fg=colors["text_muted"], bg=colors["surface_dim"])
        self.sidebar_footer.config(bg=colors["surface_dim"])
        self.version_lbl.config(fg=colors["text_muted"], bg=colors["surface_dim"])
        self.content_area.config(bg=colors["bg"])

        toggle_text = "🌙  Dark Mode" if self.theme.is_dark_mode else "☀️  Light Mode"
        self.theme_toggle_btn.config(
            text=toggle_text,
            bg=colors["btn_default_bg"],
            fg=colors["text_main"],
            highlightbackground=colors["card_border"],
            activebackground=colors["card_hover"],
            activeforeground=colors["primary_container"]
        )

        for key, btn in self.nav_buttons.items():
            if key == self.current_tab:
                btn.config(bg=colors["active_cyan_bg"], fg=colors["primary_container"])
            else:
                btn.config(bg=colors["surface_dim"], fg=colors["text_muted"])

        for page in self.pages.values():
            page.apply_theme()

    def select_preset(self, val: str):
        self.interval_ms_var.set(val)

    def _on_interval_change(self, *args):
        val = self.interval_ms_var.get()
        if hasattr(self, "pages") and "dashboard" in self.pages:
            self.pages["dashboard"].update_preset_button_styles(val)

    def _apply_window_disguise(self, *args):
        val = self.disguise_title_var.get()
        if val.startswith("Normal"):
            self.root.title("Stealth Clicker Pro")
        else:
            self.root.title(val)

    def _update_button_text(self, *args):
        hk = self.hotkey_var.get()
        if hasattr(self, "pages"):
            dash = self.pages.get("dashboard")
            if dash:
                if not self.engine.running:
                    dash.main_action_btn.config(text=f"▶  START AUTO CLICKER ({hk})")
                else:
                    dash.main_action_btn.config(text=f"⏸  STOP AUTO CLICKER ({hk})")

    def get_effective_click_type(self) -> str:
        mode = self.action_mode_var.get()
        if mode == "Mouse":
            return self.click_type_var.get()
        else:
            cust = self.custom_key_var.get().strip()
            return cust if cust else "f"

    def toggle_clicking(self):
        try:
            interval = float(self.interval_ms_var.get())
            if interval <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric interval in ms (e.g. 500).")
            return

        effective_click_type = self.get_effective_click_type()

        self.engine.toggle(
            interval_ms=interval,
            click_type=effective_click_type,
            human_mode=self.human_mode_var.get(),
            sendinput_mode=self.sendinput_mode_var.get(),
            sound_enabled=self.sound_enabled_var.get()
        )

    def emergency_stop(self):
        self.engine.emergency_stop()

    def reset_counter(self):
        self.engine.reset_counter()

    def _on_count_update(self, count: int):
        if hasattr(self, "pages"):
            dash = self.pages.get("dashboard")
            if dash:
                self.root.after(0, lambda: dash.counter_lbl.config(text=f"{count:,}"))

    def _on_state_change(self, is_running: bool):
        if not hasattr(self, "pages"):
            return

        dash = self.pages.get("dashboard")
        if not dash:
            return

        colors = self.theme.colors
        hk = self.hotkey_var.get()

        def update_ui():
            if is_running:
                dash.status_card.config(bg=colors["active_cyan_bg"], highlightbackground=colors["primary_container"])
                dash.status_inner.config(bg=colors["active_cyan_bg"])
                dash.status_txt_box.config(bg=colors["active_cyan_bg"])
                dash.status_icon.config(text="🟢", bg=colors["active_cyan_bg"])
                dash.status_text.config(text="STATUS: RUNNING", fg=colors["primary_container"], bg=colors["active_cyan_bg"])
                dash.status_sub.config(
                    text=f"Clicking every ~{self.interval_ms_var.get()} ms. Press [{self.emergency_key_var.get()}] for Emergency Break!",
                    fg=colors["text_main"],
                    bg=colors["active_cyan_bg"]
                )
                dash.main_action_btn.config(
                    text=f"⏸  STOP AUTO CLICKER ({hk})",
                    bg=colors["card_bright"],
                    fg="#ffffff" if not self.theme.is_dark_mode else colors["text_main"]
                )
            else:
                dash.status_card.config(bg=colors["card_bg"], highlightbackground=colors["error_red"])
                dash.status_inner.config(bg=colors["card_bg"])
                dash.status_txt_box.config(bg=colors["card_bg"])
                dash.status_icon.config(text="🔴", bg=colors["card_bg"])
                dash.status_text.config(text="STATUS: OFF", fg=colors["error_red"], bg=colors["card_bg"])
                dash.status_sub.config(text="Press Trigger Shortcut to Start Auto Clicker", fg=colors["text_muted"], bg=colors["card_bg"])
                dash.main_action_btn.config(
                    text=f"▶  START AUTO CLICKER ({hk})",
                    bg=colors["primary_container"],
                    fg=colors["on_primary"]
                )

        self.root.after(0, update_ui)

    def _on_close(self):
        self.engine.stop()
        if hasattr(self, "listeners"):
            self.listeners.stop()
        self.root.destroy()

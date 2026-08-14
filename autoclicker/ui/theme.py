# -*- coding: utf-8 -*-

DARK_COLORS = {
    "bg": "#111317",
    "surface_dim": "#0c0e12",
    "card_bg": "#1e2024",
    "card_border": "#3b494c",
    "card_hover": "#282a2e",
    "card_bright": "#37393e",
    "primary": "#c3f5ff",
    "primary_container": "#00e5ff",
    "on_primary": "#001f24",
    "text_main": "#e2e2e8",
    "text_muted": "#bac9cc",
    "secondary_bg": "#2a080c",
    "secondary_border": "#c7003a",
    "error_red": "#ffb4ab",
    "error_bg": "#93000a",
    "on_error": "#ffb4ab",
    "tertiary_purple": "#ecb2ff",
    "tertiary_purple_dark": "#74009f",
    "active_cyan_bg": "#002b33",
    "btn_default_bg": "#333539",
    "entry_bg": "#0c0e12"
}

LIGHT_COLORS = {
    "bg": "#f8fafc",
    "surface_dim": "#ffffff",
    "card_bg": "#ffffff",
    "card_border": "#cbd5e1",
    "card_hover": "#f1f5f9",
    "card_bright": "#334155",
    "primary": "#0284c7",
    "primary_container": "#0284c7",
    "on_primary": "#ffffff",
    "text_main": "#0f172a",
    "text_muted": "#64748b",
    "secondary_bg": "#fef2f2",
    "secondary_border": "#fca5a5",
    "error_red": "#dc2626",
    "error_bg": "#dc2626",
    "on_error": "#ffffff",
    "tertiary_purple": "#7e22ce",
    "tertiary_purple_dark": "#c084fc",
    "active_cyan_bg": "#e0f2fe",
    "btn_default_bg": "#e2e8f0",
    "entry_bg": "#ffffff"
}

class ThemeManager:
    def __init__(self, is_dark_mode: bool = True):
        self.is_dark_mode = is_dark_mode

    @property
    def colors(self) -> dict:
        return DARK_COLORS if self.is_dark_mode else LIGHT_COLORS

    def toggle(self) -> dict:
        self.is_dark_mode = not self.is_dark_mode
        return self.colors

# -*- coding: utf-8 -*-
import json
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval_ms": "500",
    "action_mode": "Mouse",
    "click_type": "Left",
    "custom_key": "f",
    "hotkey": "F",
    "emergency_key": "ESC",
    "sound_enabled": True,
    "human_mode": True,
    "sendinput_mode": True,
    "disguise_title": "Normal (Auto Clicker)",
    "is_dark_mode": True,
}

class ConfigManager:
    @staticmethod
    def get_config_path() -> Path:
        return Path.home() / ".stealth_clicker_config.json"

    @classmethod
    def load_config(cls) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        config_path = cls.get_config_path()
        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    saved_data = json.load(f)
                    if isinstance(saved_data, dict):
                        config.update(saved_data)
            except Exception as e:
                print(f"[ConfigManager] Error loading config: {e}")
        return config

    @classmethod
    def save_config(cls, config_dict: Dict[str, Any]) -> bool:
        config_path = cls.get_config_path()
        try:
            config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config_dict, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"[ConfigManager] Error saving config: {e}")
            return False

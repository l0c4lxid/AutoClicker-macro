# -*- coding: utf-8 -*-
import time
import random
import threading
from pynput.mouse import Button as MouseButton, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from autoclicker.utils.sysinfo import IS_WINDOWS, IS_LINUX, perform_sendinput_click, perform_sendinput_key, perform_wayland_click
from autoclicker.utils.sound import play_beep

class AutoClickerEngine:
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.running = False
        self.click_count = 0
        self.click_thread = None

        # Settings
        self.interval_ms = 500.0
        self.click_type = "Left"
        self.human_mode = True
        self.sendinput_mode = True
        self.sound_enabled = True

        # Callbacks
        self.on_count_update = None
        self.on_state_change = None

    def start(self, interval_ms: float, click_type: str, human_mode: bool, sendinput_mode: bool, sound_enabled: bool):
        if self.running:
            return

        self.interval_ms = interval_ms
        self.click_type = click_type
        self.human_mode = human_mode
        self.sendinput_mode = sendinput_mode
        self.sound_enabled = sound_enabled

        self.running = True

        if self.sound_enabled:
            play_beep(850, 150)

        if self.on_state_change:
            self.on_state_change(True)

        self.click_thread = threading.Thread(target=self._click_loop, daemon=True)
        self.click_thread.start()

    def stop(self):
        if not self.running:
            return

        self.running = False

        if self.sound_enabled:
            play_beep(450, 150)

        if self.on_state_change:
            self.on_state_change(False)

    def emergency_stop(self):
        """Halts clicking immediately with emergency audio alert."""
        if self.running:
            self.running = False
            if self.on_state_change:
                self.on_state_change(False)

            if self.sound_enabled:
                def play_emergency_beep():
                    play_beep(1000, 100)
                    play_beep(1000, 100)
                    play_beep(1000, 200)
                threading.Thread(target=play_emergency_beep, daemon=True).start()

    def toggle(self, interval_ms: float, click_type: str, human_mode: bool, sendinput_mode: bool, sound_enabled: bool):
        if self.running:
            self.stop()
        else:
            self.start(interval_ms, click_type, human_mode, sendinput_mode, sound_enabled)

    def reset_counter(self):
        self.click_count = 0
        if self.on_count_update:
            self.on_count_update(0)

    def _click_loop(self):
        btn_map = {
            "Left": MouseButton.left,
            "Right": MouseButton.right,
            "Middle": MouseButton.middle
        }

        while self.running:
            base_delay_sec = max(0.001, self.interval_ms / 1000.0)

            # 1. Human Mode Jitter Calculation
            if self.human_mode:
                jitter = random.uniform(0.92, 1.08)
                actual_delay = max(0.001, base_delay_sec * jitter)
                hold_duration = random.uniform(0.025, 0.050)
            else:
                actual_delay = base_delay_sec
                hold_duration = 0.020

            # 2. Execution (Mouse vs Keyboard Key)
            c_type = self.click_type.strip()
            if c_type in btn_map:
                # Mouse Click
                if self.sendinput_mode and IS_WINDOWS:
                    perform_sendinput_click(c_type, hold_duration)
                elif self.sendinput_mode and IS_LINUX:
                    perform_wayland_click(c_type, hold_duration)
                else:
                    selected_btn = btn_map.get(c_type, MouseButton.left)
                    self.mouse.press(selected_btn)
                    time.sleep(hold_duration)
                    self.mouse.release(selected_btn)
            else:
                # Keyboard Key Press
                target_key = c_type.replace("Key:", "").strip()
                sendinput_done = False
                if self.sendinput_mode and IS_WINDOWS:
                    sendinput_done = perform_sendinput_key(target_key, hold_duration)

                if not sendinput_done:
                    key_clean = target_key.lower()
                    key_map = {
                        "space": Key.space, "spasi": Key.space, "enter": Key.enter,
                        "tab": Key.tab, "shift": Key.shift, "ctrl": Key.ctrl,
                        "alt": Key.alt, "backspace": Key.backspace, "esc": Key.esc
                    }
                    if key_clean in key_map:
                        key_obj = key_map[key_clean]
                    elif key_clean.startswith("f") and key_clean[1:].isdigit():
                        key_obj = getattr(Key, key_clean, key_clean)
                    elif len(key_clean) == 1:
                        key_obj = key_clean
                    else:
                        key_obj = key_clean

                    try:
                        self.keyboard.press(key_obj)
                        time.sleep(hold_duration)
                        self.keyboard.release(key_obj)
                    except Exception as e:
                        print(f"[Warning] Keyboard press execution exception: {e}")

            self.click_count += 1

            if self.on_count_update:
                self.on_count_update(self.click_count)

            # High-precision sleep loop for instant emergency break responsiveness
            elapsed = 0.0
            step = 0.01
            while self.running and elapsed < actual_delay:
                time.sleep(step)
                elapsed += step


# -*- coding: utf-8 -*-
import time
import random
import threading
from pynput.mouse import Button as MouseButton, Controller as MouseController
from autoclicker.utils.platform import IS_WINDOWS, perform_sendinput_click
from autoclicker.utils.sound import play_beep

class AutoClickerEngine:
    def __init__(self):
        self.mouse = MouseController()
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

            # 2. Click Execution (Windows SendInput vs pynput)
            if self.sendinput_mode and IS_WINDOWS:
                perform_sendinput_click(self.click_type, hold_duration)
            else:
                selected_btn = btn_map.get(self.click_type, MouseButton.left)
                self.mouse.press(selected_btn)
                time.sleep(hold_duration)
                self.mouse.release(selected_btn)

            self.click_count += 1

            if self.on_count_update:
                self.on_count_update(self.click_count)

            # High-precision sleep loop for instant emergency break responsiveness
            elapsed = 0.0
            step = 0.01
            while self.running and elapsed < actual_delay:
                time.sleep(step)
                elapsed += step

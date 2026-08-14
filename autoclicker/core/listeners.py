# -*- coding: utf-8 -*-
from pynput.mouse import Button as MouseButton, Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener

class GlobalInputListeners:
    def __init__(self, get_hotkey_func, get_emergency_key_func, on_toggle_func, on_emergency_func):
        self.get_hotkey_func = get_hotkey_func
        self.get_emergency_key_func = get_emergency_key_func
        self.on_toggle_func = on_toggle_func
        self.on_emergency_func = on_emergency_func

        self.keyboard_listener = None
        self.mouse_listener = None

    def start(self):
        def on_key_press(key):
            target_hk = self.get_hotkey_func()
            break_hk = self.get_emergency_key_func()

            # 1. Emergency Break Key Check
            if break_hk == "ESC" and key == Key.esc:
                self.on_emergency_func()
                return
            elif break_hk == "F12" and key == Key.f12:
                self.on_emergency_func()
                return
            elif break_hk == "Pause/Break" and key == Key.pause:
                self.on_emergency_func()
                return

            if key == Key.esc:
                self.on_emergency_func()
                return

            # 2. Trigger Hotkey Check
            hk_map = {
                "F6": Key.f6,
                "F8": Key.f8,
                "F9": Key.f9,
                "F10": Key.f10,
                "F11": Key.f11,
                "Space": Key.space
            }

            if target_hk in hk_map and key == hk_map[target_hk]:
                self.on_toggle_func()

        def on_mouse_click(x, y, button, pressed):
            target_hk = self.get_hotkey_func()
            if pressed and target_hk == "Mouse Side (X1/X2)":
                if button in (MouseButton.x1, MouseButton.x2):
                    self.on_toggle_func()
            elif pressed and target_hk == "Middle Mouse":
                if button == MouseButton.middle:
                    self.on_toggle_func()

        try:
            self.keyboard_listener = KeyboardListener(on_press=on_key_press)
            self.mouse_listener = MouseListener(on_click=on_mouse_click)

            self.keyboard_listener.daemon = True
            self.mouse_listener.daemon = True

            self.keyboard_listener.start()
            self.mouse_listener.start()
        except Exception as e:
            print(f"[Warning] Global listeners initialization notice: {e}")

    def stop(self):
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        if self.mouse_listener:
            self.mouse_listener.stop()

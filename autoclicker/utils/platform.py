# -*- coding: utf-8 -*-
import sys
import os
import ctypes

IS_WINDOWS = sys.platform.startswith("win")
IS_LINUX = sys.platform.startswith("linux")

if IS_WINDOWS:
    from ctypes import wintypes

    INPUT_MOUSE = 0
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004
    MOUSEEVENTF_RIGHTDOWN = 0x0008
    MOUSEEVENTF_RIGHTUP = 0x0010
    MOUSEEVENTF_MIDDLEDOWN = 0x0020
    MOUSEEVENTF_MIDDLEUP = 0x0040

    class MOUSEINPUT(ctypes.Structure):
        _fields_ = [
            ("dx", wintypes.LONG),
            ("dy", wintypes.LONG),
            ("mouseData", wintypes.DWORD),
            ("dwFlags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG)),
        ]

    class INPUT_UNION(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]

    class INPUT(ctypes.Structure):
        _fields_ = [
            ("type", wintypes.DWORD),
            ("u", INPUT_UNION),
        ]

def perform_sendinput_click(click_type: str, hold_duration: float):
    """Executes a low-level Windows SendInput API click (DirectInput Game Evasion)."""
    if not IS_WINDOWS:
        return False

    flags = {
        "Left": (MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP),
        "Right": (MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP),
        "Middle": (MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP),
    }
    down_flag, up_flag = flags.get(click_type, (MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP))

    extra = ctypes.c_ulong(0)
    ii_down = INPUT(type=INPUT_MOUSE, u=INPUT_UNION(mi=MOUSEINPUT(0, 0, 0, down_flag, 0, ctypes.pointer(extra))))
    ii_up = INPUT(type=INPUT_MOUSE, u=INPUT_UNION(mi=MOUSEINPUT(0, 0, 0, up_flag, 0, ctypes.pointer(extra))))

    ctypes.windll.user32.SendInput(1, ctypes.pointer(ii_down), ctypes.sizeof(ii_down))
    import time
    time.sleep(hold_duration)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(ii_up), ctypes.sizeof(ii_up))
    return True

def perform_sendinput_key(key_str: str, hold_duration: float):
    """Executes a low-level Windows keyboard event (DirectInput Game Evasion)."""
    if not IS_WINDOWS:
        return False

    import time
    key_str_clean = key_str.strip().lower()
    
    vk_map = {
        "space": 0x20, "spasi": 0x20, "enter": 0x0D, "tab": 0x09,
        "backspace": 0x08, "esc": 0x1B, "escape": 0x1B,
        "shift": 0x10, "ctrl": 0x11, "alt": 0x12,
        "f1": 0x70, "f2": 0x71, "f3": 0x72, "f4": 0x73,
        "f5": 0x74, "f6": 0x75, "f7": 0x76, "f8": 0x77,
        "f9": 0x78, "f10": 0x79, "f11": 0x7A, "f12": 0x7B
    }

    if key_str_clean in vk_map:
        vk = vk_map[key_str_clean]
    elif len(key_str_clean) == 1:
        res = ctypes.windll.user32.VkKeyScanW(ord(key_str_clean))
        if res == -1:
            return False
        vk = res & 0xFF
    else:
        return False

    KEYEVENTF_KEYUP = 0x0002
    ctypes.windll.user32.keybd_event(vk, 0, 0, 0)
    time.sleep(hold_duration)
    ctypes.windll.user32.keybd_event(vk, 0, KEYEVENTF_KEYUP, 0)
    return True

def get_asset_path(relative_path: str) -> str:
    """Gets absolute path to asset, handling PyInstaller bundle path (sys._MEIPASS)."""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return os.path.join(base_path, relative_path)

def set_window_icon(root):
    """Sets window icon for Tkinter root window if icon exists."""
    import os
    try:
        ico_path = get_asset_path(os.path.join("assets", "icon.ico"))
        png_path = get_asset_path(os.path.join("assets", "icon.png"))
        if IS_WINDOWS and os.path.exists(ico_path):
            root.iconbitmap(ico_path)
        elif os.path.exists(png_path):
            from tkinter import PhotoImage
            img = PhotoImage(file=png_path)
            root.iconphoto(True, img)
    except Exception as e:
        pass

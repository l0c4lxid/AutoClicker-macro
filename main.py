# -*- coding: utf-8 -*-
"""
Stealth Clicker Pro - Main Entry Point
Cross-Platform Auto Clicker Application with Anti-Cheat Evasion, Human Jitter, and Theme Switching.
"""

import tkinter as tk
from autoclicker.ui import AutoClickerApp

def main():
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

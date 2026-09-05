# -*- coding: utf-8 -*-
import sys
import threading
from autoclicker.utils.sysinfo import IS_WINDOWS

def play_beep(freq: int, duration_ms: int, enabled: bool = True):
    """Cross-platform audio beep handler (Windows winsound / Linux bell)."""
    if not enabled:
        return

    def beep_worker():
        if IS_WINDOWS:
            try:
                import winsound
                winsound.Beep(freq, duration_ms)
            except Exception:
                pass
        else:
            try:
                sys.stdout.write('\a')
                sys.stdout.flush()
            except Exception:
                pass

    threading.Thread(target=beep_worker, daemon=True).start()

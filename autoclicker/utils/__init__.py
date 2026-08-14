# -*- coding: utf-8 -*-
from .platform import IS_WINDOWS, IS_LINUX, perform_sendinput_click
from .sound import play_beep

__all__ = ["IS_WINDOWS", "IS_LINUX", "perform_sendinput_click", "play_beep"]

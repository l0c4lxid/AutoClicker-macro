@echo off
title Stealth Clicker Pro Launcher
cd /d "%~dp0"
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred while launching Stealth Clicker Pro.
    pause
)

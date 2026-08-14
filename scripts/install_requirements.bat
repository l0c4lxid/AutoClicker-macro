@echo off
title Install Dependensi Python Auto Clicker
cd /d "%~dp0\.."
echo ========================================================
echo   Installing requirements for Python Auto Clicker...
echo ========================================================
pip install -r requirements.txt
echo.
echo Pemasangan selesai! Silakan jalankan run_autoclicker.bat
pause

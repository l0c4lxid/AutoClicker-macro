@echo off
title Stealth Clicker Pro - Windows App Builder
cd /d "%~dp0"
echo ========================================================
echo   Stealth Clicker Pro - Building Windows Application (.exe)
echo ========================================================
echo.
python scripts/build_app.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Process failed with error code %ERRORLEVEL%
    pause
    exit /b %ERRORLEVEL%
)
echo.
echo Executable successfully generated inside 'dist' folder!
pause

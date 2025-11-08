@echo off
title PS3 Compatibility Checker - Flask
echo ============================================
echo   Starting PS3 Compatibility Checker server
echo ============================================

REM Activate virtual environment if it exists
if exist venv\Scripts\activate (
    echo Activating virtual environment...
    call venv\Scripts\activate
) else (
    echo No virtual environment found. Installing dependencies globally.
)

REM Install Flask if missing
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Flask not found. Installing Flask...
    pip install flask
)

echo.
echo Launching Flask server...
echo (Press CTRL + C to stop)
echo.

python app.py

echo.
pause

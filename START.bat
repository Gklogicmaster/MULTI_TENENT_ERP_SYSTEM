@echo off
echo ========================================
echo ERP SYSTEM - AUTO START
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Testing database...
python test_login_quick.py
if errorlevel 1 (
    echo.
    echo [ERROR] Database issue! Reinitializing...
    python init_demo_data.py
)

echo.
echo [2/3] Verifying system...
python system_check.py
if errorlevel 1 (
    echo.
    echo [ERROR] System check failed!
    pause
    exit /b 1
)

echo.
echo [3/3] Starting server...
echo.
echo ========================================
echo SERVER RUNNING ON http://localhost:8000
echo ========================================
echo.
echo NOW OPEN IN BROWSER:
echo   vscode\index.html
echo.
echo LOGIN WITH:
echo   LAID: S101-ABC123
echo   Password: student123
echo.
echo KEEP THIS WINDOW OPEN!
echo Press Ctrl+C to stop
echo ========================================
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

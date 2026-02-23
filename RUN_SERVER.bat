@echo off
echo ================================================
echo ERP System - Starting Backend Server
echo ================================================
echo.

cd /d "%~dp0"

echo Checking setup...
python test_setup.py
if errorlevel 1 (
    echo.
    echo ERROR: Setup check failed!
    echo Please run: python init_demo_data.py
    pause
    exit /b 1
)

echo.
echo ================================================
echo Starting server on http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo ================================================
echo.
echo KEEP THIS WINDOW OPEN!
echo Press Ctrl+C to stop the server
echo.
echo Now open in browser:
echo   vscode\index.html  OR  admin\index.html
echo.
echo Login with:
echo   LAID: S101-ABC123
echo   Password: student123
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

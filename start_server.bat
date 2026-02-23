@echo off
echo ========================================
echo ERP Backend Server Startup
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Checking database...
python test_setup.py
if errorlevel 1 (
    echo.
    echo ERROR: Database test failed!
    echo Run: python init_demo_data.py
    pause
    exit /b 1
)

echo.
echo [2/3] Starting server...
echo.
echo Server will run at: http://localhost:8000
echo API Docs at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause

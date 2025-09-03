
@echo off
echo Starting Me-API Playground...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if virtual environment exists and create if not
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Seed database if it doesn't exist
if not exist "me_api.db" (
    echo Seeding database with sample data...
    python seed_data.py
)

REM Start the server
echo.
echo Starting FastAPI server...
echo API will be available at: http://localhost:8001
echo Frontend will be available at: http://localhost:8001/static/index.html
echo API Documentation at: http://localhost:8001/docs
echo.
uvicorn main:app --host 127.0.0.1 --port 8001 --reload

=======
@echo off
echo Starting Me-API Playground...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if virtual environment exists and create if not
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Seed database if it doesn't exist
if not exist "me_api.db" (
    echo Seeding database with sample data...
    python seed_data.py
)

REM Start the server
echo.
echo Starting FastAPI server...
echo API will be available at: http://localhost:8001
echo Frontend will be available at: http://localhost:8001/static/index.html
echo API Documentation at: http://localhost:8001/docs
echo.
uvicorn main:app --host 127.0.0.1 --port 8001 --reload

>>>>>>> ac3d1a1848664a93ad8763713f315124e9e6f55e
pause
@echo off
REM 🐍 Python Virtual Environment Setup Script for Penny Stock Gainers App (Windows)
REM This script creates and configures a virtual environment for local development

echo 🐍 Setting up Python Virtual Environment for Penny Stock Gainers App...
echo ==================================================================

REM Check if Python 3 is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found!
    echo Please install Python 3.8 or higher first
    pause
    exit /b 1
)

python --version
echo ✅ Python found

REM Check if virtualenv is available
python -m venv --help >nul 2>&1
if errorlevel 1 (
    echo ❌ Python venv module not available!
    echo Please install python3-venv package
    pause
    exit /b 1
)

REM Create virtual environment
echo 🔧 Creating virtual environment...
python -m venv venv

if errorlevel 1 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
) else (
    echo ✅ Virtual environment created successfully
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
) else (
    echo ✅ Virtual environment activated
    echo 🐍 Python path: %where python%
    echo 📦 Pip path: %where pip%
)

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r api\requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
) else (
    echo ✅ Dependencies installed successfully
)

REM Create activation script for easy use
echo 📝 Creating activation script...
(
echo @echo off
echo REM Quick activation script for the virtual environment
echo echo 🐍 Activating Penny Stock App Virtual Environment...
echo call venv\Scripts\activate.bat
echo echo ✅ Virtual environment activated!
echo echo 🚀 You can now run: python start_app.py
echo echo.
echo echo 💡 To deactivate, run: deactivate
echo pause
) > activate-venv.bat

REM Create deactivation reminder
echo 📝 Creating deactivation reminder...
(
echo 🐍 Virtual Environment Setup Complete!
echo.
echo ✅ Virtual environment created: venv\
echo ✅ Dependencies installed
echo ✅ Activation script created: activate-venv.bat
echo.
echo 🚀 How to use:
echo.
echo 1. Activate the environment:
echo    venv\Scripts\activate.bat
echo    # OR
echo    activate-venv.bat
echo.
echo 2. Run the app:
echo    python start_app.py
echo.
echo 3. Deactivate when done:
echo    deactivate
echo.
echo 💡 Tips:
echo - Always activate the venv before running the app
echo - Use 'pip list' to see installed packages
echo - Use 'pip freeze ^> requirements.txt' to update requirements
) > deactivate-reminder.txt

echo.
echo 🎉 Virtual Environment Setup Complete!
echo.
echo 📱 Next steps:
echo 1. Activate the environment: venv\Scripts\activate.bat
echo 2. Run the app: python start_app.py
echo 3. Deactivate when done: deactivate
echo.
echo 📝 See deactivate-reminder.txt for detailed instructions
echo.
echo 🐍 Happy coding!
pause

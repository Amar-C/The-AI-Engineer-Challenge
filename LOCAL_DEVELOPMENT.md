# 🐍 Local Development Guide for Penny Stock Gainers App

Ready to develop locally? This guide will get you up and running with a clean, isolated Python environment! 🚀

## 🎯 What We're Setting Up

A local development environment that:
- ✅ **Isolates Dependencies**: No conflicts with system Python packages
- ✅ **Easy Activation**: Simple commands to start/stop development
- ✅ **Cross-Platform**: Works on macOS, Linux, and Windows
- ✅ **Production Ready**: Matches the Vercel deployment environment

## 🛠️ Prerequisites

Before we start, make sure you have:
- **Python 3.8+** installed on your system
- **Git** for version control
- **Terminal/Command Prompt** access

### Check Your Python Installation
```bash
# Check Python version
python3 --version  # macOS/Linux
python --version   # Windows

# Should show Python 3.8.0 or higher
```

## 🚀 Quick Setup (Choose Your Platform)

### **macOS & Linux Users**
```bash
# Make the script executable and run it
chmod +x setup-venv.sh
./setup-venv.sh
```

### **Windows Users**
```cmd
# Run the batch script
setup-venv.bat
```

### **Manual Setup (Advanced Users)**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows

# Install dependencies
pip install -r api/requirements.txt
```

## 🔌 Using Your Virtual Environment

### **Activate the Environment**
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate.bat

# Or use the quick scripts
./activate-venv.sh      # macOS/Linux
activate-venv.bat       # Windows
```

### **Verify Activation**
```bash
# Check Python path (should point to venv)
which python  # macOS/Linux
where python  # Windows

# Check pip path
which pip     # macOS/Linux
where pip     # Windows

# Should show paths inside your venv directory
```

### **Deactivate When Done**
```bash
deactivate
```

## 🚀 Running the App Locally

### **1. Start the Backend**
```bash
# Make sure venv is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows

# Start the FastAPI server
cd api
python app.py
```

**Backend will be available at:** `http://localhost:8000`

### **2. Start the Frontend**
```bash
# In a new terminal, activate venv again
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows

# Start frontend server
cd frontend
python -m http.server 8001
```

**Frontend will be available at:** `http://localhost:8001`

### **3. Use the Startup Script (Recommended)**
```bash
# Make sure venv is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows

# Run the startup script
python start_app.py
```

**This starts both backend and frontend automatically!**

## 📱 Accessing Your App

Once running, you can access:
- **Frontend App**: http://localhost:8001
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## 🔧 Development Workflow

### **Daily Development**
```bash
# 1. Activate environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows

# 2. Make your changes
# 3. Test locally
python start_app.py

# 4. Deactivate when done
deactivate
```

### **Adding New Dependencies**
```bash
# Activate venv
source venv/bin/activate

# Install new package
pip install new-package

# Update requirements.txt
pip freeze > api/requirements.txt

# Deactivate
deactivate
```

### **Updating Dependencies**
```bash
# Activate venv
source venv/bin/activate

# Update all packages
pip install --upgrade -r api/requirements.txt

# Deactivate
deactivate
```

## 🚨 Troubleshooting

### **Issue: "Command not found: python3"**
**Solution**: Install Python 3.8+ from [python.org](https://python.org)

### **Issue: "No module named 'venv'"**
**Solution**: Install python3-venv package
```bash
# Ubuntu/Debian
sudo apt-get install python3-venv

# macOS (with Homebrew)
brew install python3

# Windows: Should be included with Python installer
```

### **Issue: "Permission denied" on setup script**
**Solution**: Make script executable
```bash
chmod +x setup-venv.sh
```

### **Issue: "Port already in use"**
**Solution**: Kill existing processes or use different ports
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

## 📊 Virtual Environment Benefits

### **Why Use a Virtual Environment?**
- 🚫 **No Conflicts**: Won't interfere with system Python packages
- 🔒 **Isolation**: Each project has its own dependencies
- 📦 **Clean Install**: Fresh start for each project
- 🎯 **Reproducible**: Same environment across different machines
- 🚀 **Production Match**: Matches Vercel deployment environment

### **What Gets Installed**
- **FastAPI**: Modern web framework
- **yfinance**: Yahoo Finance API wrapper
- **pandas**: Data manipulation
- **uvicorn**: ASGI server
- **pydantic**: Data validation
- **requests**: HTTP library

## 🔄 Updating Your Environment

### **When to Update**
- After pulling new code changes
- When requirements.txt changes
- When adding new features

### **How to Update**
```bash
# Activate venv
source venv/bin/activate

# Pull latest code
git pull origin main

# Update dependencies
pip install -r api/requirements.txt

# Test the app
python start_app.py
```

## 💡 Pro Tips

### **Development Efficiency**
- 🚀 **Use the startup script**: `python start_app.py` handles everything
- 🔄 **Auto-reload**: FastAPI automatically reloads on code changes
- 📱 **Mobile testing**: Test responsive design on different screen sizes
- 🐛 **Debug mode**: FastAPI provides detailed error messages

### **Code Quality**
- 📝 **Format code**: Use `black` or `autopep8` for consistent formatting
- ✅ **Run tests**: Add tests to ensure code quality
- 🔍 **Linting**: Use `flake8` or `pylint` for code analysis
- 📚 **Documentation**: Keep docstrings and comments up to date

## 🎉 You're Ready!

Your local development environment is now set up and ready for:
- 🚀 **Local Development**: Code, test, and iterate quickly
- 🔧 **Debugging**: Easy troubleshooting and testing
- 📱 **Frontend Testing**: Responsive design validation
- 🔌 **API Testing**: Backend endpoint validation
- 🚀 **Production Deployment**: Same environment as Vercel

---

**Happy coding! 🐍** Your penny stock app is ready for local development! 🚀

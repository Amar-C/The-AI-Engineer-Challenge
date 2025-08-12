#!/usr/bin/env python3
"""
Penny Stock Gainers App Startup Script

This script helps you start both the backend API and frontend of the penny stock app.
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path


def print_banner():
    """Print the application banner"""
    print("=" * 60)
    print("🚀 PENNY STOCK GAINERS APP")
    print("=" * 60)
    print("A comprehensive app to track top penny stock gainers")
    print("=" * 60)


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")


def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        # Try to import key dependencies
        import fastapi  # noqa: F401
        import yfinance  # noqa: F401
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r api/requirements.txt")
        return False


def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "api/requirements.txt"
        ], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False


def start_backend():
    """Start the FastAPI backend server"""
    print("🔧 Starting backend server...")
    
    # Change to api directory
    api_dir = Path("api")
    if not api_dir.exists():
        print("❌ Error: API directory not found")
        return False
    
    os.chdir(api_dir)
    
    try:
        # Start the server in background
        process = subprocess.Popen([
            sys.executable, "app.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for server to start
        time.sleep(3)
        
        # Check if server is running
        if process.poll() is None:
            print("✅ Backend server started successfully")
            print("🌐 API available at: http://localhost:8000")
            return process
        else:
            stdout, stderr = process.communicate()
            print("❌ Backend server failed to start")
            print(f"Error: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return False


def start_frontend():
    """Start the frontend server"""
    print("🎨 Starting frontend server...")
    
    # Go back to root directory
    os.chdir(Path(__file__).parent)
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Error: Frontend directory not found")
        return False
    
    try:
        # Start a simple HTTP server for the frontend
        process = subprocess.Popen([
            sys.executable, "-m", "http.server", "8001"
        ], cwd=frontend_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        time.sleep(2)
        
        if process.poll() is None:
            print("✅ Frontend server started successfully")
            print("🌐 Frontend available at: http://localhost:8001")
            return process
        else:
            stdout, stderr = process.communicate()
            print("❌ Frontend server failed to start")
            return False
            
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")
        return False


def open_browser():
    """Open the application in the default browser"""
    print("🌐 Opening application in browser...")
    try:
        webbrowser.open("http://localhost:8001")
        print("✅ Browser opened successfully")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print("Please manually navigate to: http://localhost:8001")


def main():
    """Main function to start the application"""
    print_banner()
    
    # Check Python version
    check_python_version()
    
    # Check and install dependencies if needed
    if not check_dependencies():
        print("\n📦 Installing dependencies...")
        if not install_dependencies():
            print("❌ Failed to install dependencies. Exiting.")
            sys.exit(1)
    
    print("\n🚀 Starting Penny Stock Gainers App...")
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("❌ Failed to start backend. Exiting.")
        sys.exit(1)
    
    # Start frontend
    frontend_process = start_frontend()
    if not frontend_process:
        print("❌ Failed to start frontend. Exiting.")
        backend_process.terminate()
        sys.exit(1)
    
    print("\n🎉 Application started successfully!")
    print("\n📱 How to use:")
    print("1. Backend API: http://localhost:8000")
    print("2. Frontend App: http://localhost:8001")
    print("3. API Documentation: http://localhost:8000/docs")
    
    # Open browser
    open_browser()
    
    print("\n⏹️  Press Ctrl+C to stop the application")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping application...")
        
        # Terminate processes
        if backend_process:
            backend_process.terminate()
            print("✅ Backend stopped")
        
        if frontend_process:
            frontend_process.terminate()
            print("✅ Frontend stopped")
        
        print("👋 Application stopped. Goodbye!")


if __name__ == "__main__":
    main()

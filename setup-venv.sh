#!/bin/bash

# 🐍 Python Virtual Environment Setup Script for Penny Stock Gainers App
# This script creates and configures a virtual environment for local development

echo "🐍 Setting up Python Virtual Environment for Penny Stock Gainers App..."
echo "=================================================================="

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found!"
    echo "Please install Python 3.8 or higher first"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python version: $PYTHON_VERSION"

# Check if virtualenv is available
if ! command -v python3 -m venv &> /dev/null; then
    echo "❌ Python venv module not available!"
    echo "Please install python3-venv package"
    exit 1
fi

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv

if [ $? -eq 0 ]; then
    echo "✅ Virtual environment created successfully"
else
    echo "❌ Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

if [ $? -eq 0 ]; then
    echo "✅ Virtual environment activated"
    echo "🐍 Python path: $(which python)"
    echo "📦 Pip path: $(which pip)"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r api/requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Create activation script for easy use
echo "📝 Creating activation script..."
cat > activate-venv.sh << 'EOF'
#!/bin/bash
# Quick activation script for the virtual environment
echo "🐍 Activating Penny Stock App Virtual Environment..."
source venv/bin/activate
echo "✅ Virtual environment activated!"
echo "🚀 You can now run: python start_app.py"
echo ""
echo "💡 To deactivate, run: deactivate"
EOF

chmod +x activate-venv.sh

# Create deactivation reminder
echo "📝 Creating deactivation reminder..."
cat > deactivate-reminder.txt << 'EOF'
🐍 Virtual Environment Setup Complete!

✅ Virtual environment created: venv/
✅ Dependencies installed
✅ Activation script created: activate-venv.sh

🚀 How to use:

1. Activate the environment:
   source venv/bin/activate
   # OR
   ./activate-venv.sh

2. Run the app:
   python start_app.py

3. Deactivate when done:
   deactivate

💡 Tips:
- Always activate the venv before running the app
- Use 'pip list' to see installed packages
- Use 'pip freeze > requirements.txt' to update requirements
EOF

echo ""
echo "🎉 Virtual Environment Setup Complete!"
echo ""
echo "📱 Next steps:"
echo "1. Activate the environment: source venv/bin/activate"
echo "2. Run the app: python start_app.py"
echo "3. Deactivate when done: deactivate"
echo ""
echo "📝 See deactivate-reminder.txt for detailed instructions"
echo ""
echo "🐍 Happy coding!"

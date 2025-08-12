#!/bin/bash

# 🚀 Vercel Deployment Script for Penny Stock Gainers App
# This script automates the deployment process to Vercel

echo "🚀 Starting Vercel deployment for Penny Stock Gainers App..."
echo "=================================================="

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found!"
    echo "Please install it first: npm i -g vercel"
    exit 1
fi

echo "✅ Vercel CLI found"

# Check if user is logged in
if ! vercel whoami &> /dev/null; then
    echo "🔐 Please login to Vercel first:"
    vercel login
fi

echo "✅ User authenticated"

# Check if we're in the right directory
if [ ! -f "vercel.json" ] || [ ! -f "api/app.py" ] || [ ! -f "frontend/index.html" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    echo "Make sure vercel.json, api/app.py, and frontend/index.html exist"
    exit 1
fi

echo "✅ Project structure verified"

# Ask user if they want to deploy to production
read -p "🚀 Deploy to production? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Deploying to production..."
    vercel --prod
else
    echo "🔧 Deploying to preview..."
    vercel
fi

echo ""
echo "🎉 Deployment completed!"
echo ""
echo "📱 Next steps:"
echo "1. Check your Vercel dashboard for the deployment URL"
echo "2. Test the API endpoints"
echo "3. Test the frontend"
echo "4. Share your app with the world!"
echo ""
echo "🔗 Useful URLs:"
echo "- Frontend: https://your-app.vercel.app"
echo "- API: https://your-app.vercel.app/api/*"
echo "- API Docs: https://your-app.vercel.app/docs"
echo ""
echo "Happy trading! 📈"

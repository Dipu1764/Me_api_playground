#!/bin/bash

echo "🚀 Building Me-API Playground for Render deployment..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create and seed database
echo "🗄️ Setting up database..."
python seed_data.py

echo "✅ Build completed successfully!"
echo "🎯 Ready for deployment on Render!"
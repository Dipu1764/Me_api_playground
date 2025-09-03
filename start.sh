#!/bin/bash

echo "Starting Me-API Playground..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Seed database if it doesn't exist
if [ ! -f "me_api.db" ]; then
    echo "Seeding database with sample data..."
    python seed_data.py
fi

# Start the server
echo
echo "Starting FastAPI server..."
echo "API will be available at: http://localhost:8001"
echo "Frontend will be available at: http://localhost:8001/static/index.html"
echo "API Documentation at: http://localhost:8001/docs"
echo

uvicorn main:app --host 127.0.0.1 --port 8001 --reload
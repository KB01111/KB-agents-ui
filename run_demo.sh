#!/bin/bash

# Run the demo with appropriate Python executable
echo "Trying to run the KB-agents-ui demo..."

# Try to find Python
if command -v python3 &> /dev/null; then
    echo "Running with python3..."
    python3 demo.py
elif command -v python &> /dev/null; then
    echo "Running with python..."
    python demo.py
else
    echo "Python not found. Please install Python to run this demo."
    echo "Visit https://www.python.org/downloads/ for installation instructions."
    exit 1
fi
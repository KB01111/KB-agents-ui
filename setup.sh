#!/bin/bash

# This script attempts to set up the environment using various methods
# depending on what's available on the system

echo "Attempting to install packages using pip..."

# Try curl to download pip installer
if command -v curl &> /dev/null; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    if [ -f get-pip.py ]; then
        python get-pip.py || python3 get-pip.py
        pip install -r requirements.txt || pip3 install -r requirements.txt
    fi
fi

# Try to set the OpenAI API key
echo "Please enter your OpenAI API key:"
read OPENAI_API_KEY
export OPENAI_API_KEY=$OPENAI_API_KEY

echo "Setup complete. Now you can run: python my_project/main.py or python3 my_project/main.py"
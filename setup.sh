#!/bin/bash

# Exit immediately if a command fails
set -e

# Create virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "✅ Environment setup complete!"

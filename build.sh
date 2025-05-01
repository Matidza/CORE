#!/bin/bash

# Create and activate virtual environment
python3 -m venv /opt/venv
source /opt/venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Deactivate virtual environment
deactivate

#!/bin/bash

echo "creating venv..."
python3 -m venv venv
echo "creating venv successfully"
sleep 3
echo "."

# enter to venv
echo "activating venv..."
source venv/bin/activate
echo "activating successfully"
sleep 3
echo "."

# install requirements
echo "installing packages..."
pip install -r requirements.txt
pip list
echo "installing packages successfully"
sleep 5

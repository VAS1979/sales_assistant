#!/bin/bash

# enter to venv
source venv/bin/activate

# start program
cd ./app
uvicorn main:app --reload
echo "project starting..."

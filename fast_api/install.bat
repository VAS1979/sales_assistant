:: create venv
echo off
cls
echo creating venv...
python -m venv venv
echo creating venv successfully
timeout 3 > NUL
echo .

:: enter to venv
echo activating venv...
call venv\Scripts\activate.bat
echo activating successfully
timeout 3 > NUL
echo .

:: install requirements
echo installing packages...
pip install -r requirements.txt
pip list
echo installing packages successfully
timeout 5 > NUL
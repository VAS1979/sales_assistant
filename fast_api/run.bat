echo off
cls
:: enter to venv
call venv\Scripts\activate.bat

:: start program
cd .\app
uvicorn main:app --reload
echo project starting...

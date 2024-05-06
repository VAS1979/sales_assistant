echo off
cls
:: enter to venv
call venv\Scripts\activate.bat

:: start program
cd .\app
main.py
echo project starting...

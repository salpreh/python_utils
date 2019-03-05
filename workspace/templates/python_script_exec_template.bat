@echo off
:: Save current dir
SET currentDir=%cd%

:: Move to python env and activate it
cd /D D:\path\to\venv\parent
call "venv\Scripts\activate.bat"
cd workspace

:: If args are passed we pass it to python script
IF "%1"=="" (
python script.py
goto Executed
)
python script.py %*

:: Deactivate venv and restore folder
:Executed
cd ..
call "deactivate.bat"
cd /D %currentDir%
:: If you want confirmation to stop the execution
::pause

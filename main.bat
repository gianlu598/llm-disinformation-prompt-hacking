@echo off
REM setup
if NOT EXIST openai-env\ (
	REM create virtual environment
	python -m venv openai-env
	REM activate virtual environment
	call openai-env\Scripts\activate.bat
	REM install required libraries
	pip install -r requirements.txt
) else (
	REM activate virtual environment
	call openai-env\Scripts\activate.bat
)

REM ask for the OPENAI_API_KEY
set /p key= OPENAI API KEY: 
setx OPENAI_API_KEY %key%

REM text art
type assets\title-ascii-text-art.txt

REM execute the program
python python\main.py

pause

REM deactivate venv
call openai-env\Scripts\deactivate.bat






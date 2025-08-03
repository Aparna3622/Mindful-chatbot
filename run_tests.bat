@echo off
echo Installing requests if needed...
C:/python/python.exe -m pip install requests
echo.
echo Running chatbot tests...
C:/python/python.exe test_chatbot.py
pause

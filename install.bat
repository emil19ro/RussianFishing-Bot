@echo off
echo Descarcă Python 3.1.0
curl -o python310.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

echo Instalează Python 3.1.0
start /wait python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

echo Instalează PyAutoGUI și Keyboard
pip install pyautogui keyboard

echo Instalează OpenCV-Python
pip install opencv-python

echo Curăță fișierele temporare
del python310.exe

echo Instalare completă!
pause

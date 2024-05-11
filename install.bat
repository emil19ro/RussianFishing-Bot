@echo off
echo Descarcă Python 3.10.0
curl -o python310.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

echo Instalează Python 3.10.0
start /wait python310.exe /quiet TargetDir=C:\Python310 InstallAllUsers=1 PrependPath=1

echo Instalează PyAutoGUI și Keyboard
C:\Python310\python.exe -m pip install pyautogui keyboard

echo Instalează OpenCV-Python
C:\Python310\python.exe -m pip install opencv-python

echo Curăță fișierele temporare
del python310.exe

echo Instalare completă!
pause

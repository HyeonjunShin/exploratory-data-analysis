cd /d "%~dp0"
pyinstaller -p ../library --onefile --clean ../program/main.py --hidden-import=fearticulus_basic
cmd /k
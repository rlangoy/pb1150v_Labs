echo off

set "folderPath=..\dist"


echo Check if pyqt6-tools is installed
pyqt6-tools.exe  >nul 2>&1
Echo Errorlevel: [%errorlevel%]
if %errorlevel% neq 0 (
    echo installing Qt Designer

    python -m pip install pyqt6-tools
    echo Check if pyqt6-tools was properly installed
    pyqt6-tools.exe  >nul 2>&1
    '' Echo Errorlevel: [%errorlevel%]
    if %errorlevel% neq 0 (
    echo Error installing pyqt6-tools
    exit /b 1
    )
)

set currentDir=%cd%
set PYTHONPATH= %PYTHONPATH%;%cd%\qtDesignerPlugins\widgets


::echo PYQTDESIGNERPATH  %PYQTDESIGNERPATH%
::echo PYTHONPATH        %PYTHONPATH%

pyqt6-tools designer  -p "%cd%\qtDesignerPlugins\register"


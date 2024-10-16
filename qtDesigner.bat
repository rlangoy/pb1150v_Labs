echo off

set "folderPath=..\dist"

:: python -m pip install pyserial

echo check if 'pyserial' is installed
python -c "import pkgutil; exit(0 if pkgutil.find_loader('serial') else 1)"
if errorlevel 1 (
    echo The Python module 'pyserial' is not installed.
    echo Installing 'pyserial'...
    python -m pip install pyserial
    python -c "import pkgutil; exit(0 if pkgutil.find_loader('serial') else 1)"

    if errorlevel  1 (
        echo Failed to install the 'pyserial' module.
        exit /b 1
    ) else (
        echo The 'pyserial' module was successfully installed.
    )
) else (
    echo The Python module 'pyserial' is already installed.
)

echo check if 'matplotlib' is installed

python -c "import pkgutil; exit(0 if pkgutil.find_loader('matplotlib') else 1)"
if errorlevel 1 (
    echo The Python module 'matplotlib' is not installed.
    echo Installing 'matplotlib'...
    python -m pip install matplotlib
    python -c "import pkgutil; exit(0 if pkgutil.find_loader('matplotlib') else 1)"

    if errorlevel  1 (
        echo Failed to install the 'matplotlib' module.
        exit /b 1
    ) else (
        echo The 'matplotlib' module was successfully installed.
    )
) else (
    echo The Python module 'matplotlib' is already installed.
)



echo Check if pyqt6-tools is installed
pyqt6-tools.exe  >nul 2>&1
Echo Errorlevel: [%errorlevel%]
if %errorlevel% neq 0 (
    echo installing Qt Designer

    python -m pip install pyqt6-tools
    )
)

set currentDir=%cd%
set PYTHONPATH= %PYTHONPATH%;%cd%\qtDesignerPlugins\widgets


::echo PYQTDESIGNERPATH  %PYQTDESIGNERPATH%
::echo PYTHONPATH        %PYTHONPATH%

pyqt6-tools designer  -p "%cd%\qtDesignerPlugins\register"


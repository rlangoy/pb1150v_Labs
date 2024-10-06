@echo off



set "folderPath=..\dist"

:: Check if the folder exists
if exist "%folderPath%" (
    echo The folder dist exists no nead to create a distro 
    echo Delete to Remove the dist folder to recompile the outout 
    exit /b 0

) else (
    echo The folder dist does not exists
    echo The python program is compiled to a new binary width deps
    echo result placed in the .\dist folder
)


echo Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    exit /b 1
)

echo Check if the specified Python module pyinstaller is installed


echo Check if pyinstaller.exe is present in the system
pyinstaller --version >nul 2>&1

if %errorlevel% neq 0 (
    echo The Python module 'pyinstaller' is not installed.
    echo Installing the module 'pyinstaller'...
    python -m pip install -U pyinstaller 

    echo Check if PyInstaller is corectly installed

    :: Ignore warnings
    if %errorlevel% == 1 (
        echo Failed to install the module 'pyinstaller'.
        exit /b 1
    ) else (
        echo PyInstaller was successfully installed.
    )
) else (
    echo PyInstaller is already installed 
)

pyinstaller.exe --distpath ..\dist ..\FileEditAndSave.py  --windowed --icon="..\BlueSphere.ico" --add-data="..\folder_open_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg:." --add-data="..\save_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg:."


if %errorlevel% neq 0 (
    echo error executing pyinstaller.exe 
    exit /b 1
)

echo Python program sucessfulle created as a distro 

exit /b 0


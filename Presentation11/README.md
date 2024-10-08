

Install pyinstaller
To Install pyinstaller Run:
   pip install -U pyinstaller

Make FileEditAndSave.py as a single file run:
pyinstaller.exe FileEditAndSave.py --noconsole --add-data="folder_open_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg:." --add-data="save_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg:." --add-data="BlueSphere.ico:."

pyinstaller.exe FileEditAndSave.py  --windowed --icon="BlueSphere.ico" --add-data="folder_open_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg:." --add-data="save_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg:." --add-data="BlueSphere.ico:."
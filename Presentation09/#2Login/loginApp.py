from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6 import uic,QtGui
from loginDialog import Ui_LoginDialog   #File generated using pyuic6 -x loginDialog.ui -o loginDialog.py

"""
This class demonstrates how to import and use the `loginDialog.py` file. 
The `loginDialog.py` file was auto-generated using `pyuic6` from the `loginDialog.ui` file with the following command:
    pyuic6 -x loginDialog.ui -o loginDialog.py

Steps:
1. Use `pyuic6` to convert the UI file `loginDialog.ui` into a Python file `loginDialog.py`:
      pyuic6 -x loginDialog.ui -o loginDialog.py
2. Import the `Ui_LoginDialog` class from `loginDialog.py` using:
      from loginDialog import Ui_LoginDialog
3. The `loginDialog.py` file contains the class and widget definitions, allowing you to directly
   use them in your code.
4. The `Ui_LoginDialog` class (generated from the UI file) can be instantiated and integrated 
   into your custom classes. You can then connect signals (such as button clicks) to appropriate 
   slots (methods) within the class to define the dialog’s behavior.
"""
class loginDialog(QDialog):
    def __init__(self):
        super().__init__()

        #connect the Grpphical Interface from the file Ui_LoginDialog
        self.ui = Ui_LoginDialog()

        # initialoze the Grpphical Interface from the file Ui_LoginDialog
        self.ui.setupUi(self)

        #Connect functions to be executed on click,pressed,released
        self.ui.btnLogin.clicked.connect     (self.onLoginClicked)
        self.ui.btnVisibility.pressed.connect(self.onVisibilityPressed)
        self.ui.btnVisibility.released.connect(self.onVisibilityReleased)

        self.show()

    def onLoginClicked(self):
        print("Login Button Clicked")

    def onVisibilityPressed(self):
        print("Visibility Button onVisibilityPressed")
    def onVisibilityReleased(self):
        print("Visibility Button onVisibilityReleased")


"""
This class demonstrates how to use a UI file created in Qt Designer (loginDialog.ui)
Steps:
1. The class `loginDialog` loads the UI using the `uic.loadUi()` method.
2. Widgets within the UI file are accessed using `findChild()`, enabling
   interaction with the elements in the UI, such as buttons or text fields.
3. Signals (such as button clicks) are connected to appropriate slots (methods)
   within the class to define the behavior of the dialog.
"""
class loginDialogUsingUiFile(QDialog):

    btlVisibility : QPushButton  #Hide/Show password

    def __init__(self):
        super().__init__()

        #Load .ui dialog
        uic.loadUi("loginDialog.ui", self)

        #find and map .ui elemnts that is needed
        btnLogin            = self.findChild(QPushButton, "btnLogin")          # Find the button by its object name
        self.btnVisibility  = self.findChild(QPushButton, "btnVisibility")

        #Connect functions to be executed on click,pressed,released
        btnLogin.clicked.connect(self.onLoginClicked)
        self.btnVisibility.pressed.connect(self.onVisibilityPressed)
        self.btnVisibility.released.connect(self.onVisibilityReleased)

        self.show()

    def onLoginClicked(self):
        print("Login Button Clicked")
    def onVisibilityPressed(self):
        print("Visibility Button onVisibilityPressed")
    def onVisibilityReleased(self):
        print("Visibility Button onVisibilityReleased")


# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    #loadUi - seful for quickly testing the UI created in Qt Designer with minimal code.
    dialog=uic.loadUi('loginDialog.ui')
    dialog.show()

    #  Create/Update DialogBox that includes the UI from loginDialog.ui
    #dialog = loginDialogUsingUiFile()

    #  Create/Update DialogBox file loginDialog.py from loginDialog.ui
    #pyuic6 - x loginDialog.ui - o loginDialog.py
    #dialog = loginDialog()

    # Start the event loop.
    app.exec()               # Wait for program to be closed



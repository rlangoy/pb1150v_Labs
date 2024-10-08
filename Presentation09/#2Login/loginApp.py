from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6 import uic,QtGui
from loginDialog import Ui_LoginDialog

class loginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.show()


# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])
    #dialog=uic.loadUi('loginDialog.ui')
    dialog = loginDialog()


    # Start the event loop.
    app.exec()               # Wait for program to be closed



from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6 import uic,QtGui
 #File generated using pyuic6 -x loginDialog.ui -o loginDialog.py
import MatPlotLibWidget
# Run the program

if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    #loadUi - seful for quickly testing the UI created in Qt Designer with minimal code.
    dialog=uic.loadUi('timerWindow.ui')
    dialog.show()

    app.exec()


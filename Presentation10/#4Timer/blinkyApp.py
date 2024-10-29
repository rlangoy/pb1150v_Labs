
from PyQt6.QtWidgets import QStyleFactory,QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent,QCloseEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from blinkyWindow import Ui_blinkyWindow
from PyQt6.QtCore import QTimer

class SimpleBlinkyWindow(QMainWindow):
    # Create timer object
    timer = QTimer()

    #Counter
    cnt = 0

    def __init__(self):
        super().__init__()

        self.ui = Ui_blinkyWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Simple Blinky Window")
        self.ui.checkBox.setVisible(False)

        self.timer.timeout.connect(self.onTimer)
        self.timer.start(15)

        self.show()

    def onTimer(self):
        '''Handle timer event'''
        self.cnt += 1
        self.ui.dial.setValue(self.cnt)
        if self.cnt > 100:
            self.cnt = 0


class BlinkyWindow(QMainWindow):
    # Create timer object
    timer = QTimer()

    #Counter
    cnt = 0

    def __init__(self):
        super().__init__()

        self.ui = Ui_blinkyWindow()
        self.ui.setupUi(self)

        self.timer.timeout.connect(self.onTimer)
        self.ui.checkBox.stateChanged.connect(self.onCheckBoxChanged)

        self.show()

    def onCheckBoxChanged(self):
        '''Handle checkbox event'''
        if self.ui.checkBox.isChecked():
            self.timer.start(15)
        else:
            self.timer.stop()

    def onTimer(self):
        '''Handle timer event'''
        self.cnt += 1
        self.ui.dial.setValue(self.cnt )
        if self.cnt > 100:
            self.cnt = 0



# pyuic6 -x blinkyWindow.ui -o blinkyWindow.py

# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    #window = SimpleBlinkyWindow()   # Simple Blinkey example
    window = BlinkyWindow()         # Blinkey example using a checkbox for timer enable/disable
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed

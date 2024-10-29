from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6 import uic,QtGui
from PyQt6.QtCore import QTimer
from timerWindow import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
 #File generated using pyuic6 -x timerWindow.ui -o timerWindow.py
import MatPlotLibWidget
# Run the program

class timerWindow(QMainWindow):
    # Create timer object
    timer = QTimer()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Timer Window")

        #Update the lcd number
        self.ui.lcdNumber.display(0)


        self.timer.timeout.connect(self.onTimer)

        self.ui.verticalSlider.valueChanged.connect(self.onSliderChanged)

        self.show()

    def onTimer(self):
        '''Handle timer event'''
        pass


    def onCheckBoxChanged(self):
        '''Enable / Disable timer'''
        pass

    def onSliderChanged(self):
        '''Handle slider event'''''
        self.ui.matPlotWidget.addDataAndPlot(self.ui.verticalSlider.value())



if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    #loadUi - seful for quickly testing the UI created in Qt Designer with minimal code.
    dialog=timerWindow()
    dialog.show()

    app.exec()


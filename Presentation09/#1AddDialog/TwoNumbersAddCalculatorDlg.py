from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog, QStyle
from PyQt6.QtCore import QRect

class TwoNumbersAddCalculatorDlg(QDialog):

    txtEdNumber1 : QLineEdit
    txtEdNumber2 : QLineEdit
    txtEdAnswer  : QLineEdit
    def __init__(self):
        super().__init__()

        #Set up Dialog view
        self.setWindowTitle("Add two numbers")
        self.setGeometry(QRect(100, 30, 450, 150))
        self.setStyleSheet("QDialog { background-color: lightgray }")

        #Add widgets to Dialog
        label1     =             QLabel("+", self)
        btnAnswer =         QPushButton("=", self)
        self.txtEdNumber1 = QLineEdit("0",self)
        self.txtEdNumber2 = QLineEdit("0", self)
        self.txtEdAnswer  = QLineEdit("0", self)

        # Place widgets inside Dialog
        self.txtEdNumber1.setGeometry  (QRect(50, 30,  70, 40))
        label1.setGeometry             (QRect(125, 30, 10, 40))
        self.txtEdNumber2.setGeometry  (QRect(140, 30, 70, 40))
        btnAnswer.setGeometry          (QRect(220, 30, 50, 40))
        self.txtEdAnswer.setGeometry   (QRect(280, 30, 80, 40))

        # Add signals
        #    When  btnAnswer is clicked jump to function doCaclulation
        btnAnswer.clicked.connect(self.doCaclulation)

        #Show my dialog
        self.show()
    def doCaclulation(self):
        print("Use self.txtEdNumber1.text()) get the first number ")
        print("Use self.txtEdNumber2.text()) get the second number ")
        print("convert the strings to numbers  ")
        print("Calculate the result")
        print("convert the result to a string (strAnwer)  ")
        print("Use self.txtEdAnswer.setText(strAnwer)  to show the result ")
        strOut=F"{float(self.txtEdNumber1.text())} + {float(self.txtEdNumber2.text())} = {float(self.txtEdNumber1.text())+float(self.txtEdNumber2.text())}"
        print(strOut)
        strAnwer=F"You fix :)"
        self.txtEdAnswer.setText(strAnwer)



# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = TwoNumbersAddCalculatorDlg()   # Create QtMainWindow
    #window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed

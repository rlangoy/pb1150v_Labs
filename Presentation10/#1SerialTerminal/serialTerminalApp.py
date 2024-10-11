


from PyQt6.QtWidgets import QStyleFactory,QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6.QtCore import QRect

from serialTerminalWindow import Ui_serialTerminal
from qtSerialComp import JsonSerialConnector


class SerialTerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_serialTerminal()
        self.ui.setupUi(self)

        #Get list of available serial ports
        listOfSerialPorts=JsonSerialConnector.getSerialPortsAsList()

        self.ui.cmbSerialPorts.addItem("Select a port")
        self.ui.cmbSerialPorts.addItems(listOfSerialPorts)
        self.ui.cmbSerialPorts.addItems(["He","aa","dd"])


        self.ui.cmbSerialPorts.currentIndexChanged.connect(self.onCmbIndexChanged)

        self.show()

    def onCmbIndexChanged(self,index):
       # if self.ui.cmbSerialPorts.itemText(0) == "Select a port" and self.ui.cmbSerialPorts.currentIndex() != 0:
       #     self.ui.cmbSerialPorts.removeItem(0)
        serialPortToUse=self.ui.cmbSerialPorts.itemText(index)
        print(serialPortToUse)

        #Move to Connect...
        print("Setting up serial port")
        self.jsonConnector=JsonSerialConnector(serialPortToUse)    #Connect to serial port
        self.jsonConnector.serialDataRxSignal.connect(self.onRxSerialData)
#        if (self.ui.cmbSerialPorts.cont(["Select Com"]))

        #idx = self.ui.cmbSerialPorts.findText("Select a port")
        #self.ui.cmbSerialPorts.removeItem(idx)

    #print(index)


    def onRxSerialData(self,message):
            print(f"RecieverClass: Received  message: {message}")


#  pip install pyserial
#  Create/Update DialogBox file loginDialog.py from loginDialog.ui
# pyuic6 -x serialTerminalWindow.ui -o serialTerminalWindow.py

# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])


    window = SerialTerminalWindow()   # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed

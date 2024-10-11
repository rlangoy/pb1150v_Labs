
from PyQt6.QtWidgets import QStyleFactory,QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent,QCloseEvent
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

        #Set display Text in the Place holder
        self.ui.labSerialPortStatusConected.setVisible(False)
        self.ui.cmbSerialPorts.setPlaceholderText("Select a port")
        self.ui.cmbSerialPorts.setStyleSheet("QComboBox {color: red}")
        self.ui.cmbSerialPorts.setCurrentIndex(-1)
        self.ui.cmbSerialPorts.addItems(listOfSerialPorts)

        self.ui.cmbSerialPorts.currentIndexChanged.connect(self.onCmbIndexChanged)

        self.show()

    def onCmbIndexChanged(self,index):
        #Remove the red line
        self.ui.cmbSerialPorts.setStyleSheet("")
        serialPortToUse=self.ui.cmbSerialPorts.itemText(index)

        try :
            try :  # Try to close serial port and remove it
                   # Wil expextidly fail first time when it i not declared..
               self.jsonConnector.running = False
               self.jsonConnector.serialPort.close()
               del self.jsonConnector
            except:
                self.jsonConnector = None

            self.jsonConnector=JsonSerialConnector(serialPortToUse)    #Connect to serial port
            self.jsonConnector.serialDataRxSignal.connect(self.onRxSerialData)
            self.ui.labSerialPortStatusConected.setVisible(True)
            self.ui.labSerialPortStatusDisconnected.setVisible(False)
            self.ui.txtRecieved.setPlainText("")

        except Exception as e:
            self.ui.labSerialPortStatusConected.setVisible(False)
            self.ui.labSerialPortStatusDisconnected.setVisible(True)
            print("Error")
            print(e)

    def onRxSerialData(self,message):
            self.ui.txtRecieved.appendPlainText(str(message))

    def closeEvent(self, event: QCloseEvent):
        try:  # Try to close serial port and remove it
            # Wil expextidly fail first time when it i not declared..
            self.jsonConnector.running= False
            self.jsonConnector.serialPort.close()
            del self.jsonConnector
        except:
            self.jsonConnector = None


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

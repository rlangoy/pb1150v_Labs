
from PyQt6.QtWidgets import QStyleFactory,QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent,QCloseEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6.QtCore import QRect

from serialTerminalWindow import Ui_serialTerminal
from qtSerialComp import SerialConnector

class SerialTerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_serialTerminal()
        self.ui.setupUi(self)

        #Get list of available serial ports
        listOfSerialPorts=SerialConnector.getSerialPortsAsList()

        #Set display Text in the Place holder
        self.ui.cmbSerialCommands.setPlaceholderText("Select a macro")
        self.ui.cmbSerialCommands.addItems(['{"userLedOn": 1}','{"userLedOn": 0}'])
        self.ui.cmbSerialCommands.currentIndexChanged.connect(self.onCmbSerialCommandsIdxCh)

        self.ui.labSerialPortStatusConected.setVisible(False)
        self.ui.cmbSerialPorts.setPlaceholderText("Select a port")
        self.ui.cmbSerialPorts.setStyleSheet("QComboBox {color: red}")
        self.ui.cmbSerialPorts.setCurrentIndex(-1)
        self.ui.cmbSerialPorts.addItems(listOfSerialPorts)
        self.ui.cmbSerialPorts.currentIndexChanged.connect(self.onCmbIndexChanged)

        #Connect send button to the method onBtSend
        self.ui.btnSend.clicked.connect(self.onBtnSend)

        self.show()


    def onBtnSend(self):
        """
         Handles the action triggered when the send button is pressed.

         This method sends the text entered in the `txtToSend` text box
         to the connected serial device. The text is appended with a newline (`\n`)
         and carriage return (`\r`) characters before being sent.
        """
        print(self.ui.txtToSend.toPlainText())
        self.serialConnector.sendTextMessage(self.ui.txtToSend.toPlainText()+'\n\r')


    def onCmbSerialCommandsIdxCh(self,index):
        """
        Handles changes in the selection of the combobox `cmbSerialCommands`.

        This method reads the selected text from the combobox and places it in
        the `txtToSend` textbox. The content of `txtToSend` will be sent to the
        serial port when the `onBtnSend` button is clicked.

        Args:
            index (int): The index of the selected item in the combobox.
        """
        self.ui.txtToSend.setText(self.ui.cmbSerialCommands.itemText(index))

    def connectToSerialPort(self,serialPortToUse):
        """
        Establishes a connection to the specified serial port.

        This method attempts to connect to the provided `serialPortToUse`. If a previous
        serial connection exists, it will attempt to close and delete it before making a
        new connection. If the connection is successful, the serial port status image
        in the UI will reflect the connected state. If there is an error during the
        connection process, the status image will reflect the disconnected state.

        Args:
            serialPortToUse (str): The name of the serial port to connect to.

        Raises:
            Exception: If the connection to the serial port fails.
        """
        try:
            try:  # Try to close serial port and remove it
                # Wil expextidly fail first time when it i not declared..
                self.serialConnector.close()
                del self.serialConnector
            except:
                self.serialConnector = None

            # Connect to serial port and show it
            self.serialConnector = SerialConnector(serialPortToUse)
            self.serialConnector.serialDataRxAsDict.connect(self.onRxSerialDictData)
            self.ui.labSerialPortStatusConected.setVisible(True)
            self.ui.labSerialPortStatusDisconnected.setVisible(False)
            self.ui.txtRecieved.setPlainText("")

        except Exception as e:
            self.ui.labSerialPortStatusConected.setVisible(False)
            self.ui.labSerialPortStatusDisconnected.setVisible(True)
            print("Error")
            print(e)

    def onCmbIndexChanged(self,index):
        """
        Handles changes in the selection of the combobox `cmbSerialPorts`.

        This method reads the selected serial port name, attempts to open the serial
        port, and updates the graphical user interface accordingly.

        Args:
            index (int): The index of the selected item in the combobox.
        """
        #Remove the red line by removing the stylesheet
        self.ui.cmbSerialPorts.setStyleSheet("")
        #Get the selected serial port name
        serialPortToUse=self.ui.cmbSerialPorts.itemText(index)

        # Try to connect to serial port and
        # update the user interface
        self.connectToSerialPort(serialPortToUse)




    def onRxSerialDictData(self,message : dict):
        """
        Handles the action triggered when serial data is ready to be processed.

        This method appends the received Python dictionary to the `txtRecieved`
        text box as a string.

        Args:
            message (dict): The incoming serial data represented as a dictionary.
        """
        self.ui.txtRecieved.appendPlainText(str(message))

    def closeEvent(self, event: QCloseEvent):
        """
         Handles the windows triggered close event.

         This method disconnects the serial port
        """

        try:  # Try to close serial port and remove it
            self.serialConnector.close()
            del self.serialConnector
        except:
            self.serialConnector = None


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

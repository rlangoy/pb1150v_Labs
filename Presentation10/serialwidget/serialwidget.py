
from PyQt6.QtWidgets import QStyleFactory,QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent,QCloseEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog,QWidget
from PyQt6.QtCore import QRect

from PyQt6 import QtCore, QtGui, QtWidgets

##
#   In The Terminal install pySerial
#     pip install pyserial
#   In The Terminal install PyQt6
#     pip install PyQt6
#   In The Terminal install qt-designer
#    pip install pyqt6-tools
#
import serial
import serial.tools.list_ports
import threading
import json
from PyQt6.QtCore import QObject,pyqtSlot,QCoreApplication
from PyQt6 import QtCore
import sys
import warnings
warnings.filterwarnings('ignore')  # remove warning for python v3.10.8 (DeprecationWarning: sipPyTypeDict())


class SerialConnector(threading.Thread,QObject):
    """
    A class to manage serial port communication using PySerial.

    This class extends both `threading.Thread` and `QObject`, allowing it to
    run in a separate thread and emit signals for data received over the serial
    port. It provides methods to send text and JSON-encoded dictionary messages,
    as well as to read incoming data and notify subscribers.

    Attributes:
        serialPort (serial.Serial): The PySerial object representing the open
            serial port.
        serialDataRxAsDict (QtCore.pyqtSignal): Signal emitted when data is
            received as a Python dictionary.
        serialDataRxAsLineStr (QtCore.pyqtSignal): Signal emitted when data is
            received as a string.

    Static Methods:
        getSerialPortsAsList(): Returns a list of available serial ports.
                                 No need to instantiate the class
    Methods:
        printSerialPorts(): Prints a list of available serial ports to the console.
        run(): Continuously reads data from the serial port and emits it to
            subscribers.
        sendDictMessageAsJson(dictMessage): Sends a Python dictionary as a JSON-encoded
            string over the serial port.
        sendTextMessage(strMessage): Sends a text message over the serial port.
        close(): Stops the running thread and closes the serial port connection.

    Notes:
        - The constructor initializes the serial port connection and starts
          the thread for reading incoming data. It raises a ValueError if
          the provided serial port number is empty or invalid.
        - This class is designed to facilitate real-time data exchange
          between a device and a host computer using serial communication.
    """
    serialPort = None  # PySerial Com Port Object opened in the constructor
    serialDataRxAsDict     = QtCore.pyqtSignal(dict)
    serialDataRxAsLineStr  = QtCore.pyqtSignal(str)

    @staticmethod
    def getSerialPortsAsList():
        ports=serial.tools.list_ports.comports()
        portList = [port.device for port in ports]
        return portList
    def printSerialPorts(self):
        print('List of available Serial Ports:')
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            print('serialPort : ' + port)

    def __init__(self,serialPortNumber):
      """
            Initializes a new instance of the JsonSerialConnector class.

            This constructor sets up the serial connection using the specified
            `serialPortNumber`. It initializes threading, sets default values,
            and attempts to open the serial port. If the port number is not specified
            or if the connection fails, it raises a ValueError with an appropriate message.

            Args:
                serialPortNumber (str): The name of the serial port to connect to.

            Raises:
                ValueError: If `serialPortNumber` is an empty string or if there
                is an error while trying to open the serial port.

            Notes:
                - The method initializes threading to allow for concurrent operations.
      """
      #QObject.__init__(self)
      super(QObject, self).__init__()
      #Init threading
      threading.Thread.__init__(self)
      self.number = 1
      self.running = True

      if (serialPortNumber == ''):
            errorMsg = "The JsonSerialConnector(serialPort)\n serialPort was not specified !\n"
            errorMsg +="Please Select one of the comports\nIf you do not know try the last one :)"
            raise ValueError(errorMsg)
      try:
            self.serialPort = serial.Serial(serialPortNumber)  # open serial port
      except Exception as e:
            errorMsg=f"{e}+ \nCould not connect to {serialPortNumber}\n"
            #print(errorMsg + 'Please Select one of the serialPort listed below\nIf you do not know try the last one :)')
            #self.printSerialPorts()
            raise ValueError(errorMsg)

      self.start()

    #Thread for reading serial lines
    def run(self):
        """
        Continuously reads data from the serial port and emits it to subscribers.

        This method runs in a loop as long as `self.running` is set to True. It checks
        if there is any data available to read from the serial port. If data is available,
        it reads a line from the serial port, emits the line as a string to subscribers,

        Notes:
            - This method is started from the construtor
            - Subscribers should connect to the `serialDataRxAsLineStr` and `serialDataRxAsDict` signals
              inorder to receive the emitted data.
        """
        while self.running :
            if(self.serialPort.inWaiting()>0):
                serialInputStringAsLine = self.serialPort.readline()
                #send data as string to subscribers
                self.serialDataRxAsLineStr.emit(str(serialInputStringAsLine))
                serialInputAsDictionary = json.loads(serialInputStringAsLine)
                #send data ad python dictionary to subscribers
                self.serialDataRxAsDict.emit(serialInputAsDictionary)

    def sendDictMessageAsJson(self,dictMessage):
        """
        Sends a Python dictionary as a JSON-encoded string over the serial port.

        This method converts the provided dictionary (`dictMessage`) into a JSON string,
        encodes it in UTF-8, and sends it over the connected serial port.

        Args:
            dictMessage (dict): The dictionary containing the message to be sent.

        Raises:
            TypeError: If `dictMessage` is not serializable to JSON.
        """
        message=json.dumps(dictMessage)
        self.serialPort.write(message.encode('utf-8'))

    def sendTextMessage(self,strMessage):
        """
        Sends a text message over the serial port.

        This method encodes the provided string (`strMessage`) in UTF-8 and sends it
        over the connected serial port.

        Args:
            strMessage (str): The text message to be sent.

        Raises:
            AttributeError: If the serial port is not properly initialized or connected.
        """
        self.serialPort.write(strMessage.encode('utf-8'))

    #Close the component by stoping the thread and close the serial port
    def close(self):
        """
        Stops the running thread and closes the serial port connection.

        This method sets the `running` attribute to False to stop the thread from
        executing further. If a serial port connection exists, it will be closed.

        Notes:
            - This method should be called to ensure proper cleanup and
              resource management before the object is destroyed or
              the application is closed.
        """
        #Stop the thread from  running
        self.running = False
        if(self.serialPort ):
          self.serialPort.close()


class SerialTerminalWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.placeUi()

        #Get list of available serial ports
        listOfSerialPorts=SerialConnector.getSerialPortsAsList()

        self.labSerialPortStatusConected.setVisible(False)

        self.cmbSerialPorts.setPlaceholderText("Select a port")
        self.cmbSerialPorts.setStyleSheet("QComboBox {color: red}")
        self.cmbSerialPorts.setCurrentIndex(-1)
        self.cmbSerialPorts.addItems(listOfSerialPorts)
        self.cmbSerialPorts.currentIndexChanged.connect(self.onCmbIndexChanged)

        self.show()


    def placeUi(self):
        self.labSerialPortStatusConected = QtWidgets.QLabel(self)
        self.labSerialPortStatusConected.setGeometry(QtCore.QRect(0, 4, 32, 32))
        self.labSerialPortStatusConected.setText("")
        self.labSerialPortStatusConected.setPixmap(QtGui.QPixmap("electrical_services.svg"))
        self.labSerialPortStatusConected.setScaledContents(True)
        self.labSerialPortStatusConected.setObjectName("labSerialPortStatusConected")

        self.labSerialPortStatusDisconnected = QtWidgets.QLabel(self)
        self.labSerialPortStatusDisconnected.setGeometry(QtCore.QRect(0, 4, 32, 32))
        self.labSerialPortStatusDisconnected.setText("")
        self.labSerialPortStatusDisconnected.setPixmap(QtGui.QPixmap("power_off.svg"))
        self.labSerialPortStatusDisconnected.setScaledContents(True)
        self.labSerialPortStatusDisconnected.setObjectName("labSerialPortStatusDisconnected")

        self.cmbSerialPorts = QtWidgets.QComboBox(self)
        self.cmbSerialPorts.setGeometry(QtCore.QRect(42, 0, 121, 41))
        self.cmbSerialPorts.setCurrentText("")
        self.cmbSerialPorts.setObjectName("cmbSerialPorts")


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
            self.labSerialPortStatusConected.setVisible(True)
            self.labSerialPortStatusDisconnected.setVisible(False)

        except Exception as e:
            self.labSerialPortStatusConected.setVisible(False)
            self.labSerialPortStatusDisconnected.setVisible(True)
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
        self.cmbSerialPorts.setStyleSheet("")
        #Get the selected serial port name
        serialPortToUse=self.cmbSerialPorts.itemText(index)

        # Try to connect to serial port and
        # update the user interface
        self.connectToSerialPort(serialPortToUse)




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


    window = SerialTerminalWidget()   # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed

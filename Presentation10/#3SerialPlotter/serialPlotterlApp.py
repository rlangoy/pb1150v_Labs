
from PyQt6.QtWidgets import QStyleFactory,QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit,QWidget
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent,QCloseEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog,QHBoxLayout
from PyQt6.QtCore import QRect
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot  as plt

from serialPlotterWindow import Ui_serialPlotter
from qtSerialComp import SerialConnector

# Import the custom QWidget MatplotlibWidget
import MatPlotLibWidget


class SerialPlotterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_serialPlotter()
        self.ui.setupUi(self)

        #Get list of available serial ports
        listOfSerialPorts=SerialConnector.getSerialPortsAsList()
        self.ui.labSerialPortStatusConected.setVisible(False)

        self.ui.cmbSerialPorts.setPlaceholderText("Select a port")
        self.ui.cmbSerialPorts.setStyleSheet("QComboBox {color: red}")
        self.ui.cmbSerialPorts.setCurrentIndex(-1)
        self.ui.cmbSerialPorts.addItems(listOfSerialPorts)
        self.ui.cmbSerialPorts.currentIndexChanged.connect(self.onCmbIndexChanged)


        self.show()

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

        Args:
            message (dict): The incoming serial data represented as a dictionary.
        """

        self.ui.pltGraph.addDataAndPlot(message['Pot1Value'])

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
# pyuic6 -x serialPlotterWindow.ui -o serialPlotterWindow.py

# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])


    window = SerialPlotterWindow()   # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed

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
        while self.running :
            if(self.serialPort.inWaiting()>0):
                serialInputStringAsLine = self.serialPort.readline()
                #send data as string to subscribers
                self.serialDataRxAsLineStr.emit(str(serialInputStringAsLine))
                serialInputAsDictionary = json.loads(serialInputStringAsLine)
                #send data ad python dictionary to subscribers
                self.serialDataRxAsDict.emit(serialInputAsDictionary)

    def sendDictMessageAsJson(self,dictMessage):
        message=json.dumps(dictMessage)
        self.serialPort.write(message.encode('utf-8'))
        #self.serialPort.write(b'{\"userLedOn\": 1}\r\n')

    def sendTextMessage(self,strMessage):
        self.serialPort.write(strMessage.encode('utf-8'))

    #Close the component by stoping the thread and close the serial port
    def close(self):
        #Stop the thread from  running
        self.running = False
        if(self.serialPort ):
          self.serialPort.close()

if __name__ == "__main__":
    class TestRecieverClass(QObject):
        def __init__(self):
            super().__init__()

        # Slot to handle the signal from a sender
        @pyqtSlot(dict)
        def handleJsonSignal(self, message):
            print(f"RecieverClass: Received  message: {message}")

    app = QCoreApplication(sys.argv)

    serialConnector=SerialConnector("COM7")    #Connect to serial port

    # Create and connect Class that listens for JSON information
    recvClass = TestRecieverClass()
    serialConnector.serialDataRxAsDict.connect(recvClass.handleJsonSignal)

    #Send message to turn led on
    serialConnector.sendDictMessageAsJson({"userLedOn": 1})

    sys.exit(app.exec())

    print("Bye")
    serialConnector.close()
    #minBryter.running= False
    #del minBryter



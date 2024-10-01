from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog , QLabel , QPushButton,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap

from PyQt6.QtWidgets import QApplication,QMainWindow


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Velkommen")
        self.setWindowIcon(QIcon("BlueSphere .webp"))

        #Plaser inn Widgets



        self.show()


# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = mainWindow()   # Create QtMainWindow



  #  window.setCentralWidget(label)

    # Start the event loop.
    app.exec()               # Wait for program to be closed



'''
Code to be used later


    window.setWindowTitle("Velkommen")
    window.setWindowIcon(QIcon("BlueSphere .webp"))
    window.setGeometry(200, 100, 400, 300)


class mainWindow(QMainWindow):

        icon = QIcon("BlueSphere .webp")
        self.setWindowIcon(icon)


        self.name_label = QLabel("Don't push the button.", self)
        self.name_label.move(20, 40)

        self.button = QPushButton("Push Me", self)
        self.button.move(20, 70)
      
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("BlueSphere .webp").scaled(32,32))
        self.label.move(10, 10)



        QMessageBox.warning(self, "Error","Hei \nDu skulle ikke trykke  på knappen!!!", QMessageBox.StandardButton.Ok)



     #Add Widdgets to MainForm
     self.qTextEditField = QPlainTextEdit()       
     self.setCentralWidget(self.qTextEditField)

     actionFileOpen = QAction("&Open File", self)
     self.menuBar().addAction(actionFileOpen)
     actionFileOpen.triggered.connect(self.openFile) # type: ignore

    #Repitisjon #04 ListerStringerOgFilbehandling slide 48 
        def openFile(self):
                # Read the context of filePath to the variable called data
                filenameAndPath=f"C:\\Documents\\test.txt" # File to Open
                fileHandle = open(filenameAndPath, 'r’)    # Open file for reading 
                strData = fileHandle.read()                # Read into a the variable strData
                fileHandle.close()                         # Close file 
        
        def saveFile(self): 
                # text to be written is contained in the variable textToWrite
                filenameAndPath=f"C:\\Documents\\test.txt" # File to Write
                strTextToWrite="Dette skal lagres på disk"    # Text to save in file
                fileHandle = open(filenameAndPath, 'w’)       # Open file for writing
                fileHandle.write(strTextToWrite)              # Write out text from string textToWrite
                fileHandle.close()                            # Close file


'''
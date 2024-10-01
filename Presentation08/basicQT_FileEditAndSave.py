from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog , QLabel , QPushButton,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QCloseEvent
from PyQt6.QtWidgets import QApplication,QMainWindow



class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        print("Hi")
        self.setWindowTitle("Velkommen")
        self.setWindowIcon(QIcon("BlueSphere .webp"))
        self.show()


    def closeEvent(self, event :QCloseEvent ):
        # This function runs when the window is about to close
        reply = QMessageBox.question(self, 'Close Confirmation',
                                     "Are you sure you want to close the window?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            print("Window is closing.")
            event.accept()  # Accept the close event
        else:
            event.ignore()  # Ignore the close event, keep the window open


# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = mainWindow()   # Create QtMainWindow



    # Start the event loop.
    app.exec()               # Wait for program to be closed



'''
Code to be used later


    window.setWindowTitle("Velkommen")
    window.setWindowIcon(QIcon("BlueSphere .webp"))
    window.setGeometry(200, 100, 400, 300)


class mainWindow(QMainWindow):

     #Add Widdgets to MainForm
     self.qTextEditField = QPlainTextEdit()       
     self.setCentralWidget(self.qTextEditField)

     actionFileOpen = QAction("&Open File", self)
     self.menuBar().addAction(actionFileOpen)
     actionFileOpen.triggered.connect(self.openFile) # type: ignore
    
      
    def openFile(self):
    
        dlg = QFileDialog(self)    
        dlg.setNameFilter("Text files (*.txt *.py)")
        dlg.setWindowTitle("Open File")  # Show save
        
        if( dlg.exec() ):   #exec and wait for dlg to close
            fileNames = dlg.selectedFiles()
            print(fileNames)
            print("Nå skal vi åpne filen")
        else:
            print("Åpne filen avbrutt")



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
from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog , QLabel , QPushButton,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QCloseEvent
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore  import QSettings,QRect



class mainWindow(QMainWindow):

    fileName=None   # :str path+FileName to save/write

    def __init__(self):
        super().__init__()
        # App Settings archive
        self.settings = QSettings('USN', 'MyApp')

        #Init the Window
        self.setupWindow()


    def _isWindowInsideScreen(self, geometry):
        # Get the geometry of the primary screen
        primaryScreen = QApplication.primaryScreen().availableGeometry()
        # Check if the window's geometry is within the screen's geometry
        return primaryScreen.contains(geometry.topLeft()) and primaryScreen.contains(geometry.bottomRight())


    def setupWindow(self):
        self.setWindowTitle("myNoteBook")
        self.setWindowIcon(QIcon("BlueSphere .webp"))
        #default windows size
        defaultWindowSize=QRect(0,0,400,300)
        #If windows geomentry is not stored in settings use values from defaultWindowSize
        geoRect=self.settings.value('Geometry',defaultWindowSize)
        print(geoRect)
        if(self._isWindowInsideScreen(geoRect) == False):
            geoRect=defaultWindowSize

        #Set the actual window Size
        self.setGeometry(geoRect)

        # Add Widdgets to MainForm
        self.qTextEditField = QPlainTextEdit()
        self.setCentralWidget(self.qTextEditField)

        actionFileOpen = QAction("&Open File", self)
        self.menuBar().addAction(actionFileOpen)
        actionFileOpen.triggered.connect(self.openFile)  # type: ignore

        actionFileSave = QAction("&Save File", self)
        self.menuBar().addAction(actionFileSave)
        actionFileSave.triggered.connect(self.saveFile)  # type: ignore


        self.show()

    def openFile(self):
        dlg = QFileDialog(self)
        dlg.setNameFilter("Text files (*.txt *.py)")
        dlg.setWindowTitle("Open File")  # Show save

        if (dlg.exec()):  # exec and wait for dlg to close
            self.fileName = dlg.selectedFiles()[0]
            # Read the context of filePath to the variable called data
            fileHandle = open(self.fileName, 'r')    # Open file for reading
            strData = fileHandle.read()  # Read into a the variable strData
            fileHandle.close()  # Close file

            self.qTextEditField.setPlainText(strData)
        else:
            print("Åpne filen avbrutt")


    def saveFile(self):

        if (self.fileName == None) :
            dlg = QFileDialog(self)
            dlg.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            dlg.setNameFilter("Text files (*.txt *.py)")
            dlg.setWindowTitle("Save File")  # Show save

            if (dlg.exec()):  # exec and wait for dlg to close
                self.fileName = dlg.selectedFiles()[0]
            else:
                return #Ret if save was canceled

        # text to be written is contained in the variable textToWrite
        strTextToWrite = self.qTextEditField.toPlainText()  # Text to save in file
        fileHandle = open(self.fileName, 'w')  # Open file for writing
        fileHandle.write(strTextToWrite)  # Write out text from string textToWrite
        fileHandle.close()  # Close file

    def closeEvent(self, event :QCloseEvent ):
        print("Program About to close")

        #Store settings before exiting the application
        self.settings.setValue('Geometry', self.geometry())

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
    defaultWindowSize=QRect(0,0,400,300)
    window.setGeometry(defaultWindowSize)


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
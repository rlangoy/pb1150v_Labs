from PyQt6.QtWidgets import QStyleFactory, QPlainTextEdit, QFileDialog, QLabel, QPushButton, QCheckBox, QDial, \
    QMessageBox, QLineEdit
from PyQt6.QtGui import QIcon, QAction, QPixmap, QDropEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.QtCore import QRect

# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = QMainWindow()  # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()  # Wait for program to be closed

'''
Code to be used later


    window.setWindowTitle("Velkommen")
    window.setWindowIcon(QIcon("BlueSphere.ico"))
    defaultWindowSize=QRect(0,0,400,300)
    window.setGeometry(defaultWindowSize)

     # App Settings archive
    self.settings = QSettings('USN', 'MyApp')


Widgets events:

  
    closeEvent      (event : QCloseEvent )'
    dropEvent                (event :  QDropEvent )
    
    def closeEvent(self, event :QCloseEvent ):

        #Store settings before exiting the application
        self.settings.setValue('Geometry', self.geometry())

    #If windows geomentry is not stored in settings use values from defaultWindowSize 
    geoRect=self.settings.value('Geometry',defaultWindowSize)



    window.setWindowTitle("Velkommen")
    window.setWindowIcon(QIcon("BlueSphere.ico"))
    defaultWindowSize=QRect(0,0,400,300)
    window.setGeometry(defaultWindowSize)

    # App Settings archive
    self.settings = QSettings('USN', 'MyApp')


class myFilePlainTextEdit(QPlainTextEdit) :
    def __init__(self):
        super().__init__()
        #run dropEvent if files is dropped
        self.setAcceptDrops(True)    

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            listOfURLs=event.mimeData().urls()
            #Get the first file name 
            firstDroppedFileName=listOfURLs[0].toLocalFile() 
            print(firstDroppedFileName)


class mainWindow(QMainWindow):

     #Add Widdgets to MainForm
     self.qTextEditField = QPlainTextEdit()       
     self.setCentralWidget(self.qTextEditField)

     strData='Velkommen'
     self.qTextEditField.setPlainText(strData)           # Set text in   QPlainTextEdit
     strInTextField = self.qTextEditField.toPlainText()  # Get Text from QPlainTextEdit


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







    #Repitisjon #04 ListerStringerOgFilbehandling slide 48 
        def openFile(self):
                # Read the context of filePath to the variable called data
                filenameAndPath=f"C:\\Documents\\test.txt" # File to Open
                fileHandle = open(filenameAndPath, 'r')    # Open file for reading
                strData = fileHandle.read()                # Read into a the variable strData
                fileHandle.close()                         # Close file

        def saveFile(self): 
                # text to be written is contained in the variable textToWrite
                filenameAndPath=f"C:\\Documents\\test.txt" # File to Write
                strTextToWrite="Dette skal lagres på disk"    # Text to save in file
                fileHandle = open(filenameAndPath, 'w')       # Open file for writing
                fileHandle.write(strTextToWrite)              # Write out text from string textToWrite
                fileHandle.close()                            # Close file


    def closeEvent(self, event :QCloseEvent ):

        #Store settings before exiting the application
        self.settings.setValue('Geometry', self.geometry())
'''
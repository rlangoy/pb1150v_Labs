from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap
from PyQt6.QtWidgets import QApplication,QMainWindow


# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = QMainWindow()   # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed



'''
Code to be used later

Widgets events:

    actionEvent     (event : QActionEvent )
    changeEvent   (event : QEvent )
    closeEvent      (event : QCloseEvent )
    contextMenuEvent  (event : QContextMenuEvent )
    dragEnterEvent       (event : QDragEnterEvent )
    dragLeaveEvent      (event : QDragLeaveEvent )
    dragMoveEvent       (event : QDragMoveEvent )
    dropEvent                (event :  QDropEvent )
    enterEvent               (event : QEnterEvent )
    focusInEvent            (event :QFocusEvent )
    focusOutEvent         (event : QFocusEvent )
    hideEvent                 (event : QHideEvent )
    inputMethodEvent    (event : QInputMethodEvent )
    keyPressEvent         (event : QKeyEvent )
    keyReleaseEvent     (event : QKeyEvent )
    leaveEvent               (event : QEvent )
    mouseDoubleClickEvent (event : QMouseEvent )
    mouseMoveEvent           (event : QMouseEvent )
    mousePressEvent           (event : QMouseEvent )
    mouseReleaseEvent       (event : QMouseEvent )
    moveEvent         (event : QMoveEvent )
    paintEvent          (event : QPaintEvent )
    resizeEvent        (event : QResizeEvent )
    showEvent         (event : QShowEvent )
    tabletEvent         (event : QTabletEvent )
    wheelEvent        (event : QWheelEvent )


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



    def closeEvent(self, event :QCloseEvent ):
        
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

'''
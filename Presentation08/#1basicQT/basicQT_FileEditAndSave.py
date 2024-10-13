from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog , QLabel , QPushButton,QMessageBox,QStyle
from PyQt6.QtGui import QIcon, QAction,QPixmap,QCloseEvent,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import QSettings,QRect

class FileQPlainTextEdit(QPlainTextEdit) :
    """
    A custom QPlainTextEdit widget that handles file drag-and-drop operations and file reading/writing.
    This class also tracks whether the text has been modified by the user, allowing the application
    to monitor changes in the editor's content.

    This class extends the QPlainTextEdit widget from PyQt6 and provides additional functionality
    for handling file-related actions, such as accepting dropped files and loading/saving text
    from/to files.
    """

    textChanged = False  # chk if edit field has been changed
    def __init__(self):
        super().__init__()
        # run dropEvent if files is dropped
        self.setAcceptDrops(True)
        super().textChanged.connect(self.textEntering)

    def textEntering(self):
        """
        Marks the text as changed when any modification is made.

        This method is triggered by the `super().textChanged` signal.
        When text is entered or modified in the widget, it sets `self.textChanged` to True, indicating
        that there are unsaved changes.
        """
        self.textChanged = True

    def dropEvent(self, event: QDropEvent):
        """
            Handles file drop events on the widget by processing the first file from the list of dropped URLs
            and passing it to the `setTextFromFile` method.

            The `dropEvent` method is an abstract override from the PyQt6 framework, which handles drop events.
            This functionality is enabled by calling `self.setAcceptDrops(True)` in the widget initialization.

            Args:
                event (QDropEvent): Contains information about the data being dropped onto the widget.
        """
        if event.mimeData().hasUrls():
            listOfURLs=event.mimeData().urls()
            # Get the first file name in uls list
            firstDroppedFileName=listOfURLs[0].toLocalFile()

            self.setTextFromFile(firstDroppedFileName)

    # Get the file path of the dropped file(s)

    def setTextFromFile(self,filenameAndPath: str):
        """
        Sets the content of a file as the text in the widget.

        This method opens a file specified by `filenameAndPath`, reads its content,
        and sets it as the text displayed in the `QPlainTextEdit` widget. After reading
        the file, it ensures that the file handle is properly closed.

        Args:
            filenameAndPath (str): The full path and filename of the file to be opened and displayed.

        Note:
            Repitisjon #04 ListerStringerOgFilbehandling slide 48

        """

        fileHandle = open(filenameAndPath, 'r')    # Open file for reading
        strData = fileHandle.read()                # Read into a the variable strData
        fileHandle.close()                         # Close file

        self.setPlainText(strData)  # Show text in QPlainTextEdit
        self.textChanged = False

    def writeTextToFile(self,filenameAndPath: str):
        """
        Writes the current content of the widget to a specified file.

        This method retrieves the current text from the `QPlainTextEdit` widget and writes
        it to a file specified by `filenameAndPath`. After the text is written, the file is
        properly closed.

        Args:
            filenameAndPath (str): The full path and filename of the file where the content
            will be written.

        Notes:
            Repitisjon #04 ListerStringerOgFilbehandling slide 48
         """
        strTextToWrite = self.toPlainText()      # Text to save in file
        fileHandle = open(filenameAndPath, 'w')  # Open file for writing
        fileHandle.write(strTextToWrite)         # Write out text from string textToWrite
        fileHandle.close()                       # Close file
        self.textChanged = False


class mainWindow(QMainWindow):

    fileName=None            # :str path+FileName to save/write
    settings : QSettings     # Configuration storage

    def __init__(self):
        super().__init__()
        # App Settings archive
        self.settings = QSettings('USN', 'MyApp')

        #Init the Window
        self.setupWindow()

    def _isWindowInsideScreen(self, geometry):
        """
        Checks if the window's geometry is fully contained within the primary screen's available area.

        This method verifies whether the top-left and bottom-right corners of the given window geometry
        are within the bounds of the primary screen's available geometry.

        Args:
            geometry (QRect): The geometry of the window to check.

        Returns:
            bool: True if the window is entirely within the primary screen's boundaries, False otherwise.
        """
        # Get the geometry of the primary screen
        primaryScreen = QApplication.primaryScreen().availableGeometry()
        # Check if the window's geometry is within the screen's geometry
        return primaryScreen.contains(geometry.topLeft()) and primaryScreen.contains(geometry.bottomRight())


    def setupWindow(self):
        """
        Initializes and configures the main application window.
        """

        self.setWindowTitle("myEditor")
        self.setWindowIcon(QIcon("BlueSphere.ico"))

        #default windows size
        defaultWindowSize=QRect(0,0,400,300)
        #If windows geomentry is not stored in settings use values from defaultWindowSize
        geoRect=self.settings.value('Geometry',defaultWindowSize)

        if(self._isWindowInsideScreen(geoRect) == False):
            geoRect=defaultWindowSize
        #Set the actual window Size
        self.setGeometry(geoRect)

        # Add Widdgets to MainForm
        self.qTextEditField = FileQPlainTextEdit()
        self.setCentralWidget(self.qTextEditField)

        fileMenu = self.menuBar().addMenu("File")
        actionFileOpen = QAction(QIcon("folder_open.svg"), "&Open File",self)
        #actionFileOpen = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon), "&Open File", self)  #    QT-standard Icons
        fileMenu.addAction(actionFileOpen)
        actionFileOpen.triggered.connect(self.openFile)  # type: ignore

        actionFileSave = QAction(QIcon("save.svg"), "&Save File", self)
        #actionFileSave = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton), "&Save File", self)  # QT-standard Icons
        fileMenu.addAction(actionFileSave)
        actionFileSave.triggered.connect(self.saveFile)  # type: ignore

        self.show()

    def openFile(self):
        """
           Opens a file dialog to allow the user to select a file for opening and displaying it in the
           self.qTextEditField (FileQPlainTextEdit : QPlainTextEdit : Widget)
        """

        dlg = QFileDialog(self)
        dlg.setNameFilter("Text files (*.txt *.py)")
        dlg.setWindowTitle("Open File")  # Show save

        if (dlg.exec()):  # exec and wait for dlg to close
            self.fileName = dlg.selectedFiles()[0]

            #Update the window Title showing the file name
            self.setWindowTitle("myNoteBook FileName : " + self.fileName.rsplit('/', 1)[-1])
        else:
            print("Åpne filen avbrutt")
            return

        print(self.qTextEditField)
        self.qTextEditField.setTextFromFile(self.fileName)   # Read text into text field



    def saveFile(self):
        """
            Opens a file dialog to allow the user to select a file for saving the context from
            self.qTextEditField (FileQPlainTextEdit : QPlainTextEdit : Widget)
         """

        if (self.fileName == None) :
            dlg = QFileDialog(self)
            dlg.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            dlg.setNameFilter("Text files (*.txt *.py)")
            dlg.setWindowTitle("Save File")  # Show save

            if (dlg.exec()):  # exec and wait for dlg to close
                self.fileName = dlg.selectedFiles()[0]
                # Update the window Title showing the file name
                self.setWindowTitle("myNoteBook FileName : " + self.fileName.rsplit('/', 1)[-1])

            else:
                return  # Ret if save was canceled

        # text to be written is contained in the variable textToWrite
        self.qTextEditField.writeTextToFile(self.fileName)


    def closeEvent(self, event :QCloseEvent ):
        """
         Handles the window close event and prompts the user to save unsaved changes.

         This method is an abstract override that runs when the window is about to close.
         It checks if there are unsaved changes in the text editor (`qTextEditField.textChanged`).
         If changes are detected, it prompts the user with a confirmation dialog asking
         whether they wish to close the window without saving.

         The window's geometry is also saved in the application settings before closing.

         Args:
             event (QCloseEvent): The close event triggered when the user attempts to close the window.

         Behavior:
             - If there are unsaved changes and the user selects 'No' in the confirmation dialog,
               the close event is ignored and the window remains open.
             - If the user selects 'Yes', the event is accepted, and the window closes.
         """
        #Store settings before exiting the application
        self.settings.setValue('Geometry', self.geometry())

        #Ask if unsaved changes is detected
        if(self.qTextEditField.textChanged) :
            # This function runs when the window is about to close
            reply = QMessageBox.question(self, 'Unsaved text',
                                         f"Are you sure you want to close the window<br>without saving first?",
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

    app.setWindowIcon(QIcon("BlueSphere.ico"))

    window = mainWindow()   # Create QtMainWindow

    # Start the event loop.
    app.exec()               # Wait for program to be closed
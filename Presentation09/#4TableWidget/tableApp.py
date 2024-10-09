from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QTableWidgetItem,QTableView ,QPushButton,QCheckBox,QDial,QMessageBox,QLineEdit,QTableWidget
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt6.QtCore import QRect
from PyQt6 import uic,QtGui
import json

class showPersonalInfo(QDialog):
    btlVisibility: QPushButton  # Hide/Show password

    def __init__(self):
        super().__init__()

        # Load .ui dialog
        uic.loadUi("personalInfo.ui", self)



        # find and map .ui elemnts that is needed
        self.tblwInfo = self.findChild(QTableView, "tblwInfo")  # Find the button by its object name

        print(self.tblwInfo)

        """Load JSON data from a file."""
        with open("Names.json", 'r') as file:
            self.data = json.load(file)

        # Set the number of columns
        self.tblwInfo.setColumnCount(3)
        # Set the number of rows
        self.tblwInfo.setRowCount(len(self.data))

        # Set the column headers
        self.tblwInfo.setHorizontalHeaderLabels(["Fornavn", "Etternavn", "E-Mail"])

        # Populate the table with data
        for row_index, row_data in enumerate(self.data):
            self.tblwInfo.setItem(row_index, 0, QTableWidgetItem(row_data["Fornavn"]))
            self.tblwInfo.setItem(row_index, 1, QTableWidgetItem(row_data["Etternavn"]))
            self.tblwInfo.setItem(row_index, 2, QTableWidgetItem(row_data["E-Mail"]))

        self.show()

    def onLoginClicked(self):
        print("Login Button Clicked")

    def onVisibilityPressed(self):
        print("Visibility Button onVisibilityPressed")

    def onVisibilityReleased(self):
        print("Visibility Button onVisibilityReleased")


# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = showPersonalInfo()   # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed


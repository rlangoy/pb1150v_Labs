from PyQt6.QtWidgets import QPlainTextEdit,QFileDialog,QLabel,QPushButton,QCheckBox,QDial,QMessageBox
from PyQt6.QtGui import QIcon, QAction,QPixmap,QDropEvent
from PyQt6.QtWidgets import QApplication,QMainWindow




# Run the program
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    window = QMainWindow()   # Create QtMainWindow
    window.show()

    # Start the event loop.
    app.exec()               # Wait for program to be closed



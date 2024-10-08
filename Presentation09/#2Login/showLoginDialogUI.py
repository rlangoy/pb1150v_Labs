from PyQt6 import uic,QtGui
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QDialog
from PyQt6.QtCore import QResource


#
class MainWindow(QDialog):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__()

        uic.loadUi('loginDialog.ui', self)


if __name__ == "__main__":
    #app = QtGui.QApplication(sys.argv)
    app = QApplication([])
    myapp = MainWindow()
    myapp.show()
    #sys.exit(app.exec_())
    app.exec()
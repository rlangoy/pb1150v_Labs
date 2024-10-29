from PyQt6.QtWidgets import QWidget,QHBoxLayout

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# Define the custom MatplotlibWidget class
class MatPlotLibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fig = Figure(figsize=(6, 4))
        self.plt = self.fig.add_subplot(111)

        #Add the matplotlib canvas to the widget
        self.canvas = FigureCanvas(self.fig)
        layout = QHBoxLayout (self)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

class RealTimeMatplotLibWidget(MatPlotLibWidget):

        #Data to display
        xdata, ydata = [], []
        #Curent plot index
        pltXIndex = 0

        #Maximum number of plots to display
        dataPointToPlot=50

        def __init__(self, parent=None):
            super().__init__(parent)
        def addDataAndPlot(self, y ):
            """
           Adds new Y-Value to be plotted.
           The number of datapoints to be ploted is
               limited by 'self.dataPointToPlot'
            """
            self.xdata.append(self.pltXIndex)
            self.ydata.append(y)
            self.pltXIndex += 1

            # Limit the list to the last 50 elements
            self.xdata = self.xdata[-self.dataPointToPlot:]
            self.ydata = self.ydata[-self.dataPointToPlot:]

            self.plt.clear()
            self.plt.plot(self.ydata)
            self.canvas.draw()  # Redraw the canvas

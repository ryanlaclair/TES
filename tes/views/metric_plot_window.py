"""
"""

from PyQt4 import QtGui, QtCore
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg
    as FigureCanvas)
from matplotlib.backends.backend_qt4agg import (NavigationToolbar2QT
    as NavigationToolbar)

class MetricPlotWindow(QtGui.QWidget):
    """
    """

    def __init__(self, model):
        """
        """

        super(MetricPlotWindow, self).__init__()

        self.model = model

        self.init_ui()
        self.setLayout(self.layout)
        self.setWindowTitle('Metric')
        self.show()

    def init_ui(self):
        """
        """

        # ok button
        self.ok_button = QtGui.QPushButton('Ok')
        self.ok_button.setFixedWidth(100)
        self.ok_button.clicked.connect(self.handle_ok_button)
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.addWidget(self.ok_button)

        # plot area
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self)

        axis = figure.add_subplot(111)

        temps = []
        metrics = []

        for emissivity in self.model.tes_method.emissivities:
            temps.append(emissivity.temperature)
            metrics.append(emissivity.assd)

        axis.plot(temps, metrics, color='k')
        axis.plot(self.model.emissivity.temperature, self.model.emissivity.assd,
                'ro', label='Estimated temperature')
        #axis.legend(loc=1, prop={'size':11})

        axis.axis([temps[0]-1, temps[-1]+1, min(metrics), max(metrics)])
        axis.set_xlabel('Temperature (K)')
        axis.set_ylabel('Metric')
        axis.set_yscale('log')

        canvas.draw()

        self.plot_layout = QtGui.QVBoxLayout()
        self.plot_layout.addWidget(toolbar)
        self.plot_layout.addWidget(canvas)

        # layout
        self.layout = QtGui.QVBoxLayout()
        self.layout.addLayout(self.plot_layout)
        self.layout.addLayout(self.button_layout)

    def handle_ok_button(self):
        """
        """

        plt.close('all')
        self.close()

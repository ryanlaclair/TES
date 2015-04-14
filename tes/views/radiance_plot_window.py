"""
"""

from PyQt4 import QtGui, QtCore
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg
    as FigureCanvas)
from matplotlib.backends.backend_qt4agg import (NavigationToolbar2QT
    as NavigationToolbar)

class RadiancePlotWindow(QtGui.QWidget):
    """
    """

    def __init__(self, model):
        """
        """

        super(RadiancePlotWindow, self).__init__()

        self.model = model

        self.init_ui()
        self.setLayout(self.layout)
        self.setWindowTitle('Calibrated Radiance')
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

        axis.plot(self.model.measurement.cbb.data.wavelength,
                self.model.measurement.cbb.data.average_spectrum,
                label='Cold blackbody', color='b')
        axis.plot(self.model.measurement.wbb.data.wavelength,
                self.model.measurement.wbb.data.average_spectrum,
                label='Warm blackbody', color='r')
        axis.plot(self.model.measurement.sam.data.wavelength,
                self.model.measurement.sam.data.average_spectrum,
                label='Sample', color='k')
        axis.plot(self.model.measurement.dwr.data.wavelength,
                self.model.measurement.dwr.data.average_spectrum,
                label='Downwelling', color='y')

        axis.axis([0, 20, 0, 30])
        axis.set_xlabel('Wavelength (microns)')
        axis.set_ylabel('Radiance (W/m^2/sr/micron)')
        axis.legend(loc=1, prop={'size':11})

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

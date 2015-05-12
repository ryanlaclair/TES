"""
"""

try:
    from PyQt5 import QtWidgets, QtCore
    import matplotlib
    matplotlib.use('Qt5Agg')
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg
       as FigureCanvas)
    from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT
       as NavigationToolbar)
except ImportError:
    from PyQt4 import QtGui as QtWidgets, QtCore
    import matplotlib
    matplotlib.use('Qt4Agg')
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg
       as FigureCanvas)
    from matplotlib.backends.backend_qt4agg import (NavigationToolbar2QT
       as NavigationToolbar)

class EmissivityPlotWindow(QtWidgets.QWidget):
    """
    """

    def __init__(self, model):
        """
        """

        super(EmissivityPlotWindow, self).__init__()

        self.model = model

        self.init_ui()
        self.setLayout(self.layout)
        self.setWindowTitle('Emissivity')
        self.show()

    def init_ui(self):
        """
        """

        # ok button
        self.ok_button = QtWidgets.QPushButton('Ok')
        self.ok_button.setFixedWidth(100)
        self.ok_button.clicked.connect(self.handle_ok_button)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addWidget(self.ok_button)

        # plot area
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self)

        axis = figure.add_subplot(111)

        axis.plot(self.model.emissivity.wavelength,
                self.model.emissivity.emissivity, color='k')

        axis.axis([8, 14, -0.2, 1.2])
        axis.set_xlabel('Wavelength (microns)')
        axis.set_ylabel('Emissivity')

        canvas.draw()

        self.plot_layout = QtWidgets.QVBoxLayout()
        self.plot_layout.addWidget(toolbar)
        self.plot_layout.addWidget(canvas)

        # layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.plot_layout)
        self.layout.addLayout(self.button_layout)

    def handle_ok_button(self):
        """
        """

        plt.close('all')
        self.close()

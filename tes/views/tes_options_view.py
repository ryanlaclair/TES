"""
File:       tes_options_view.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

# Try block to ensure compatibility with PyQt4 and PyQt5
try:
   from PyQt5 import QtWidgets, QtCore
except ImportError:
   from PyQt4 import QtGui as QtWidgets, QtCore

class TesOptionsView(QtWidgets.QGroupBox):
    """A class that represents the options frame layout.
    """

    def __init__(self):
        """Instance constructor.
        """

        super(TesOptionsView, self).__init__()

        self.init_ui()
        self.setLayout(self.layout)

    def init_ui(self):
        """Initiallize and add the UI elements to the frame.
        """

        # measurement
        self.measurement = QtWidgets.QLabel('Measurement:')
        self.measurement_edit = QtWidgets.QLineEdit()
        self.measurement_edit.setPlaceholderText('Required..')
        self.measurement_button = QtWidgets.QPushButton('Browse')
        self.measurement_button.setFixedWidth(100)

        # technique
        self.technique = QtWidgets.QLabel('Technique:')
        self.technique_combo_box = QtWidgets.QComboBox()
        self.technique_combo_box.addItem(
                'Fixed Window Temperature Emissivity Separation')
        self.technique_combo_box.addItem(
                'Moving Window Temperature Emissivity Separation')
        self.technique_combo_box.addItem(
                'Multiple Fixed Window Temperature Emissivity Separation')
        self.technique_combo_box.addItem(
                'Known Temperature')
        #self.technique_combo_box.addItem(
        #        'Multiple Moving Window Temperature Emissivity Separation')

        # plate emissivity
        self.plate = QtWidgets.QLabel('Plate emissivity:')
        self.plate_edit = QtWidgets.QLineEdit()
        self.plate_edit.setFixedWidth(75)
        self.plate_edit.setPlaceholderText('Optional..')

        # tolerance
        self.tolerance = QtWidgets.QLabel('Coadd variation tolerance:')
        self.tolerance_edit = QtWidgets.QLineEdit()
        self.tolerance_edit.setFixedWidth(75)
        self.percent = QtWidgets.QLabel('%')

        # temperature range
        self.temp_limits = QtWidgets.QLabel('Temperature limits:')
        self.min_temp_edit = QtWidgets.QLineEdit()
        self.min_temp_edit.setFixedWidth(75)
        self.k1 = QtWidgets.QLabel('K')
        self.max_temp_edit = QtWidgets.QLineEdit()
        self.max_temp_edit.setFixedWidth(75)
        self.k2 = QtWidgets.QLabel('K')

        # wavelength range
        self.wave_limits = QtWidgets.QLabel('Wavelength limits:')
        self.min_wave_edit = QtWidgets.QLineEdit()
        self.min_wave_edit.setFixedWidth(75)
        self.micron1 = QtWidgets.QLabel('microns')
        self.max_wave_edit = QtWidgets.QLineEdit()
        self.max_wave_edit.setFixedWidth(75)
        self.micron2 = QtWidgets.QLabel('microns')

        # window width
        self.win_widths = QtWidgets.QLabel('Window widths:')
        self.win_width_edit = QtWidgets.QLineEdit()
        self.win_width_edit.setFixedWidth(75)
        self.micron3 = QtWidgets.QLabel('microns')

        # plots
        self.plots = QtWidgets.QLabel('Plots:')
        self.radiance_plot_check = QtWidgets.QCheckBox('Calibrated radiance')
        self.emissivity_plot_check = QtWidgets.QCheckBox('Calculated emissivity')
        self.metric_plot_check = QtWidgets.QCheckBox('Metric')

        # plot layout
        self.plot_layout = QtWidgets.QGridLayout()
        self.plot_layout.addWidget(self.radiance_plot_check, 0, 0)
        self.plot_layout.addWidget(self.emissivity_plot_check, 0, 1)
        self.plot_layout.addWidget(self.metric_plot_check, 1, 0)
        self.plot_layout.setContentsMargins(0, 0, 0, 0)

        # layout
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.measurement, 0, 0, QtCore.Qt.AlignRight)
        self.layout.addWidget(self.measurement_edit, 0, 1)
        self.layout.addWidget(self.measurement_button, 0, 2)
        self.layout.addLayout(self._add_stretch(), 1, 0)
        self.layout.addWidget(self.technique, 2, 0, QtCore.Qt.AlignRight)
        self.layout.addWidget(self.technique_combo_box, 2, 1)
        self.layout.addWidget(self.plate, 3, 0, QtCore.Qt.AlignRight)
        self.layout.addWidget(self.plate_edit, 3, 1)
        self.layout.addWidget(self.tolerance, 4, 0, QtCore.Qt.AlignRight)
        self.layout.addLayout(
                self._add_units(self.tolerance_edit, self.percent), 4, 1)
        self.layout.addWidget(self.temp_limits, 5, 0, QtCore.Qt.AlignRight)
        self.layout.addLayout(
                self._add_units(self.min_temp_edit, self.k1, 
                    self.max_temp_edit, self.k2), 5, 1)
        self.layout.addWidget(self.wave_limits, 6, 0, QtCore.Qt.AlignRight)
        self.layout.addLayout(
                self._add_units(self.min_wave_edit, self.micron1,
                    self.max_wave_edit, self.micron2), 6, 1)
        self.layout.addWidget(self.win_widths, 7, 0, QtCore.Qt.AlignRight)
        self.layout.addLayout(
                self._add_units(self.win_width_edit, self.micron3), 7, 1)
        self.layout.addLayout(self._add_stretch(), 8, 0)
        self.layout.addWidget(self.plots, 9, 0, QtCore.Qt.AlignRight)
        self.layout.addLayout(self.plot_layout, 9, 1)

    def _add_units(self, edit1, label1, edit2=None, label2=None):
        """Helper function to create a sublayout.  For use in adding units to
        Qt Edit boxes.

        Arguments:
            edit1 - First edit box.
            label1 - First label.
            edit2 - Second edit box (optional).
            label2 - Second label (optional).

        Returns:
            A horizontal box layout containing the specified elements.
        """


        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(edit1)
        layout.addWidget(label1)

        if not edit2 is None:
            layout.addWidget(edit2)

        if not label2 is None:
            layout.addWidget(label2)

        layout.setContentsMargins(0, 0, 0, 0)

        return layout

    def _add_stretch(self):
        """Create a blank stretch layout.

        Returns:
            The blank layout.
        """

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(QtWidgets.QFrame())
        layout.addWidget(QtWidgets.QFrame())

        return layout

"""
"""

from PyQt4 import QtGui, QtCore

from tes_options_view import TesOptionsView
from ..models.gui_models.tes_options import TesOptions
from ..controllers.tes_options_control import TesOptionsControl
from ..controllers.tes_main_control import TesMainControl

class TesMainWindow(QtGui.QWidget):
    """
    """

    def __init__(self):
        """
        """

        super(TesMainWindow, self).__init__()

        self.options = TesOptions()
        self.options_view = TesOptionsView()
        self.options_control = TesOptionsControl(self.options, self.options_view)

        self.control = TesMainControl(self.options, self)

        self.init_ui()

        self.options_control.update_view()
        self.options_view.measurement_button.clicked.connect(
                self.options_control.handle_measurement_button)
        self.options_view.technique_combo_box.currentIndexChanged.connect(
                self.options_control.update_view)
        self.ok_button.clicked.connect(self.options_control.update_model)
        self.ok_button.clicked.connect(self.control.handle_ok_button)
        self.cancel_button.clicked.connect(self.control.handle_cancel_button)

        self.setLayout(self.layout)
        self.show()

    def init_ui(self):
        """
        """

        # temperature
        self.temperature = QtGui.QLabel('Sample temperature:')
        self.temperature_edit = QtGui.QLabel(' ')
        self.temperature_layout = QtGui.QHBoxLayout()
        self.temperature_layout.addWidget(self.temperature)
        self.temperature_layout.addWidget(self.temperature_edit)
        self.temperature_group = QtGui.QGroupBox()
        self.temperature_group.setLayout(self.temperature_layout)

        # ok button
        self.ok_button = QtGui.QPushButton('Ok')
        self.ok_button.setFixedWidth(100)

        # cancel button
        self.cancel_button = QtGui.QPushButton('Cancel')
        self.cancel_button.setFixedWidth(100)

        # button layout
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addStretch()

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.options_view)
        self.layout.addWidget(self.temperature_group)
        self.layout.addLayout(self.button_layout)


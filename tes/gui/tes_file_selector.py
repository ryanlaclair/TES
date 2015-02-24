"""
"""

class FileSelector(QtGui.QWidget):
    """
    """

    def __init__(self):
        """
        """

        super(FileSelector, self).__init__()

        self.cbb = QtGui.QLabel('Cold blackbody:')
        self.wbb = QtGui.QLabel('Warm blackbody:')
        self.sam = QtGui.QLabel('Sample:')
        self.dwr = QtGui.QLabel('Downwelling:')
        self.plate = QtGui.QLabel('Plate emissivity:')

        self.cbb_edit = QtGui.QLineEdit()
        self.cbb_edit.setPlaceholderText('Required..')
        self.wbb_edit = QtGui.QLineEdit()
        self.wbb_edit.setPlaceholderText('Required..')
        self.sam_edit = QtGui.QLineEdit()
        self.sam_edit.setPlaceholderText('Required..')
        self.dwr_edit = QtGui.QLineEdit()
        self.dwr_edit.setPlaceholderText('Optional..')
        self.plate_edit = QtGui.QLineEdit()
        self.plate_edit.setPlaceholderText('Optional..')

        self.cbb_button = QtGui.QPushButton('Browse')
        self.cbb_button.setFixedWidth(100)
        self.wbb_button = QtGui.QPushButton('Browse')
        self.wbb_button.setFixedWidth(100)
        self.sam_button = QtGui.QPushButton('Browse')
        self.sam_button.setFixedWidth(100)
        self.dwr_button = QtGui.QPushButton('Browse')
        self.dwr_button.setFixedWidth(100)

        self._init_ui()

    def _init_ui(self):
        """Creates the layout used for the file selection tab.
        """

        file_selector_layout = QtGui.QGridLayout()
        file_selector_layout.addWidget(self.cbb, 0, 0, QtCore.Qt.AlignRight)
        file_selector_layout.addWidget(self.cbb_edit, 0, 1)
        file_selector_layout.addWidget(self.cbb_button, 0, 2)
        file_selector_layout.addWidget(self.wbb, 1, 0, QtCore.Qt.AlignRight)
        file_selector_layout.addWidget(self.wbb_edit, 1, 1)
        file_selector_layout.addWidget(self.wbb_button, 1, 2)
        file_selector_layout.addWidget(self.sam, 2, 0, QtCore.Qt.AlignRight)
        file_selector_layout.addWidget(self.sam_edit, 2, 1)
        file_selector_layout.addWidget(self.sam_button, 2, 2)
        file_selector_layout.addWidget(self.dwr, 3, 0, QtCore.Qt.AlignRight)
        file_selector_layout.addWidget(self.dwr_edit, 3, 1)
        file_selector_layout.addWidget(self.dwr_button, 3, 2)
        file_selector_layout.addWidget(self.plate, 4, 0, QtCore.Qt.AlignRight)
        file_selector_layout.addWidget(self.plate_edit, 4, 1)

        self.cbb_button.clicked.connect(self._handle_cbb_button)
        self.wbb_button.clicked.connect(self._handle_wbb_button)
        self.sam_button.clicked.connect(self._handle_sam_button)
        self.dwr_button.clicked.connect(self._handle_dwr_button)

    def _handle_cbb_button(self):
        """Open a file selection dialog to choose a .cbb (cold blackbody) file
        when the corresponding CBB button is pressed, and update the CBB text
        area to reflect the chosen file.
        """

        self.cbb_edit.setText(QtGui.QFileDialog.getOpenFileName(self,
            'Choose a cold blackbody file..', '', 'CBB (*.cbb)'))

    def _handle_wbb_button(self):
        """Open a file selection dialog to choose a .wbb (warm blackbody) file
        when the corresponding WBB button is pressed, and update the WBB text
        area to reflect the chosen file.
        """

        self.wbb_edit.setText(QtGui.QFileDialog.getOpenFileName(self,
            'Choose a warm blackbody file..', '', 'WBB (*.wbb)'))

    def _handle_sam_button(self):
        """Open a file selection dialog to choose a .sam (sample) file when the
        corresponding SAM button is pressed, and update the SAM text area to
        reflect the chosen file.
        """

        self.sam_edit.setText(QtGui.QFileDialog.getOpenFileName(self,
            'Choose a sample file..', '', 'SAM (*.sam)'))

    def _handle_dwr_button(self):
        """Open a file selection dialog to choose a .dwr (downwelling) file
        when the corresponding DWR button is pressed, and update the DWR text
        area to reflect the chosen file.
        """

        self.dwr_edit.setText(QtGui.QFileDialog.getOpenFileName(self,
            'Choose a downwelling file..', '', 'DWR (*.dwr)'))

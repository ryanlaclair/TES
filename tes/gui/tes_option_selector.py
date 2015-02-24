"""
"""

class OptionSelector(QtGui.QWidget):
    """
    """

    def __init__(self):
        """
        """

        super(OptionSelector, self).__init__()

        self.technique = QtGui.QLabel('Technique:')
        self.measurementTolerance = QtGui.QLabel('Coadd variation tolerance:')
        self.tempLimits = QtGui.QLabel('Search interval temperature limits:')
        self.waveLimits = QtGui.QLabel('Waterband wavelength limits:')
        self.windowLimits = QtGui.QLabel('Window width:')
        self.windowStep = QtGui.QLabel('Window step:')
        self.numWindows = QtGui.QLabel('Number of windows:')
        self.plots = QtGui.QLabel('Plots:')
        self.percent = QtGui.QLabel('%')
        self.k1 = QtGui.QLabel('K')
        self.k2 = QtGui.QLabel('K')
        self.micron1 = QtGui.QLabel('microns')
        self.micron2 = QtGui.QLabel('microns')
        self.micron3 = QtGui.QLabel('microns')
        self.micron4 = QtGui.QLabel('microns')
        self.micron5 = QtGui.QLabel('microns')

        # measurement tolerance
        self.measurementToleranceEdit = QtGui.QLineEdit()
        self.measurementToleranceEdit.setFixedWidth(75)
        self.measurementToleranceEdit.setText(self.wbTolerance)

        # temperature range
        self.minTempEdit = QtGui.QLineEdit()
        self.minTempEdit.setFixedWidth(75)
        self.minTempEdit.setText(self.wbLowerTemp)
        self.maxTempEdit = QtGui.QLineEdit()
        self.maxTempEdit.setFixedWidth(75)
        self.maxTempEdit.setText(self.wbUpperTemp)

        # wavelength range
        self.minWaveEdit = QtGui.QLineEdit()
        self.minWaveEdit.setFixedWidth(75)
        self.minWaveEdit.setText(self.wbLowerWave)
        self.maxWaveEdit = QtGui.QLineEdit()
        self.maxWaveEdit.setFixedWidth(75)
        self.maxWaveEdit.setText(self.wbUpperWave)

        # window size range
        self.minWinEdit = QtGui.QLineEdit()
        self.minWinEdit.setFixedWidth(75)
        self.maxWinEdit = QtGui.QLineEdit()
        self.maxWinEdit.setFixedWidth(75)

        # number of window steps
        self.windowStepEdit = QtGui.QLineEdit()
        self.windowStepEdit.setFixedWidth(75)

        # number of windows
        self.numWindowsEdit = QtGui.QLineEdit()
        self.numWindowsEdit.setFixedWidth(75)

        self.techniqueComboBox = QtGui.QComboBox(self)
        self.techniqueComboBox.addItem(
            'Waterband Temperature Emissivity Separation')
        self.techniqueComboBox.addItem(
            'Standard Temperature Emissivity Separation')
        self.techniqueComboBox.addItem(
            'Moving Window Temperature Emissivity Separation')
        self.techniqueComboBox.addItem(
            'Variable Moving Window Temperature Emissivity Separation')
        self.techniqueComboBox.addItem(
            'Multiple Moving Window Temperature Emissivity Separation')
        self.techniqueComboBox.currentIndexChanged.connect(
            self._handleTechnique)

        self.radiancePlotCheckBox = QtGui.QCheckBox('Calibrated radiance')
        self.emissivityPlotCheckBox = QtGui.QCheckBox('Calculated emissivity')
        self.emissivitySearchCheckBox = QtGui.QCheckBox('Emissivity search')
        self.metricPlotCheckBox = QtGui.QCheckBox('Variation criterea')

        # tooltips
        self.measurementTolerance.setToolTip('Maximum allowed error between coadds.')
        self.measurementToleranceEdit.setToolTip(self.measurementTolerance.toolTip())
        self.tempLimits.setToolTip('Upper and lower temperature limits on which 
                to perform the emissivity search.')
        self.minTempEdit.setToolTip('Lower temperature limit')
        self.maxTempEdit.setToolTip('Upper temperature limit')
        self.waveLimits.setToolTip('Upper and lower waterband wavelength limits 
                to be used in the temperature determination.')
        self.minWaveEdit.setToolTip('Lower waterband limit')
        self.maxWaveEdit.setToolTip('Upper waterband limit')
        self.windowLimits.setToolTip('Width of the wavelength window to examine 
                across the spectrum.')
        self.minWinEdit.setToolTip(self.windowLimits.toolTip())
        self.maxWinEdit.setToolTip('Upper window limit')
        self.windowStep.setToolTip('The step to increase the window width within 
                the limits.')
        self.windowStepEdit.setToolTip(self.windowStep.toolTip())
        self.numWindows.setToolTip('The total number of windows to examine at one 
                time.')
        self.numWindowsEdit.setToolTip(self.numWindows.toolTip())
        self.radiancePlotCheckBox.setToolTip('Display a plot of the calibrated 
                radiance curves for the sample, downwelling, cold blackbody and 
                warm blackbody.')
        self.emissivityPlotCheckBox.setToolTip('Display a plot of the final 
                calculated emissivity.')
        self.emissivitySearchCheckBox.setToolTip('Display a dynamic plot of 
                the emissivity curve at each temperature examined.')
        self.metricPlotCheckBox.setToolTip('Display a plot of the variation 
                metric used to determine the best temperature approximation.')


    def _optionSelector(self):
        """Creates the layout for the option selection tab.
        """

        self._parseConfig()

        checkBoxLayout = QtGui.QGridLayout()
        checkBoxLayout.addWidget(self.radiancePlotCheckBox, 0, 0)
        checkBoxLayout.addWidget(self.emissivityPlotCheckBox, 0, 1)
        checkBoxLayout.addWidget(self.emissivitySearchCheckBox, 1, 0)
        checkBoxLayout.addWidget(self.metricPlotCheckBox, 1, 1)
        checkBoxLayout.setContentsMargins(0, 0, 0, 0)

        checkBoxWidget = QtGui.QFrame()
        checkBoxWidget.setLayout(checkBoxLayout)

        self.measurementToleranceUnits = self._addUnits(self.measurementToleranceEdit, self.percent)
        self.tempLimitsUnits = self._addUnits(self.minTempEdit, self.k1, self.maxTempEdit, self.k2)
        self.waveLimitsUnits = self._addUnits(self.minWaveEdit, self.micron1, self.maxWaveEdit, self.micron2)
        self.windowLimitsUnits = self._addUnits(self.minWinEdit, self.micron3, self.maxWinEdit, self.micron4)
        self.windowStepUnits = self._addUnits(self.windowStepEdit, self.micron5)

        windowLimitsWidget = self._makeWidget(self.windowLimitsUnits)
        windowStepWidget = self._makeWidget(self.windowStepUnits)
        numWindowsWidget = self._makeWidget(self.numWindowsEdit)

        optionSelectorLayout = QtGui.QGridLayout()
        optionSelectorLayout.addWidget(self.technique, 0, 0,
            QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(self.techniqueComboBox, 0, 1)
        optionSelectorLayout.addWidget(self.measurementTolerance, 1, 0, QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(self.measurementToleranceUnits, 1, 1)
        optionSelectorLayout.addWidget(self.tempLimits, 2, 0,
            QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(self.tempLimitsUnits, 2, 1)
        optionSelectorLayout.addWidget(self.waveLimits, 3, 0,
            QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(self.waveLimitsUnits, 3, 1)
        optionSelectorLayout.addWidget(self.windowLimits, 4, 0, QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(windowLimitsWidget, 4, 1)
        optionSelectorLayout.addWidget(self.windowStep, 5, 0, QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(windowStepWidget, 5, 1)
        optionSelectorLayout.addWidget(self.numWindows, 6, 0, QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(numWindowsWidget, 6, 1, QtCore.Qt.AlignLeft)
        optionSelectorLayout.addWidget(self.plots, 7, 0, QtCore.Qt.AlignRight)
        optionSelectorLayout.addWidget(checkBoxWidget, 7, 1)

        self._waterbandOptions()

        return optionSelectorLayout

    def _makeWidget(self, item):
        """
        """

        widget = QtGui.QFrame()
        layout = QtGui.QHBoxLayout()

        layout.addWidget(item)

        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        return widget

    def _addUnits(self, edit1, label1, edit2=None, label2=None):
        """Helper function to create a sublayout.  For use in adding units to
        Qt Edit boxes.

        arguments:
            edit1 - First edit box.
            label1 - First label.
            edit2 - Second edit box (optional).
            label2 - Second label (optional).

        returns:
            A horizontal box layout containing the specified elements.
        """

        unitWidget = QtGui.QFrame()

        unitLayout = QtGui.QHBoxLayout()

        unitLayout.addWidget(edit1)
        unitLayout.addWidget(label1)

        if not edit2 is None:
            unitLayout.addWidget(edit2)

        if not label2 is None:
            unitLayout.addWidget(label2)

        unitLayout.setContentsMargins(0, 0, 0, 0)

        unitWidget.setLayout(unitLayout)

        return unitWidget

    def _handleTechnique(self):
        """Make necessary changes to wavelength range, window size range, and
        number of windows when a different temperature emissivity separation
        technique is chosen.
        """

        technique = str(self.techniqueComboBox.currentText())

        if ('Waterband' in technique):
            self._waterbandOptions()
        elif ('Standard' in technique):
            self._standardOptions()
        elif ('Variable' in technique):
            self._variableOptions()
        elif ('Multiple' in technique):
            self._multipleOptions()
        else:
            self._movingOptions()

    def _waterbandOptions(self):
        """
        """

        self.waveLimits.setText('Waterband wavelength limits:')

        self.measurementToleranceEdit.setText(self.wbTolerance)
        self.minTempEdit.setText(self.wbLowerTemp)
        self.maxTempEdit.setText(self.wbUpperTemp)
        self.minWaveEdit.setText(self.wbLowerWave)
        self.maxWaveEdit.setText(self.wbUpperWave)
        self.minWinEdit.setText('')
        self.maxWinEdit.setText('')
        self.windowStepEdit.setText('')
        self.numWindowsEdit.setText('')
        self.metricPlotCheckBox.setText('Variation criterea')

        self.waveLimits.setToolTip('Upper and lower waterband wavelength limits to be used in the temperature determination.')

        self.windowLimits.setVisible(False)
        self.windowLimitsUnits.setVisible(False)
        self.windowStep.setVisible(False)
        self.windowStepUnits.setVisible(False)
        self.numWindows.setVisible(False)
        self.numWindowsEdit.setVisible(False)
        self.emissivitySearchCheckBox.setVisible(True)
        self.metricPlotCheckBox.setVisible(True)

        self.waveLimits.setToolTip('Upper and lower waterband wavelength limits to be used in the temperature determination.')
        self.minWaveEdit.setToolTip('Lower waterband limit')
        self.maxWaveEdit.setToolTip('Upper waterband limit')
        self.metricPlotCheckBox.setToolTip('Display a plot of the variation metric used to determine the best temperature approximation.')

    def _standardOptions(self):
        """
        """

        self.waveLimits.setText('Wavelength limits:')

        self.measurementToleranceEdit.setText(self.stdTolerance)
        self.minTempEdit.setText(self.stdLowerTemp)
        self.maxTempEdit.setText(self.stdUpperTemp)
        self.minWaveEdit.setText(self.stdLowerWave)
        self.maxWaveEdit.setText(self.stdUpperWave)
        self.minWinEdit.setText('')
        self.maxWinEdit.setText('')
        self.windowStepEdit.setText('')
        self.numWindowsEdit.setText('')
        self.metricPlotCheckBox.setText('Smoothness criterea')

        self.metricPlotCheckBox.setChecked(False)

        self.windowLimits.setVisible(False)
        self.windowLimitsUnits.setVisible(False)
        self.windowStep.setVisible(False)
        self.windowStepUnits.setVisible(False)
        self.numWindows.setVisible(False)
        self.numWindowsEdit.setVisible(False)
        self.emissivitySearchCheckBox.setVisible(True)
        self.metricPlotCheckBox.setVisible(True)

        self.waveLimits.setToolTip('Upper and lower wavelength limits to be used in the temperature determination.')
        self.minWaveEdit.setToolTip('Lower wavelength limit')
        self.maxWaveEdit.setToolTip('Upper wavelength limit')
        self.metricPlotCheckBox.setToolTip('Display a plot of the smoothness metric used to determine the best temperature approximation.')

    def _movingOptions(self):
        """
        """

        self.waveLimits.setText('Search range:')
        self.windowLimits.setText('Window width:')

        self.measurementToleranceEdit.setText(self.mwTolerance)
        self.minTempEdit.setText(self.mwLowerTemp)
        self.maxTempEdit.setText(self.mwUpperTemp)
        self.minWaveEdit.setText(self.mwLowerWave)
        self.maxWaveEdit.setText(self.mwUpperWave)
        self.minWinEdit.setText(self.mwWinWidth)
        self.maxWinEdit.setText('')
        self.windowStepEdit.setText('')
        self.numWindowsEdit.setText('')

        self.emissivitySearchCheckBox.setChecked(False)
        self.metricPlotCheckBox.setChecked(False)

        self.maxWinEdit.setVisible(False)
        self.micron4.setVisible(False)
        self.windowLimits.setVisible(True)
        self.windowLimitsUnits.setVisible(True)
        self.windowStep.setVisible(False)
        self.windowStepUnits.setVisible(False)
        self.numWindows.setVisible(False)
        self.numWindowsEdit.setVisible(False)
        self.emissivitySearchCheckBox.setVisible(False)
        self.metricPlotCheckBox.setVisible(False)

        self.waveLimits.setToolTip('Upper and lower wavelength limits to be used in the temperature determination.')
        self.minWaveEdit.setToolTip('Lower wavelength limit')
        self.maxWaveEdit.setToolTip('Upper wavelength limit')
        self.windowLimits.setToolTip('Width of the wavelength window to examine across the spectrum.')
        self.minWinEdit.setToolTip(self.windowLimits.toolTip())

    def _variableOptions(self):
        """
        """

        self.waveLimits.setText('Search range:')
        self.windowLimits.setText('Window width limits:')
        self.windowStep.setText('Window step:')

        self.measurementToleranceEdit.setText(self.vmwTolerance)
        self.minTempEdit.setText(self.vmwLowerTemp)
        self.maxTempEdit.setText(self.vmwUpperTemp)
        self.minWaveEdit.setText(self.vmwLowerWave)
        self.maxWaveEdit.setText(self.vmwUpperWave)
        self.minWinEdit.setText(self.vmwLowerWinWidth)
        self.maxWinEdit.setText(self.vmwUpperWinWidth)
        self.windowStepEdit.setText(self.vmwWinStep)
        self.numWindowsEdit.setText('')

        self.emissivitySearchCheckBox.setChecked(False)
        self.metricPlotCheckBox.setChecked(False)

        self.maxWinEdit.setVisible(True)
        self.micron4.setVisible(True)
        self.windowLimits.setVisible(True)
        self.windowLimitsUnits.setVisible(True)
        self.windowStep.setVisible(True)
        self.windowStepUnits.setVisible(True)
        self.numWindows.setVisible(False)
        self.numWindowsEdit.setVisible(False)
        self.emissivitySearchCheckBox.setVisible(False)
        self.metricPlotCheckBox.setVisible(False)

        self.waveLimits.setToolTip('Upper and lower wavelength limits to be used in the temperature determination.')
        self.minWaveEdit.setToolTip('Lower wavelength limit')
        self.maxWaveEdit.setToolTip('Upper wavelength limit')
        self.windowLimits.setToolTip('Upper and lower limits of the wavelength window to examine across the spectrum.')
        self.minWinEdit.setToolTip('Lower window limit')
        self.maxWinEdit.setToolTip('Upper window limit')

    def _multipleOptions(self):
        """
        """

        self.waveLimits.setText('Search range:')
        self.windowLimits.setText('Window width limits:')
        self.windowStep.setText('Window step:')

        self.measurementToleranceEdit.setText(self.mmwTolerance)
        self.minTempEdit.setText(self.mmwLowerTemp)
        self.maxTempEdit.setText(self.mmwUpperTemp)
        self.minWaveEdit.setText(self.mmwLowerWave)
        self.maxWaveEdit.setText(self.mmwUpperWave)
        self.minWinEdit.setText(self.mmwLowerWinWidth)
        self.maxWinEdit.setText(self.mmwUpperWinWidth)
        self.windowStepEdit.setText(self.mmwWinStep)
        self.numWindowsEdit.setText(self.mmwNumWins)

        self.emissivitySearchCheckBox.setChecked(False)
        self.metricPlotCheckBox.setChecked(False)

        self.maxWinEdit.setVisible(True)
        self.micron4.setVisible(True)
        self.windowLimits.setVisible(True)
        self.windowLimitsUnits.setVisible(True)
        self.windowStep.setVisible(True)
        self.windowStepUnits.setVisible(True)
        self.numWindows.setVisible(True)
        self.numWindowsEdit.setVisible(True)
        self.emissivitySearchCheckBox.setVisible(False)
        self.metricPlotCheckBox.setVisible(False)

        self.waveLimits.setToolTip('Upper and lower wavelength limits to be used in the temperature determination.')
        self.minWaveEdit.setToolTip('Lower wavelength limit')
        self.maxWaveEdit.setToolTip('Upper wavelength limit')
        self.windowLimits.setToolTip('Upper and lower limits of the wavelength window to examine across the spectrum.')
        self.minWinEdit.setToolTip('Lower window limit')
        self.maxWinEdit.setToolTip('Upper window limit')

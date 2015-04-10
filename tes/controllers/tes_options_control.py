"""
"""

from PyQt4 import QtGui, QtCore

class TesOptionsControl(object):
    """
    """

    def __init__(self, model, view):
        """
        """

        self.model = model
        self.view = view
        
    def handle_measurement_button(self):
        """
        """

        directory = QtGui.QFileDialog.getExistingDirectory(
                self.view, 'Measurement directory..')
        self.view.measurement_edit.setText(directory)

    def update_view(self):
        """
        """

        technique = str(self.view.technique_combo_box.currentText())

        if ('Water Band' in technique):
            self._set_water_band()
        elif ('Fixed' in technique):
            if ('Multiple' in technique):
                self._set_multi_fixed()
            else:
                self._set_fixed()
        elif ('Moving' in technique):
            if ('Multiple' in technique):
                self._set_multi_moving()
            else:
                self._set_moving()
        else:
            self._set_known()

    def _set_water_band(self):
        """
        """

        self.view.tolerance_edit.setText(self.model.water_band_tolerance)
        self.view.min_temp_edit.setText(self.model.water_band_lower_temp)
        self.view.max_temp_edit.setText(self.model.water_band_upper_temp)
        self.view.max_temp_edit.setEnabled(True)
        self.view.min_wave_edit.setText('13.65')
        self.view.min_wave_edit.setEnabled(False)
        self.view.max_wave_edit.setText('13.85')
        self.view.max_wave_edit.setEnabled(False)
        self.view.win_width_edit.setEnabled(False)
        self.view.win_width_edit.clear()
        self.view.win_width_edit.setPlaceholderText('Fixed..')

    def _set_fixed(self):
        """
        """

        self.view.tolerance_edit.setText(self.model.fixed_tolerance)
        self.view.min_temp_edit.setText(self.model.fixed_lower_temp)
        self.view.max_temp_edit.setText(self.model.fixed_upper_temp)
        self.view.max_temp_edit.setEnabled(True)
        self.view.min_wave_edit.setText(self.model.fixed_lower_wave)
        self.view.min_wave_edit.setEnabled(True)
        self.view.max_wave_edit.setText(self.model.fixed_upper_wave)
        self.view.max_wave_edit.setEnabled(True)
        self.view.win_width_edit.clear()
        self.view.win_width_edit.setPlaceholderText('Fixed..')
        self.view.win_width_edit.setEnabled(False)

    def _set_moving(self):
        """
        """

        self.view.tolerance_edit.setText(self.model.moving_tolerance)
        self.view.min_temp_edit.setText(self.model.moving_lower_temp)
        self.view.max_temp_edit.setText(self.model.moving_upper_temp)
        self.view.max_temp_edit.setEnabled(True)
        self.view.min_wave_edit.setText(self.model.moving_lower_wave)
        self.view.min_wave_edit.setEnabled(True)
        self.view.max_wave_edit.setText(self.model.moving_upper_wave)
        self.view.max_wave_edit.setEnabled(True)
        self.view.win_width_edit.setText(self.model.moving_width)
        self.view.win_width_edit.setEnabled(True)

    def _set_multi_fixed(self):
        """
        """

        self.view.tolerance_edit.setText(self.model.multi_fixed_tolerance)
        self.view.min_temp_edit.setText(self.model.multi_fixed_lower_temp)
        self.view.max_temp_edit.setText(self.model.multi_fixed_upper_temp)
        self.view.max_temp_edit.setEnabled(True)
        self.view.min_wave_edit.setText(self.model.multi_fixed_lower_waves)
        self.view.min_wave_edit.setEnabled(True)
        self.view.max_wave_edit.setText(self.model.multi_fixed_upper_waves)
        self.view.max_wave_edit.setEnabled(True)
        self.view.win_width_edit.clear()
        self.view.win_width_edit.setPlaceholderText('Fixed..')
        self.view.win_width_edit.setEnabled(False)

    def _set_multi_moving(self):
        """
        """

        self.view.tolerance_edit.setText(self.model.multi_moving_tolerance)
        self.view.min_temp_edit.setText(self.model.multi_moving_lower_temp)
        self.view.max_temp_edit.setText(self.model.multi_moving_upper_temp)
        self.view.max_temp_edit.setEnabled(True)
        self.view.min_wave_edit.setText(self.model.multi_moving_lower_wave)
        self.view.min_wave_edit.setEnabled(True)
        self.view.max_wave_edit.setText(self.model.multi_moving_upper_wave)
        self.view.max_wave_edit.setEnabled(True)
        self.view.win_width_edit.setText(self.model.multi_moving_widths)
        self.view.win_width_edit.setEnabled(True)

    def _set_known(self):
        """
        """

        self.view.tolerance_edit.setText(self.model.fixed_tolerance)
        self.view.min_temp_edit.clear()
        self.view.min_temp_edit.setText('')
        self.view.max_temp_edit.clear()
        self.view.max_temp_edit.setPlaceholderText('Fixed..')
        self.view.max_temp_edit.setEnabled(False)
        self.view.min_wave_edit.clear()
        self.view.min_wave_edit.setPlaceholderText('Fixed..')
        self.view.min_wave_edit.setEnabled(False)
        self.view.max_wave_edit.clear()
        self.view.max_wave_edit.setPlaceholderText('Fixed..')
        self.view.max_wave_edit.setEnabled(False)
        self.view.win_width_edit.clear()
        self.view.win_width_edit.setPlaceholderText('Fixed..')
        self.view.win_width_edit.setEnabled(False)

    def update_model(self):
        """
        """

        technique = str(self.view.technique_combo_box.currentText())

        if ('Water Band' in technique):
            self._update_water_band()
        elif ('Fixed' in technique):
            if ('Multiple' in technique):
                self._update_multi_fixed()
            else:
                self._update_fixed()
        elif ('Moving' in technique):
            if ('Multiple' in technique):
                self._update_multi_moving()
            else:
                self._update_moving()
        else:
            self._update_known()

    def _update_water_band(self):
        """
        """

        self.model.water_band_tolerance = str(self.view.tolerance_edit.text())
        self.model.water_band_lower_temp = str(self.view.min_temp_edit.text())
        self.model.water_band_upper_temp = str(self.view.max_temp_edit.text())

    def _update_fixed(self):
        """
        """

        print self.view.min_temp_edit.text()

        self.model.fixed_tolerance = str(self.view.tolerance_edit.text())
        self.model.fixed_lower_temp = str(self.view.min_temp_edit.text())
        self.model.fixed_upper_temp = str(self.view.max_temp_edit.text())
        self.model.fixed_lower_wave = str(self.view.min_wave_edit.text())
        self.model.fixed_upper_wave = str(self.view.max_wave_edit.text())

    def _set_moving(self):
        """
        """

        self.model.moving_tolerance = str(self.view.tolerance_edit.text())
        self.model.moving_lower_temp = str(self.view.min_temp_edit.text())
        self.model.moving_upper_temp = str(self.view.max_temp_edit.text())
        self.model.moving_lower_wave = str(self.view.min_wave_edit.text())
        self.model.moving_upper_wave = str(self.view.max_wave_edit.text())
        self.model.moving_width = str(self.view.win_width_edit.text())

    def _set_multi_fixed(self):
        """
        """

        self.model.multi_fixed_tolerance = str(self.view.tolerance_edit.text())
        self.model.multi_fixed_lower_temp = str(self.view.min_temp_edit.text())
        self.model.multi_fixed_upper_temp = str(self.view.max_temp_edit.text())
        self.model.multi_fixed_lower_waves = str(self.view.min_wave_edit.text())
        self.model.multi_fixed_upper_waves = str(self.view.max_wave_edit.text())

    def _set_multi_moving(self):
        """
        """

        self.model.multi_moving_tolerance = str(self.view.tolerance_edit.text())
        self.model.multi_moving_lower_temp = str(self.view.min_temp_edit.text())
        self.model.multi_moving_upper_temp = str(self.view.max_temp_edit.text())
        self.model.multi_moving_lower_wave = str(self.view.min_wave_edit.text())
        self.model.multi_moving_upper_wave = str(self.view.max_wave_edit.text())
        self.model.multi_moving_widths = str(self.view.win_width_edit.text())

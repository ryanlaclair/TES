"""
File:       tes_options_control.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

from PyQt4 import QtGui, QtCore

class TesOptionsControl(object):
    """A controller class that handles any actions to be performed by the
    options frame.
    """

    def __init__(self, model, view):
        """instance constructor.

        arguments:
            model - the tesguimodel object.
            view - the tesmainwindow object.
        """

        self.model = model
        self.view = view
        
    def handle_measurement_button(self):
        """The event handler for the measurement selection button.
        """

        directory = QtGui.QFileDialog.getExistingDirectory(
                self.view, 'Measurement directory..')
        self.view.measurement_edit.setText(directory)

    def update_view(self):
        """Update the options view.
        """

        technique = str(self.view.technique_combo_box.currentText())

        if ('Fixed' in technique):
            if ('Multiple' in technique):
                self._set_multi_fixed()
            else:
                self._set_fixed()
        elif ('Moving' in technique):
            self._set_moving()
        else:
            self._set_known()

    def _set_fixed(self):
        """Set the default fixed window options.
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
        """Set the defualt moving window options.
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
        """Set the default multi-fixed window options.
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

# Multiple moving window method is not currently implemented.
#
#    def _set_multi_moving(self):
#        """Set the default multiple moving window options.
#        """
#
#        self.view.tolerance_edit.setText(self.model.multi_moving_tolerance)
#        self.view.min_temp_edit.setText(self.model.multi_moving_lower_temp)
#        self.view.max_temp_edit.setText(self.model.multi_moving_upper_temp)
#        self.view.max_temp_edit.setEnabled(True)
#        self.view.min_wave_edit.setText(self.model.multi_moving_lower_wave)
#        self.view.min_wave_edit.setEnabled(True)
#        self.view.max_wave_edit.setText(self.model.multi_moving_upper_wave)
#        self.view.max_wave_edit.setEnabled(True)
#        self.view.win_width_edit.setText(self.model.multi_moving_widths)
#        self.view.win_width_edit.setEnabled(True)

    def _set_known(self):
        """Set the known temperature options.
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
        """Update the model.
        """

        technique = str(self.view.technique_combo_box.currentText())

        if ('Fixed' in technique):
            if ('Multiple' in technique):
                self._update_multi_fixed()
            else:
                self._update_fixed()
        elif ('Moving' in technique):
            self._update_moving()
        else:
            self._update_known()

    def _update_fixed(self):
        """Update fixed window data in model.
        """

        self.model.fixed_tolerance = str(self.view.tolerance_edit.text())
        self.model.fixed_lower_temp = str(self.view.min_temp_edit.text())
        self.model.fixed_upper_temp = str(self.view.max_temp_edit.text())
        self.model.fixed_lower_wave = str(self.view.min_wave_edit.text())
        self.model.fixed_upper_wave = str(self.view.max_wave_edit.text())

    def _update_moving(self):
        """Update moving window data in model.
        """

        self.model.moving_tolerance = str(self.view.tolerance_edit.text())
        self.model.moving_lower_temp = str(self.view.min_temp_edit.text())
        self.model.moving_upper_temp = str(self.view.max_temp_edit.text())
        self.model.moving_lower_wave = str(self.view.min_wave_edit.text())
        self.model.moving_upper_wave = str(self.view.max_wave_edit.text())
        self.model.moving_width = str(self.view.win_width_edit.text())

    def _update_multi_fixed(self):
        """Update multi-fixed window data in model.
        """

        self.model.multi_fixed_tolerance = str(self.view.tolerance_edit.text())
        self.model.multi_fixed_lower_temp = str(self.view.min_temp_edit.text())
        self.model.multi_fixed_upper_temp = str(self.view.max_temp_edit.text())
        self.model.multi_fixed_lower_waves = str(self.view.min_wave_edit.text())
        self.model.multi_fixed_upper_waves = str(self.view.max_wave_edit.text())

# Multiple moving window method is not currently implemented.
#
#    def _update_multi_moving(self):
#        """Update multi-moving window data in model.
#        """
#
#        self.model.multi_moving_tolerance = str(self.view.tolerance_edit.text())
#        self.model.multi_moving_lower_temp = str(self.view.min_temp_edit.text())
#        self.model.multi_moving_upper_temp = str(self.view.max_temp_edit.text())
#        self.model.multi_moving_lower_wave = str(self.view.min_wave_edit.text())
#        self.model.multi_moving_upper_wave = str(self.view.max_wave_edit.text())
#        self.model.multi_moving_widths = str(self.view.win_width_edit.text())

    def _update_known(self):
        """Update known temperature data in model.
        """

        self.model.known_temp = str(self.view.min_temp_edit.text())

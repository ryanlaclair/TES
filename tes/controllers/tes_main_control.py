"""
File:       tes_main_control.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import glob
from PyQt4 import QtGui, QtCore

from ..models.dp_models.dp_measurement import DpMeasurement
from ..models.tes_models.fixed_window import FixedWindow
from ..models.tes_models.moving_window import MovingWindow
from ..models.tes_models.multiple_fixed_window import MultipleFixedWindow
from ..models.tes_models.known_temperature import KnownTemperature
from ..views.radiance_plot_window import RadiancePlotWindow
from ..views.emissivity_plot_window import EmissivityPlotWindow
from ..views.metric_plot_window import MetricPlotWindow

class TesMainControl(object):
    """A controller class that handles any actions to be performed by the main
    window.

    Attributes:
        model - The TesGuiModel object that holds the pertainant data needed by
            the program.
        view - The TesMainWindow object that contains the window GUI elements.
    """

    def __init__(self, model, view):
        """instance constructor.

        arguments:
            model - the TesGuiModel object.
            view - the TesMainWindow object.
        """

        self.model = model
        self.view = view

    def handle_ok_button(self):
        """The event handler for the ok button in the TesMainWindow.
        """

        path = str(self.view.options_view.measurement_edit.text())

        if path == '':
            pass
        else:
            self._read_measurement(path)

            technique = str(self.view.options_view.technique_combo_box.currentText())

            if ('Fixed' in technique):
                if ('Multiple' in technique):
                    self._do_multi_fixed()
                else:
                    self._do_fixed()
            elif ('Moving' in technique):
                self._do_moving()
            else:
                self._do_known()

            self.update_view()

            if self.view.options_view.radiance_plot_check.isChecked():
                RadiancePlotWindow(self.model)

            if self.view.options_view.emissivity_plot_check.isChecked():
                EmissivityPlotWindow(self.model)

            if self.view.options_view.metric_plot_check.isChecked():
                MetricPlotWindow(self.model)

    def handle_cancel_button(self):
        """The event handler for the cancel button in the TesMainWindow.
        """

        self.view.close()

    def _read_measurement(self, path):
        """Read the measurement files in a directory.

        Arguments:
            path - The full path to the directory of measurement files.
        """

        files = glob.glob(path + '/*.*')
        files.sort(key=lambda f: f[-3:])

        cbb_file = files[0]
        wbb_file = files[3]
        sam_file = files[2]
        dwr_file = files[1]

        self.model.measurement = DpMeasurement(cbb_file, wbb_file, sam_file, dwr_file)

    def _do_fixed(self):
        """Perform a fixed window temperature emissivity separation.
        """

        lower_temp = float(self.model.fixed_lower_temp)
        upper_temp = float(self.model.fixed_upper_temp)
        lower_wave = float(self.model.fixed_lower_wave)
        upper_wave = float(self.model.fixed_upper_wave)

        self.model.tes_method = FixedWindow(lower_temp, upper_temp,
                lower_wave, upper_wave)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_moving(self):
        """Perform a moving window temperature emissivity separation.
        """

        lower_temp = float(self.model.moving_lower_temp)
        upper_temp = float(self.model.moving_upper_temp)
        lower_wave = float(self.model.moving_lower_wave)
        upper_wave = float(self.model.moving_upper_wave)
        width = float(self.model.moving_width)

        self.model.tes_method = MovingWindow(lower_temp, upper_temp,
                lower_wave, upper_wave, width)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_multi_fixed(self):
        """Perform a fixed window temperature emissivity separation.
        """

        lower_temp = float(self.model.multi_fixed_lower_temp)
        upper_temp = float(self.model.multi_fixed_upper_temp)
        lw = self.model.multi_fixed_lower_waves.split(',')
        lower_waves = [float(wave) for wave in lw]
        uw = self.model.multi_fixed_upper_waves.split(',')
        upper_waves = [float(wave) for wave in uw]

        self.model.tes_method = MultipleFixedWindow(lower_temp, upper_temp,
                lower_waves, upper_waves)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

# Multiple moving window method is not currently implemented.
#
#    def _do_multi_moving(self):
#        """Perform a multiple moving window temperature emissivity separation.
#        """
#
#        lower_temp = float(self.model.multi_moving_lower_temp)
#        upper_temp = float(self.model.multi_moving_upper_temp)
#        lower_wave = float(self.model.multi_moving_lower_wave)
#        upper_wave = float(self.model.multi_moving_upper_wave)
#        w = self.model.multi_moving_widths
#        widths = [float(width) for width in w]
#
#        self.model.tes_method = MultipleMovingWindow(lower_temp, upper_temp,
#                lower_wave, upper_wave, widths)
#        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_known(self):
        """Perform a known temperature emissivity calculation.
        """

        known_temp = float(self.model.known_temp)

        self.model.tes_method = KnownTemperature(known_temp)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def update_view(self):
        """Update the main window view.
        """

        self.view.temperature_edit.setText(str(self.model.emissivity.temperature) + 'K')

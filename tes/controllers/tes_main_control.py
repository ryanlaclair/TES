"""
"""

import glob
from PyQt4 import QtGui, QtCore

from ..models.dp_models.dp_measurement import DpMeasurement
from ..models.tes_models.water_band import WaterBand
from ..models.tes_models.fixed_window import FixedWindow
from ..models.tes_models.moving_window import MovingWindow
from ..models.tes_models.multiple_fixed_window import MultipleFixedWindow
from ..models.tes_models.multiple_moving_window import MultipleMovingWindow

class TesMainControl(object):
    """
    """

    def __init__(self, model, view):
        """
        """

        self.model = model
        self.view = view

    def handle_ok_button(self):
        """
        """

        path = str(self.view.options_view.measurement_edit.text())

        if path == '':
            pass
        else:
            self._read_measurement(path)

            technique = str(self.view.options_view.technique_combo_box.currentText())

            if ('Water Band' in technique):
                self._do_water_band()
            elif ('Fixed' in technique):
                if ('Multiple' in technique):
                    self._do_multi_fixed()
                else:
                    self._do_fixed()
            elif ('Moving' in technique):
                if ('Multiple' in technique):
                    self._do_multi_moving()
                else:
                    self._do_moving()
            else:
                self._do_known()

        self.update_view()

    def handle_cancel_button(self):
        """
        """

        self.view.close()

    def _read_measurement(self, path):
        """
        """

        files = glob.glob(path + '/*.*')
        files.sort(key=lambda f: f[-3:])

        cbb_file = files[0]
        wbb_file = files[3]
        sam_file = files[2]
        dwr_file = files[1]

        self.model.measurement = DpMeasurement(cbb_file, wbb_file, sam_file, dwr_file)

    def _do_water_band(self):
        """
        """

        lower_temp = float(self.model.water_band_lower_temp)
        upper_temp = float(self.model.water_band_upper_temp)

        self.model.tes_method = WaterBand(lower_temp, upper_temp)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_fixed(self):
        """
        """

        lower_temp = float(self.model.fixed_lower_temp)
        upper_temp = float(self.model.fixed_upper_temp)
        lower_wave = float(self.model.fixed_lower_wave)
        upper_wave = float(self.model.fixed_upper_wave)

        self.model.tes_method = FixedWindow(lower_temp, upper_temp,
                lower_wave, upper_wave)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_moving(self):
        """
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
        """
        """

        lower_temp = float(self.model.multi_fixed_lower_temp)
        upper_temp = float(self.model.multi_fixed_upper_temp)
        lw = self.model.multi_fixed_lower_waves.split(',')
        lower_waves = [float(wave) for waves in lw]
        uw = self.model.multi_fixed_upper_wave.split(',')
        upper_waves = [float(wave) for wave in uw]

        self.model.tes_method = MultipleFixedWindow(lower_temp, upper_temp,
                lower_waves, upper_waves)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_multi_moving(self):
        """
        """

        lower_temp = float(self.model.multi_moving_lower_temp)
        upper_temp = float(self.model.multi_moving_upper_temp)
        lower_wave = float(self.model.multi_moving_lower_wave)
        upper_wave = float(self.model.multi_moving_upper_wave)
        w = self.model.multi_moving_widths
        widths = [float(width) for width in w]

        self.model.tes_method = MultipleMovingWindow(lower_temp, upper_temp,
                lower_wave, upper_wave, widths)
        self.model.emissivity = self.model.tes_method.find_temperature(self.model.measurement)

    def _do_known(self):
        """
        """

        pass

    def update_view(self):
        """
        """

        self.view.temperature_edit.setText(str(self.model.emissivity.temperature) + 'K')

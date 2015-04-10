"""
"""

import glob
from PyQt4 import QtGui, QtCore

from ..models.dp_models.dp_measurement import DpMeasurement

class TesMainControl(object):
    """
    """

    def __init__(self, model, view):
        """
        """

        self.view = view
        self.model = model
        self.measurement = None

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

        self.measurement = DpMeasurement(cbb_file, wbb_file, sam_file, dwr_file)

    def _do_water_band(self):
        """
        """

        

    def _do_fixed(self):
        """
        """

        pass

    def _do_moving(self):
        """
        """

        pass

    def _do_multi_fixed(self):
        """
        """

        pass

    def _do_multi_moving(self):
        """
        """

        pass

    def _do_known(self):
        """
        """

        pass

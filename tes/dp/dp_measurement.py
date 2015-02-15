"""
File:       dp_measurement.py

Author:     Ryan LaClair <rgl8828@rit.edu>

Adapted from code written by Carl Salvaggio <salvaggio@cis.rit.edu>.
"""

import numpy as np

from dp_file import DpFile
from dp_header import DpHeader
from dp_data import DpData
from ..utils.bb_radiance import bb_radiance

class DpMeasurement(object):
    """A class that holds the information relavent to a complete measurement
    taken with a D&P Instruments Model 103F MicroFT or Model 202 TurboFT.

    Attributes:
        wbb - A DpFile instance holding the warm blackbody information.
        cbb - A DpFile instance holding the cold blackbody information.
        sam - A DpFile instance holding the sample information
        dwr - A DpFile instance holding the downwelling information, or None.
    """

    def __init__(self, cbb_file, wbb_file, sam_file, dwr_file):
        """DpMeasurement instance constructor.
        """

        self.cbb = DpFile(cbb_file)
        self.wbb = DpFile(wbb_file)
        self.sam = DpFile(sam_file)
        
        if (not dwr_file==None):
            self.dwr = DpFile(dwr_file)
        else:
            self.dwr = None

        self._calibrate_measurement()

    def _calibrate_measurement(self):
        """Calibrate the data for a measurement.
        """

        cold_blackbody = bb_radiance(self.cbb.header.cbb_temperature + 273.15,
                self.cbb.data.wavelength)
        warm_blackbody = bb_radiance(self.wbb.header.wbb_temperature + 273.15,
                self.wbb.data.wavelength)

        self.wbb.data.average_spectrum[0] = 1
        self.wbb.data.average_spectrum[2047] = 1

        calibration_slope = ((warm_blackbody - cold_blackbody) /
                (self.wbb.data.average_spectrum - self.cbb.data.average_spectrum))
        calibration_offset = warm_blackbody - (self.wbb.data.average_spectrum * 
                calibration_slope)

        self.wbb.calibrate_file(calibration_slope, calibration_offset)
        self.cbb.calibrate_file(calibration_slope, calibration_offset)
        self.sam.calibrate_file(calibration_slope, calibration_offset)

        if not self.dwr is None:
            self.dwr.calibrate_file(calibration_slope, calibration_offset)

            # plate stuff
            plate_temperature = self.dwr.header.spare_f[0]
            plate_emissivity = -1
            if (plate_emissivity == -1) :
                plate_emissivity = self.dwr.header.spare_f[1]

            plate_blackbody = bb_radiance(plate_temperature + 273.15,
                    self.dwr.data.wavelength)
            plate_emission = plate_emissivity * plate_blackbody
            self.dwr.data.spectrum = ((self.dwr.data.spectrum - plate_emission) /
                    (1 - plate_emissivity))

    def check_consistency(self, lower_wave, upper_wave, tolerance):
        """
        """

        errors = []
        
        errors.append(self.wbb.check_file(lower_wave, upper_wave))
        errors.append(self.cbb.check_file(lower_wave, upper_wave))
        errors.append(self.sam.check_file(lower_wave, upper_wave))

        if not self.dwr is None:
            errors.append(self.dwr.check_file(lower_wave, upper_wave))

        errors = np.array(errors)

        if errors.max() > tolerance:
            return False
        else:
            return True

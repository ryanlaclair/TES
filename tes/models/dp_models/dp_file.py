"""
File:       dp_file.py

Author:     Ryan LaClair <rgl8828@rit.edu>

Adapted from code written by Carl Salvaggio <salvaggio@cis.rit.edu>.
"""

import struct
import numpy as np

from dp_header import DpHeader
from dp_data import DpData

class DpFile(object):
    """A class that holds the information from one file output by a D&P
    Instruments Model 103F MicroFT or Model 202 TurboFT.

    Attributes:
        file_name - The data file name.
        header - A DpHeader instance holding the header information.
        data - A DpData instance holding the radiometric information.
    """

    def __init__(self, file_name):
        """DpFile instance constructor.

        Arguments:
            file_name - The filename for the data file.
        """

        self.file_name = file_name
        self.header = None
        self.data = None

        self._read_file()

    def _read_file(self):
        """Read the data file.
        """

        with open(self.file_name, 'rb') as f:
            new_test = struct.unpack('<l', f.read(8)[4:])[0]
        f.close()

        with open(self.file_name, 'rb') as f:
            old_test = struct.unpack('<h', f.read(6)[4:])[0]
        f.close()

        with open(self.file_name, 'rb') as f:
            other_test = struct.unpack('<l', f.read(20)[16:])[0]
        f.close()

        open_file = open(self.file_name, 'rb')

        if (other_test==202):
            raw = open_file.read(1236)[11:]
            model = '202'
        elif ((not new_test==102) and old_test==102):
            raw = open_file.read(1133)
            model = '102old'
        elif (new_test==102 and old_test==102):
            raw = open_file.read(1224)
            model = '102new'

        self.header = DpHeader(raw, model)

        self.data = DpData(open_file, 
                model, 
                self.header.interferogram_size, 
                self.header.number_of_coadds, 
                2048*self.header.zero_fill,
                self.header.laser_wavelength_microns, 
                self.header.dispersion_constant_xm,
                self.header.dispersion_constant_xb)

        open_file.close()

    def calibrate_file(self, calibration_slope, calibration_offset):
        """Calibrate the radiance data read from the file.

        Arguments:
            calibration_slope - The calculated calibration slope.
            calibration_offset - The calculated calibration offset.
        """

        self.data.average_spectrum = (calibration_slope * self.data.average_spectrum 
                + calibration_offset)

        individual_wavelength = np.zeros(2048)
        individual_slope = np.zeros(2048)
        individual_offset = np.zeros(2048)

        for i_wavelength in range(2048):
            individual_wavelength[i_wavelength] = self.data.wavelength[
                    i_wavelength * self.header.zero_fill]
            individual_slope[i_wavelength] = calibration_slope[
                    i_wavelength * self.header.zero_fill]
            individual_offset[i_wavelength] = calibration_offset[
                    i_wavelength * self.header.zero_fill]

        index = np.argsort(individual_wavelength)
        individual_wavelength = individual_wavelength[index]
        self.data.individual_wavelength = individual_wavelength
        average_spectrum = self.data.average_spectrum[index]

        i_min = np.argmin(abs(individual_wavelength - 8.0))
        i_max = np.argmin(abs(individual_wavelength - 14.0))

        for i in range(self.header.number_of_coadds):
            i_center_burst = np.argmax(np.absolute(self.data.interferogram[i]))

            size = self.header.interferogram_size
            interferogram_shift = size/2 - i_center_burst

            self.data.interferogram[i] = np.roll(self.data.interferogram[i], 
                    interferogram_shift)
            self.data.interferogram[i] = self.data.interferogram[i][
                    size/2-2048:size/2+2048]

            window_fn = np.hanning(4096)
        
            spectrum = np.fft.fft(self.data.interferogram[i] * window_fn)
            spectrum = spectrum/3300
            spectrum = individual_slope * np.absolute(spectrum[0:2048]
                    ) + individual_offset
            spectrum = spectrum[index]

            self.data.spectrum.append(spectrum)

    def check_file(self, lower_wave, upper_wave):
        """Check the consistency across individual scans in the file.

        Arguments:
            lower_wave - The minimum wavelength in the range to be used.
            upper_wave - The maximum wavelength in the range to be used.

        Returns:
            The ratio of the minimum to the maximum area under the normalized
            radiance curves within the range sepcified.
        """

        i_min = np.argmin(abs(self.data.individual_wavelength - lower_wave))
        i_max = np.argmin(abs(self.data.individual_wavelength - upper_wave))

        areas = []

        for i in range(0, self.header.number_of_coadds):
            spectrum = self.data.spectrum[i]

            normalized_spectrum = spectrum / self.data.average_spectrum

            area = np.trapz(normalized_spectrum[i_min:i_max], 
                    self.data.individual_wavelength[i_min:i_max])
            areas.append(area)

        areas = np.array(areas)

        return areas.min()/areas.max()

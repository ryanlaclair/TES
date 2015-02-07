"""
File:       dp_data.py

Author:     Ryan LaClair <rgl8828@rit.edu>

Adapted from code written by Carl Salvaggio <salvaggio@cis.rit.edu>.
"""

import numpy as np

class DpData(object):
    """A class that holds the radiometric information for a file output by a
    D&P Instruments Model 103F MicroFT or Model 202 TurboFT.

    Attributes:
        interferogram_size - The number of measurements in 1 interferogram
            scan.
        number_of_coadds - The number of scans taken.
        spectrum_size - The number of elements in the spectrum measured.
        dispersion_constant_xm -
        dispersion_constant_xb -
        largest_wavenumber - The upper wavenumber limit.
    """

    def __init__(self, interferogram_size,
                       number_of_coadds,
                       spectrum_size,
                       laser_wavelength_micron,
                       dispersion_constant_xm,
                       dispersion_constant_xb):
        """DpData instance constructor.
        """

        self.interferogram_size = interferogram_size
        self.number_of_coadds = number_of_coadds
        self.spectrum_size = spectrum_size
        self.dispersion_constant_xm = dispersion_constant_xm
        self.dispersion_constant_xb = dispersion_constant_xb
        self.largest_wavenumber = 10000.0 / (2.0 * laser_wavelength_micron)

        self.interferogram = []
        self.frequency = None
        self.spectrum = []
        self.wavelength = None

    def read_data(self, open_file, model):
        """Read the radiometric data.

        Args:
            open_file - The currently open data file.
            model - The D&P Instrument model.
        """

        if (model=='102old'):
            self._read_old_data(open_file)
        else:
            self._read_new_data(open_file)

        self._calc_frequency()
        self._calc_wavelength()

    def _read_new_data(self, open_file):
        """Private helper method to read data output in the "new" format.

        Args:
            open_file - The currently open data file.
        """

        for i in range(self.number_of_coadds):
            i_value = np.fromfile(open_file, dtype='<i2',
                    count=self.interferogram_size)
            self.interferogram.append(i_value)

        self.spectrum = np.fromfile(open_file, dtype='f', count=self.spectrum_size)

    def _read_old_data(self, open_file):
        """Private helper method to read data output in the "old" format.

        Args:
            open_file - The currently open data file.
        """
        
        scan_number = 0

        for i in range(self.number_of_coadds):
            scan_number = np.fromfile(open_file, dtype='<i2', count=1)
            i_value = np.fromfile(open_file, dtype='<i2',
                    count=self.interferogram_size)
            self.interferogram.append(i_value)

        scan_number = np.fromfile(open_file, dtype='<i2', count=1)
        self.spectrum = np.fromfile(open_file, dtype='<f', count=self.spectrum_size)

    def _calc_frequency(self):
        """Private helper method to calculate the frequency values.
        """
        
        self.frequency = np.empty(self.interferogram_size)

        delta_wavenumber = self.largest_wavenumber / (self.interferogram_size/2)

        for i in range(self.interferogram_size/2):
            self.frequency[i] = (self.largest_wavenumber -
                    ((self.interferogram_size/2)-i) * delta_wavenumber)
            self.frequency[i] = (self.frequency[i] +
                    10**(self.dispersion_constant_xm *
                    self.frequency[i] + self.dispersion_constant_xb))

    def _calc_wavelength(self):
        """Private helper method to calculate the wavelength values.
        """

        self.wavelength = np.empty(self.spectrum_size)

        delta_wavenumber = self.largest_wavenumber / self.spectrum_size

        for i in range(self.spectrum_size):
            self.wavelength[i] = (self.largest_wavenumber - 
                    (self.spectrum_size-i) * delta_wavenumber)
            self.wavelength[i] = (self.wavelength[i] +
                    10**(self.dispersion_constant_xm * self.wavelength[i] +
                    self.dispersion_constant_xb))
            self.wavelength[i] = 10000.0/self.wavelength[i]

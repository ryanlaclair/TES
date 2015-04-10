"""
File:       water_band.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from tes import Tes
from emissivity import Emissivity

class WaterBand(Tes):
    """A class that represents a water band temperature emissivty
    separation object.

    Attributes:
        Inherited from Tes.
    """

    def __init__(self, lower_temp,
                       upper_temp):
        """WaterBand instance constructor.  Calls constructor for super
        class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
        """

        Tes.__init__(self, lower_temp,
                           upper_temp)

    def find_temperature(self, measurement):
        """Estimate the temperature using the water band method.

        Arguments:
            measurement - A DpMeasurement instance holding the data that will
                be used for the temperature emissivity separation.

        Returns:
            An Emissivity object that contains the result of the temperature
            emissivity separation.
        """

        sam_radiance = measurement.sam.data.average_spectrum

        if measurement.dwr is None:
            dwr_radiance = np.zeros(len(sam_radiance))
        else:
            dwr_radiance = measurement.dwr.data.average_spectrum

        wavelength = measurement.sam.data.wavelength

        # sort the data in ascending order
        index = np.argsort(wavelength)
        wavelength = wavelength[index]
        sam_radiance = sam_radiance[index]
        dwr_radiance = dwr_radiance[index]

        Tes.set_data(self, sam_radiance, dwr_radiance, wavelength)

        # the wavelengths for the waterband method 13.55, 13.85
        lower_band = np.argmin(abs(wavelength - 13.55))
        middle_band = np.argmin(abs(wavelength - 13.7))
        upper_band = np.argmin(abs(wavelength - 13.85))

        # the window to calculate the emissivity over
        lower_win = np.argmin(abs(wavelength - 8.0))
        upper_win = np.argmin(abs(wavelength - 14.0))

        Tes.set_windows(self, [[lower_win, upper_win]])

        emissivities = []

        for temp in range(len(self.temps)):
            emissivities.append(Emissivity(self.temps[temp], self.wavelength,
                self.sam_radiance, self.dwr_radiance, self.window_indices, False))

            if np.isnan(emissivities[-1].assd):
                emissivities[-1].assd = np.inf

        diffs = []

        for emissivity in emissivities:
            window = emissivity.emissivity[lower_band:upper_band]
            diff = abs((emissivity.emissivity[lower_band] + 
                emissivity.emissivity[upper_band]) / 2 - 
                emissivity.emissivity[middle_band])
            diffs.append(diff)

        index = np.argmin(diffs)

        return emissivities[index]

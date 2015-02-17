"""
File:       water_band.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from tes import Tes
from ..emissivity import Emissivity

class WaterBand(Tes):
    """A class that represents a water band temperature emissivty
    separation object.

    Attributes:
        Inherited from Tes.
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave):
        """WaterBand instance constructor.  Calls constructor for super
        class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_wave - The minimum wavelength in the range to be tested.
            upper_wave - The maximum wavelength in the range ot be tested.
        """

        lower_win_width = 0
        upper_win_width = 0
        win_steps = 0
        num_wins = 0

        Tes.__init__(self, lower_temp,
                           upper_temp,
                           lower_wave,
                           upper_wave,
                           lower_win_width,
                           upper_win_width,
                           win_steps,
                           num_wins)

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

        guess = []

        lower_band = np.argmin(abs(wavelength - self.lower_wave))
        upper_band = np.argmin(abs(wavelength - self.upper_wave))
        middle_band = np.argmin(abs(wavelength - 13.7))

        for temp in range(len(self.temps)):
            guess.append(Emissivity(self.temps[temp], wavelength,
                sam_radiance, dwr_radiance, lower_band, upper_band, False))

        diffs = []

        for emissivity in guess:
            #window = em[lowerIndex+1:upperIndex]
            #diffs.append(np.std(window))
            window = emissivity.emissivity[lower_band:upper_band]
            diff = abs((emissivity.emissivity[lower_band] + 
                emissivity.emissivity[upper_band]) / 2 - 
                emissivity.emissivity[middle_band])
            diffs.append(diff)

        index = np.argmin(diffs)

        return guess[index]

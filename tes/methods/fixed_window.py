"""
File:       fixed_window.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from tes import Tes

class FixedWindow(Tes):
    """A class that represents a standard temperature emissivity separation
    object.

    Attributes:
        Inherited from Tes.
        lower_wave - 
        upper_wave - 
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave):
        """Standard instance constructor.  Calls constructor for super class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_wave -
            upper_wave -
        """

        self.lower_wave = lower_wave
        self.upper_wave = upper_wave

        Tes.__init__(self, lower_temp,
                           upper_temp)

    def find_temperature(self, measurement):
        """Estimate the temperature using the standard method.

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

        lower_win = np.argmin(abs(wavelength - self.lower_wave))
        upper_win = np.argmin(abs(wavelength - self.upper_wave))

        Tes.set_windows(self, [[lower_win, upper_win]])

        # call the super class find_temperature method
        return Tes.find_temperature(self)

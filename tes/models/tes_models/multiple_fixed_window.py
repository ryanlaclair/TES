"""
File:       multiple_fixed_window.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from tes import Tes

class MultipleFixedWindow(Tes):
    """A class that represents a moving window temperature emissivity
    separation object.

    Attributes:
        Inherited from Tes.
        lower_waves - The lower wavelengths of the windows being examined.
        upper_waves - The upper wavelengths of the windows being examined.
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_waves,
                       upper_waves):
        """MovingWindow instance constructor.  Calls constructor for super
        class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_waves - The lower wavelengths of the windows being examined.
            upper_waves - The upper wavelengths of the windows being examined.
        """

        self.lower_waves = lower_waves
        self.upper_waves = upper_waves

        Tes.__init__(self, lower_temp,
                           upper_temp)

    def find_temperature(self, measurement):
        """Estimate the temperature using moving window method.

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
        
        window_indices = []

        for i in range(len(self.lower_waves)):
            lower_win = np.argmin(abs(wavelength - self.lower_waves[i]))
            upper_win = np.argmin(abs(wavelength - self.upper_waves[i]))

            window_indices.append([lower_win, upper_win])

        Tes.set_windows(self, window_indices)

        # call the super class find_temperature method
        return Tes.find_temperature(self)

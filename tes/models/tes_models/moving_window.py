"""
File:       moving_window.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from tes import Tes

class MovingWindow(Tes):
    """A class that represents a moving window temperature emissivity
    separation object.

    Attributes:
        Inherited from Tes.
        lower_wave - The lower wavelength of the window being examined.
        upper_wave - The upper wavelength of the window being examined.
        window_width - The width of the moving window.
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave,
                       window_width):
        """MovingWindow instance constructor.  Calls constructor for super
        class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_wave - The lower wavelength of the window being examined.
            upper_wave - The upper wavelength of the window being examined.
            window_width - The width of the moving window.
        """

        self.lower_wave = lower_wave
        self.upper_wave = upper_wave
        self.window_width = window_width

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

        emissivities = []

        lower_wave = self.lower_wave
        lower_win = np.argmin(abs(wavelength - lower_wave))
        upper_win = 0

        upper_limit = np.argmin(abs(wavelength - self.upper_wave))

        while (upper_win < upper_limit):
            upper_win = np.argmin(abs(wavelength - 
                (lower_wave + self.window_width)))

            Tes.set_windows(self, [[lower_win, upper_win]])

            # call the super class find_temperature method
            emissivities.append(Tes.find_temperature(self))

            lower_win += 1
            lower_wave = wavelength[lower_win]

        self.emissivities = emissivities

        return min(self.emissivities)

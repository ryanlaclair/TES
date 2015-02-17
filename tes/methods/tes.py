"""
File:       tes.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from ..emissivity import Emissivity

class Tes(object):
    """A base class that represents a generic temperature emissivity separation
    object.

    Attributes:
        temps - A numpy array of the temperatures to be tested.
        lower_wave - The minimum wavelength in the range to be tested.
        upper_wave - The maximum wavelength in the range to be tested.
        windows - A numpy array of the window widths to be used.
        num_wins - The number of concurrent windows.
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave,
                       lower_win_width,
                       upper_win_width,
                       win_steps,
                       num_wins):
        """Tes instance constructor.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_wave - The minimum wavelength in the range to be tested.
            upper_wave - The maximum wavelength in the range ot be tested.
            lower_win_width - The minimum window width.
            upper_win_width - The maximum window width.
            win_steps - The number of different window sizes.
            num_wins - The number of concurrent windows.
        """

        self.temps = np.arange(lower_temp, upper_temp+1, 0.1)
        self.lower_wave = lower_wave
        self.upper_wave = upper_wave
        self.windows = np.linspace(lower_win_width, upper_win_width, win_steps)
        self.num_wins = num_wins

    def find_temperature(self, measurement):
        """The base temperature emissivity separation method.

        Arguments:
            measurement - A DpMeasurement instance holding the data that will
                be used for the temperature emissivity separation.

        Returns:
            A list of Emissivity objects that represent possible temperature/
            emissivity combinations for the given data.
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

        # clip the data to the wavelength range being examined
        lower_index = np.argmin(abs(wavelength - self.lower_wave))
        upper_index = np.argmin(abs(wavelength - self.upper_wave))
        wavelength = wavelength[lower_index:upper_index]
        sam_radiance = sam_radiance[lower_index:upper_index]
        dwr_radiance = dwr_radiance[lower_index:upper_index]

        window_data = []

        # generate emissivities for each window width
        for width in self.windows:
            window_data += self._test_window(width, wavelength, 
                sam_radiance, dwr_radiance)

        return window_data

    def _test_window(self, width, wavelength, sam_radiance, dwr_radiance):
        """Find the smoothest emissivity curve for a given window across a
        range of temperatures.

        Arguments:
            width - The current window width.
            wavelength - The wavelengths being examined.
            sam_radiance - The sample radiance data.
            dwr_radiance - The downwelling radiance data.

        Returns:
            An Emissivity object that contains the data for the smoothest
            emissivity curve for this given window.
        """

        emissivities = []

        steps = np.argmin(abs(wavelength-(wavelength[-1] - width))) + 1

        for lower_win in range(steps):
            upper_win = np.argmin(abs(wavelength - 
                (wavelength[lower_win] + width))) + 1

            guess = []

            for temp in range(len(self.temps)):
                guess.append(Emissivity(self.temps[temp], wavelength,
                    sam_radiance, dwr_radiance, lower_win, upper_win))

                if np.isnan(guess[-1].assd):
                    guess[-1].assd = np.inf
                
            emissivities.append(min(guess))

        return emissivities

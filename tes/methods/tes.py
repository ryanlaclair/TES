"""
"""

import numpy as np

from ..emissivity import Emissivity

class Tes(object):
    """
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave,
                       lower_win_width,
                       upper_win_width,
                       win_steps,
                       num_wins):
        """
        """

        self.temps = np.arange(lower_temp, upper_temp+1, 0.1)
        self.lower_wave = lower_wave
        self.upper_wave = upper_wave
        self.windows = np.linspace(lower_win_width, upper_win_width, win_steps)
        self.num_wins = num_wins

    def find_temperature(self, measurement):
        """
        """

        sam_radiance = measurement.sam.data.average_spectrum

        if measurement.dwr is None:
            dwr_radiance = np.zeros(len(sam_radiance))
        else:
            dwr_radiance = measurement.dwr.data.average_spectrum

        wavelength = measurement.sam.data.wavelength

        index = np.argsort(wavelength)
        wavelength = wavelength[index]
        sam_radiance = sam_radiance[index]
        dwr_radiance = dwr_radiance[index]

        lower_index = np.argmin(abs(wavelength - self.lower_wave))
        upper_index = np.argmin(abs(wavelength - self.upper_wave))
        wavelength = wavelength[lower_index:upper_index]
        sam_radiance = sam_radiance[lower_index:upper_index]
        dwr_radiance = dwr_radiance[lower_index:upper_index]

        window_data = []

        for width in self.windows:
            window_data += self._test_window(width, wavelength, 
                sam_radiance, dwr_radiance)

        return window_data

    def _test_window(self, width, wavelength, sam_radiance, dwr_radiance):
        """
        """

        emissivities = []

        steps = np.argmin(abs(wavelength-(wavelength[-1] - width))) + 1

        for lower_win in range(steps):
            upper_win = np.argmin(abs(wavelength - 
                (wavelength[lower_win] + width))) + 1

            guess = []

            for temp in range(len(self.temps)):
                guess.append(Emissivity(self.temps[temp], 
                    wavelength[lower_win:upper_win],
                    sam_radiance[lower_win:upper_win],
                    dwr_radiance[lower_win:upper_win]))

                if np.isnan(guess[-1].assd):
                    guess[-1].assd = np.inf
                
            emissivities.append(min(guess))

        return emissivities

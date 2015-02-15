"""
"""

import numpy as np

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

        self.temps = np.arrange(lower_temp, upper_temp+1, 0.1)
        self.lower_wave = lower_wave
        self.upper_wave = upper_wave
        self.windows = np.linspace(lower_win_width, upper_win_width, win_steps)
        self.num_wins = num_wins

    def find_temperature(self, measurement):
        """
        """

        sam_radiance = measurement.sam.data.spectrum

        if emissivity.measurement.dwr is None:
            dwr_radiance = np.zeros(len(sam_radiance))
        else:
            dwr_radiance = measurement.dwr.data.spectrum

        wavelength = measurement.sam.data.wavelength

        index = np.argsort(wavelength)
        wavelength = wavelength[index]
        sam_radiance = sam_radiance[wavelength]
        dwr_radiance = dwr_radiance[wavelength]

        lower_index = np.argmin(abs(wavelength - self.lower_wave))
        upper_index = np.argmin(abs(wavelength - self.upper_wave))
        wavelength = wavelength[lower_index:upper_index]
        sam_radiance = sam_radiance[lower_index:upper_index]
        dwr_radiance = dwr_radiance[lower_index:upper_index]

        window_data = []

        for width in self.windows:
            window_data.append(self._test_window(width, wavelength, 
                sam_radiance, dwr_radiance))

        return window_data

    def _test_window(self, width, wavelength, sam_radiance, dwr_radiance):
        """
        """

        steps = int((self.upper_wave - self.lower_wave) / width)

        lower_val = self.lower_wave

        emissivities = []

        for lower_win in range(steps):
            upper_win = np.argmin(abs(wavelength - (lower_val + width))) + 1
            lower_val = wavelength[lower_win+1]

            min_assd = np.inf

            min_guess = None

            for temp in range(len(self.temps)):
                self.emissivity.lower_win = lower_win
                self.emissivity.upper_win = upper_win

                guess = Emissivity(self.temps[temp], 
                    wavelength[lower_win:upper_win],
                    sam_radiance[lower_win:upper_win],
                    dwr_radiance[lower_win:upper_win])

                if np.isnan(guess.assd):
                    guess.assd = np.inf
                
                if guess.assd < assd:
                    min_guess = guess
                    min_assd = min_guess.assd
            
            emissivities.append(min_guess)

        return emissivities

"""
"""

import itertools
import numpy as np

from tes import Tes
from ..emissivity import Emissivity

class MultipleMovingWindow(Tes):
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

        Tes.__init__(self, lower_temp,
                           upper_temp,
                           lower_wave,
                           upper_wave,
                           lower_win_width,
                           upper_win_width,
                           win_steps,
                           num_wins)

    def find_temperature(self, measurement):
        """
        """

        window_data = Tes.find_temperature(self, measurement)

        win_combos = itertools.combinations_with_replacement(
                window_data, self.num_wins)

        new_data = []

        count = 0
        for combo in win_combos:
            possible_combo = True
            temperature = combo[0].temperature
            wavelength_window = combo[0].wavelength_window

            for i in range(self.num_wins-1):
                if (combo[i].wavelength_window[-1] <= 
                        combo[i+1].wavelength_window[0]):
                    temperature += combo[i+1].temperature
                    temperature = temperature / 2
                    np.concatenate((wavelength_window, 
                        combo[i+1].wavelength_window))
                else:
                    possible_combo = False

            if possible_combo:
                new_data.append(Emissivity(temperature, wavelength_window, 
                    combo[0].sam_radiance, combo[0].dwr_radiance))
                
        return min(new_data)

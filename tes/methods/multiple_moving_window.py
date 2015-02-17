"""
File:       multiple_moving_window.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import itertools
import numpy as np

from tes import Tes
from ..emissivity import Emissivity

class MultipleMovingWindow(Tes):
    """A class that represents a multiple moving window temperature emissivity
    separation object.

    Attributes:
        Inherited from Tes.
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave,
                       lower_win_width,
                       upper_win_width,
                       win_steps,
                       num_wins):
        """MultipleMovingWindow instance constructor.  Calls constructor
        for super class.

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

        Tes.__init__(self, lower_temp,
                           upper_temp,
                           lower_wave,
                           upper_wave,
                           lower_win_width,
                           upper_win_width,
                           win_steps,
                           num_wins)

    def find_temperature(self, measurement):
        """Estimate the temperature using the multiple moving window method.

        Arguments:
            measurement - A DpMeasurement instance holding the data that will
                be used for the temperature emissivity separation.

        Returns:
            An Emissivity object that contains the result of the temperature
            emissivity separation.
        """

        # call the super class find_temperature method
        window_data = Tes.find_temperature(self, measurement)

        # all possible window combinations
        win_combos = itertools.combinations_with_replacement(
                window_data, self.num_wins)

        new_data = []

        for combo in win_combos:
            possible_combo = True
            temperature = combo[0].temperature
            wavelength = combo[0].wavelength
            lower_win = [combo[0].lower_win]
            upper_win = [combo[0].upper_win]

            # determine if windows overlap
            for i in range(self.num_wins-1):
                if (combo[i].upper_win <= combo[i+1].lower_win):
                    temperature += combo[i+1].temperature
                    temperature = temperature / 2
                    lower_win.append(combo[i+1].lower_win)
                    upper_win.append(combo[i+1].upper_win)
                else:
                    possible_combo = False

            if possible_combo:
                new_data.append(Emissivity(temperature, wavelength, 
                    combo[0].sam_radiance, combo[0].dwr_radiance, 
                    lower_win, upper_win, False))
                
        return min(new_data)

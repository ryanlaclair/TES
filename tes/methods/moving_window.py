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
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave,
                       win_width):
        """MovingWindow instance constructor.  Calls constructor for super
        class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_wave - The minimum wavelength in the range to be tested.
            upper_wave - The maximum wavelength in the range ot be tested.
            win_width - The width of the moving window.
        """

        lower_win_width = win_width
        upper_win_width = win_width
        win_steps = 1
        num_wins = 1

        Tes.__init__(self, lower_temp,
                           upper_temp,
                           lower_wave,
                           upper_wave,
                           lower_win_width,
                           upper_win_width,
                           win_steps,
                           num_wins)

    def find_temperature(self, measurement):
        """Estimate the temperature using moving window method.

        Arguments:
            measurement - A DpMeasurement instance holding the data that will
                be used for the temperature emissivity separation.

        Returns:
            An Emissivity object that contains the result of the temperature
            emissivity separation.
        """

        # call the super class find_temperature method
        window_data = Tes.find_temperature(self, measurement)

        return min(window_data)

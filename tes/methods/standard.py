"""
"""

from tes import Tes

class Standard(Tes):
    """
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave):
        """
        """

        lower_win_width = upper_wave - lower_wave
        upper_win_width = lower_win_width
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
        """
        """

        window_data = Tes.find_temperature(self, measurement)

        return window_data[0]

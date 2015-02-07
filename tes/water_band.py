"""
"""

class WaterBand(Tes):
    """
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave):
        """
        """

        lower_win_width = 0
        upper_win_width = 0
        win_steps = 0
        num_wins = 0

        Tes.__init__(self, lower_temp,
                           upper_temp,
                           lower_wave,
                           upper_wave,
                           lower_win_width,
                           upper_win_width,
                           win_steps,
                           num_wins)

    def findTemperature(emissivity):
        """
        """

        pass

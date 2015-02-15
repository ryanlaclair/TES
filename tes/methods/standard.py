"""
"""

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

        super(Standard, self).__init__(self, lower_temp, 
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

        window_data = super(Standard, self).find_temperature(measurement)

        min_assd = np.inf
        min_emissivity = None

        for emissivity in emissivities:
            if emissivity.assd < min_assd:
                min_emissivity = emissivity
                min_assd = min_emissivity.assd

        return min_emissivity

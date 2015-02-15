"""
"""

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

    def find_temperature(self, emissivity):
        """
        """

        sam_radiance = emissivity.measurement.sam.data.spectrum

        if emissivity.measurement.dwr is None:
            dwr_radiance = np.zeros(len(sam_radiance))
        else:
            dwr_radiance = emissivity.measurement.dwr.data.spectrum

        wavelength = emissivity.measurement.sam.data.wavelength

        index = np.argsort(wavelength)
        wavelength = wavelength[index]
        sam_radiance = sam_radiance[wavelength]
        dwr_radiance = dwr_radiance[wavelength]

        lower_index = np.argmin(abs(wavelength - self.lower_wave))
        upper_index = np.argmin(abs(wavelength - self.upper_wave))
        wavelength = wavelength[lower_index:upper_index]
        sam_radiance = sam_radiance[lower_index:upper_index]
        dwr_radiance = dwr_radiance[lower_index:upper_index]

        for width in self.windows:
            pass

    def _test_window(self, emissivity, width, wavelength):
        """
        """

        steps = int((self.upper_wave - self.lower_wave) / width)

        lower_val = self.lower_wave

        for lower_win in range(steps):
            upper_win = np.argmin(abs(wavelength - (lower_val + width))) + 1
            lower_val = wavelength[lower_win+1]

            win_assd = np.zeros(len(self.temps))

            for temp in range(len(self.temps)):
                bb = 

    def _deriv(self, y, x=None):
        """
        """

        n = len(y)

        if not x is None:

            n2 = n - 2

            y12 = y - np.roll(y, -1)
            y01 = np.roll(y, 1) - y
            y02 = np.roll(y, 1) - np.roll(y, -1)

            d = (np.roll(x, 1) * (y12 / (y01*y02)) + x * (1/y12 - 1/y01) -
                np.roll(x, -1) * (y01 / (y02 * y12)))
            d[0] = (x[0] * (y01[1] + y02[1]) / (y01[1] * y01[1]) - x[1] * y02[1] /
                (y01[1] * y12[1]) + x[2] * y01[1] / (y02[1] * y12[1]))
            d[-1] = (-x[n-3] * y12[n2] / (y01[n2] * y02[n2]) + x[n-2] * y02[n2] /
                (y01[n2] * y12[n2]) - x[n-1] * (y02[n2] + y12[n2]) /
                (y02[n2] * y12[n2]))

        else:

            d = (np.roll(y, -1) - np.roll(y, 1)) / 2
            d[0] = (-3 * y[0] + 4 * y[1] - y[2]) / 2
            d[n-1] = (3 * y[n-1] - 4 * y[n-2] + y[n-3]) / 2

        return d

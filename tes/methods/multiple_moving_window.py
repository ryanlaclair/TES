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
        lower_wave -
        upper_wave -
        window_widths -
    """

    def __init__(self, lower_temp,
                       upper_temp,
                       lower_wave,
                       upper_wave,
                       window_widths):
        """MultipleMovingWindow instance constructor.  Calls constructor
        for super class.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
            lower_wave - The minimum wavelength in the range to be tested.
            upper_wave - The maximum wavelength in the range ot be tested.
            window_widths - 
        """

        self.lower_wave = lower_wave
        self.upper_wave = upper_wave
        self.window_widths = window_widths

        Tes.__init__(self, lower_temp,
                           upper_temp)

    def find_temperature(self, measurement):
        """Estimate the temperature using the multiple moving window method.

        Arguments:
            measurement - A DpMeasurement instance holding the data that will
                be used for the temperature emissivity separation.

        Returns:
            An Emissivity object that contains the result of the temperature
            emissivity separation.
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

        Tes.set_data(self, sam_radiance, dwr_radiance, wavelength)

        all_windows = []

        for width in self.window_widths:
            lower_wave = self.lower_wave
            lower_win = np.argmin(abs(wavelength - lower_wave))
            upper_win = 0

            upper_limit = np.argmin(abs(wavelength - self.upper_wave))

            while (upper_win < upper_limit):
                upper_win = np.argmin(abs(wavelength - 
                    (lower_wave + width)))

                all_windows.append([lower_win, upper_win])

                lower_win += 1
                lower_wave = wavelength[lower_win]

        # all possible window combinations
        all_combos = itertools.combinations_with_replacement(
                all_windows, len(self.window_widths))

        good_windows = []

        for win_combo in all_combos:
            possible_combo = True

            # determine if windows overlap
            for i in range(len(self.window_widths)-1):
                if (win_combo[i][1] > win_combo[i+1][0]):
                    possible_combo = False

            if possible_combo:
                good_windows.append(win_combo)

        print len(good_windows)

        emissivities = []

        for window in good_windows:
            Tes.set_windows(self, window)

            emissivities.append(Tes.find_temperature(self))

        return min(emissivities)

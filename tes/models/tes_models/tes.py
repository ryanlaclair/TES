"""
File:       tes.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from emissivity import Emissivity

class Tes(object):
    """A base class that represents a generic temperature emissivity separation
    object.

    Attributes:
        temps - A numpy array of the temperatures to be tested.
        window_indices - The indices for the window being examined.
        sam_radiance - The sample radiance values.
        dwr_radiance - The downwelling radiance values.
        wavelength - An array of the wavelengths.
    """

    def __init__(self, lower_temp,
                       upper_temp):
        """Tes instance constructor.

        Arguments:
            lower_temp - The minimum temperature in the range to be tested.
            upper_temp - The maximum temperature in the range to be tested.
        """

        self.temps = np.arange(lower_temp, upper_temp+0.1, 0.1)
        self.window_indices = []
        self.sam_radiance = []
        self.dwr_radiance = []
        self.wavelength = []
        self.emissivities = []

    def set_windows(self, window_indices):
        """Set the windows being examined.

        Arguments:
            window_indices - The indices for the window being examined.
        """

        self.window_indices = window_indices

    def set_data(self, sam_radiance, dwr_radiance, wavelength):
        """Set the data currently being used.

        Arguments:
            sam_radiance - The sample radiance values.
            dwr_radiance - The downwelling radiance values.
            wavelength - An array of the wavelengths.
        """

        self.sam_radiance = sam_radiance
        self.dwr_radiance = dwr_radiance
        self.wavelength = wavelength

    def find_temperature(self):
        """The base temperature emissivity separation method.

        Returns:
            A list of Emissivity objects that represent possible temperature/
            emissivity combinations for the given data.
        """

        self.emissivities = []

        for temp in range(len(self.temps)):
            self.emissivities.append(Emissivity(self.temps[temp], self.wavelength,
                self.sam_radiance, self.dwr_radiance, self.window_indices))

            if np.isnan(self.emissivities[-1].assd):
                self.emissivities[-1].assd = np.inf

        emissivities = self.emissivities
        continue_search = True

        while continue_search and len(emissivities) > 1:
            min_idx = np.argmin(emissivities)
            current_min = emissivities[min_idx]

            if current_min == emissivities[-1]:
                emissivities = emissivities[:-1]
            elif current_min == emissivities[0]:
                emissivities = emissivities[1:]
            else:
                continue_search = False

        return current_min
        #return min(emissivities)

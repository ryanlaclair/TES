"""
File:       known_temperature.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from emissivity import Emissivity

class KnownTemperature(object):
    """A class to represent a known temperature emissivity calculation.

    Attriubutes:
        temp - The sample temperature.
    """

    def __init__(self, temp):
        """Instance constructor.

        Arguments:
            temp - The sample temperature.
        """

        self.temp = temp

    def find_temperature(self, measurement):
        """Perform the calculation.

        Arguments:
            measurement - The measurement data.
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

        return Emissivity(self.temp, wavelength, sam_radiance, dwr_radiance, [], calc_assd=False)

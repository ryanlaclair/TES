"""
File:       emissivity.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

from ...utils.deriv import deriv
from ...utils.bb_radiance import bb_radiance

class Emissivity(object):
    """A class that represents an emissivity object.

    Attributes:
        temperature - The object temperature.
        wavelength - An array of wavelength values.
        sam_radiance - The sample radiance values.
        dwr_radiance - The downwelling radiance values.
        window_indices - The indices corresponding to the wavelength windows
            being examined.
        emissivity - The calculated emissivity values.
        assd - The average squared second derivative smoothness
            metric.
    """

    def __init__(self, temperature, 
                       wavelength, 
                       sam_radiance, 
                       dwr_radiance,
                       window_indices,
                       calc_assd=True):
        """Emissivity instance contructor.

        Arguments:
            temperature - The object temperature.
            wavelength - An array of wavelength values.
            sam_radiance - The sample radiance values.
            dwr_radiance - The downwelling radiance values.
            window_indices - The indices corresponding to the wavelength
                windows being examined.
            calc_assd - A flag specifying if the ASSD should be calculated.
        """

        self.temperature = temperature
        self.wavelength = wavelength
        self.sam_radiance = sam_radiance
        self.dwr_radiance = dwr_radiance
        self.window_indices = window_indices
        
        self.emissivity = self._calc_emissivity()
        
        if calc_assd:
            self.assd = self._calc_assd()
        else:
            self.assd = 0

    def __eq__(self, other):
        """Implementation for the == operator.

        Arguments:
            other - The object being compared to.

        Returns:
            True if the assd's are equal, False if they are not, and
            NotImplemented if other is not an Emissivity instance.
        """

        if isinstance(other, Emissivity):
            return self.assd == other.assd
        else:
            return NotImplemented

    def __lt__(self, other):
        """Implementation for the < operator.

        Arguments:
            other - The object being compared to.

        Returns:
            True if the assd is less then the assd of other, False if 
            it is not, and NotImplemented if other is not an Emissivity 
            instance.
        """

        if isinstance(other, Emissivity):
            return self.assd < other.assd
        else:
            return NotImplemented

    def _calc_emissivity(self):
        """Calculate the emissivity.

        Returns:
            The calculated emissivity.
        """

        bb = bb_radiance(self.temperature, self.wavelength)
        
        return (self.sam_radiance - self.dwr_radiance) / (
                bb - self.dwr_radiance)

    def _calc_assd(self):
        """Calculate the average squared second derivitive smoothness
        metric.

        Returns:
            The calculated assd.
        """

        assd = 0

        for win in self.window_indices:
            assd += np.mean(deriv(deriv(self.emissivity[win[0]:win[1]]))**2)

        return assd/len(self.window_indices)

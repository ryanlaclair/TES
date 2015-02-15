"""
"""

import numpy as np

from utils.deriv import deriv

class Emissivity(object):
    """
    """

    def __init__(self, temperature, 
                       wavelength_window, 
                       sam_radiance, 
                       dwr_radiance):
        """
        """

        self.temperature = temperature
        self.wavelength_window = wavelength_window
        self.sam_radiance = sam_radiance
        self.dwr_radiance = dwr_radiance
        
        self.emissivity = _calc_emissivity()
        self.assd = _calc_assd()

    def _calc_emissivity(self):
        """
        """

        bb = bb_radiance(self.temperature, self.wavelength_window)
        
        return (self.sam_radiance - self.dwr_radiance) / (
                bb - self.dwr_radiance)

    def _calc_assd(self):
        """
        """

        return np.mean(deriv(deriv(self.emissivity))**2)

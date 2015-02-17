"""
File:       bb_radiance.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import numpy as np

def bb_radiance(absolute_temperature, wavelength):
    """Calculate the spectral blackbody radiance.

    Arguments:
        absolute_temperature - Temperature in Kelvin.
        wavelength - Numpy array of wavelengths in microns.

    Returns:
        Array same size as wavelength array of spectral blackbody radiance
        values in units of W/m^2/sr/micron.
    """

    T = float(absolute_temperature)

    c1 = 3.74151 * (10**8)          # W / m^2 / micron
    c2 = 1.43879 * (10**4)          # micron K
    M = c1 / (wavelength**5) / (np.exp(c2 / wavelength / T) - 1)
    L = M / np.pi

    return L

"""
"""

import numpy as np

def deriv(y, x=None):
    """Performs numerical differentiation using 3-point, Lagrangian
    interpolation.

    arguments:
        y - The variable to be differentiated.
        x - The variable to differentiate with respect to.  If not specified,
            unit spacing is assumed.

    returns:
        The calculated derivcative.
    """

    n = len(y)

    if (n < 3):
        raise IndexError('Parameters must have at least 3 points.')

    if not x is None:

        n2 = n - 2

        #y = np.astype(y, float)
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

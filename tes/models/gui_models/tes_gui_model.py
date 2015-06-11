"""
File:       tes_gui_model.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import xml.etree.ElementTree as et

class TesGuiModel(object):
    """A model class that holds all of the data used for the temperature
    emissivity separation program.

    Attributes:
        All of the data memebers for each TES type.
    """

    def __init__(self):
        """Instance constructor.  Initialize all attributes and call method
        to parse the config file.
        """

        self.config_file = 'tes/tes_config.xml'

        self.fixed_tolerance = ''
        self.fixed_lower_temp = ''
        self.fixed_upper_temp = ''
        self.fixed_lower_wave = ''
        self.fixed_upper_wave = ''

        self.moving_tolerance = ''
        self.moving_lower_temp = ''
        self.moving_upper_temp = ''
        self.moving_lower_wave = ''
        self.moving_upper_wave = ''
        self.moving_width = ''

        self.multi_fixed_tolerance = ''
        self.multi_fixed_lower_temp = ''
        self.multi_fixed_upper_temp = ''
        self.multi_fixed_lower_waves = ''
        self.multi_fixed_upper_waves = ''

# Mutiple moving window method not currently implemented.
#
#        self.multi_moving_tolerance = ''
#        self.multi_moving_lower_temp = ''
#        self.multi_moving_upper_temp = ''
#        self.multi_moving_lower_wave = ''
#        self.multi_moving_upper_wave = ''
#        self.multi_moving_widths = ''

        self.known_temp = ''

        self.parse_config()

        self.measurement = None
        self.tes_method = None
        self.emissivity = None

    def parse_config(self):
        """Parse the xml config file.
        """

        tree = et.parse(self.config_file)

        for method in tree.iterfind('method'):
            # parse values for fixed window method
            if (method.attrib['name'] == 'fixed_window'):
                self.fixed_tolerance = method.find(
                    'variation_tolerance').text

                self.fixed_lower_temp = method.find(
                    'temperature_limits/lower').text
                self.fixed_upper_temp = method.find(
                    'temperature_limits/upper').text

                self.fixed_lower_wave = method.find(
                    'wavelength_window/lower').text
                self.fixed_upper_wave = method.find(
                    'wavelength_window/upper').text

            # parse values for moving window method
            elif (method.attrib['name'] == 'moving_window'):
                self.moving_tolerance = method.find(
                    'variation_tolerance').text

                self.moving_lower_temp = method.find(
                    'temperature_limits/lower').text
                self.moving_upper_temp = method.find(
                    'temperature_limits/upper').text

                self.moving_lower_wave = method.find(
                    'wavelength_limits/lower').text
                self.moving_upper_wave = method.find(
                    'wavelength_limits/upper').text

                self.moving_width = method.find(
                    'window_width').text

            # parse values for multiple fixed window method
            elif (method.attrib['name'] == 'multiple_fixed_window'):
                self.multi_fixed_tolerance = method.find(
                    'variation_tolerance').text

                self.multi_fixed_lower_temp = method.find(
                    'temperature_limits/lower').text
                self.multi_fixed_upper_temp = method.find(
                    'temperature_limits/upper').text

                self.multi_fixed_lower_waves = method.find(
                        'wavelength_windows/lower').text
                self.multi_fixed_upper_waves = method.find(
                        'wavelength_windows/upper').text

# Mutiple moving window method not currently implemented.
#
#            # parse values for multiple moving window method
#            elif (method.attrib['name'] == 'multiple_moving_window'):
#                self.multi_moving_tolerance = method.find(
#                    'variation_tolerance').text
#
#                self.multi_moving_lower_temp = method.find(
#                    'temperature_limits/lower').text
#                self.multi_moving_upper_temp = method.find(
#                    'temperature_limits/upper').text
#
#                self.multi_moving_lower_wave = method.find(
#                    'wavelength_limits/lower').text
#                self.multi_moving_upper_wave = method.find(
#                    'wavelength_limits/upper').text
#
#                self.multi_moving_widths = method.find(
#                        'window_widths').text

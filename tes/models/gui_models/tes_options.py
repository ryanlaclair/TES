"""
File:       tes_options.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import xml.etree.ElementTree as et

class TesOptions(object):
    """A class that represents the user changable options for the different
    types of temperature emissivity separation.

    Attributes:
        Descriptive attribute names corresponding to the necessary options
        to initialize TES objects of the given type.
    """

    def __init__(self):
        """Instance constructor.  Initialize all attributes and call method
        to parse the config file.
        """

        self.config_file = 'tes/tes_config.xml'

        self.water_band_tolerance = 0
        self.water_band_lower_temp = 0
        self.water_band_upper_temp = 0

        self.fixed_tolerance = 0
        self.fixed_lower_temp = 0
        self.fixed_upper_temp = 0
        self.fixed_lower_wave = 0
        self.fixed_upper_wave = 0

        self.moving_tolerance = 0
        self.moving_lower_temp = 0
        self.moving_upper_temp = 0
        self.moving_lower_wave = 0
        self.moving_upper_wave = 0
        self.moving_width = 0

        self.multi_fixed_tolerance = 0
        self.multi_fixed_lower_temp = 0
        self.multi_fixed_upper_temp = 0
        self.multi_fixed_lower_waves = None
        self.multi_fixed_upper_waves = None

        self.multi_moving_tolerance = 0
        self.multi_moving_lower_temp = 0
        self.multi_moving_upper_temp = 0
        self.multi_moving_lower_wave = 0
        self.multi_moving_upper_wave = 0
        self.multi_moving_widths = None

        self.parse_config()

    def parse_config(self):
        """Parse the xml config file.
        """

        tree = et.parse(self.config_file)

        for method in tree.iterfind('method'):
            # parse values for waterband method
            if (method.attrib['name'] == 'water_band'):
                self.water_band_tolerance = float(method.find(
                    'variation_tolerance').text)

                self.water_band_lower_temp = float(method.find(
                    'temperature_limits/lower').text)
                self.water_band_upper_temp = float(method.find(
                    'temperature_limits/upper').text)

            # parse values for fixed window method
            elif (method.attrib['name'] == 'fixed_window'):
                self.fixed_tolerance = float(method.find(
                    'variation_tolerance').text)

                self.fixed_lower_temp = float(method.find(
                    'temperature_limits/lower').text)
                self.fixed_upper_temp = float(method.find(
                    'temperature_limits/upper').text)

                self.fixed_lower_wave = float(method.find(
                    'wavelength_window/lower').text)
                self.fixed_upper_wave = float(method.find(
                    'wavelength_window/upper').text)

            # parse values for moving window method
            elif (method.attrib['name'] == 'moving_window'):
                self.moving_tolerance = float(method.find(
                    'variation_tolerance').text)

                self.moving_lower_temp = float(method.find(
                    'temperature_limits/lower').text)
                self.moving_upper_temp = float(method.find(
                    'temperature_limits/upper').text)

                self.moving_lower_wave = float(method.find(
                    'wavelength_limits/lower').text)
                self.moving_upper_wave = float(method.find(
                    'wavelength_limits/upper').text)

                self.moving_window_width = float(method.find(
                    'window_width').text)

            # parse values for multiple fixed window method
            elif (method.attrib['name'] == 'multiple_fixed_window'):
                self.multi_fixed_tolerance = float(method.find(
                    'variation_tolerance').text)

                self.multi_fixed_lower_temp = float(method.find(
                    'temperature_limits/lower').text)
                self.multi_fixed_upper_temp = float(method.find(
                    'temperature_limits/upper').text)

                lower_waves = method.find('wavelength_windows/lower').text.split(',')
                upper_waves = method.find('wavelength_windows/upper').text.split(',')

                self.multi_fixed_lower_waves = [float(wave) 
                    for wave in lower_waves]
                self.multi_fixed_upper_waves = [float(wave) 
                    for wave in upper_waves]

            # parse values for multiple moving window method
            elif (method.attrib['name'] == 'multiple_moving_window'):
                self.multi_moving_tolerance = float(method.find(
                    'variation_tolerance').text)

                self.multi_moving_lower_temp = float(method.find(
                    'temperature_limits/lower').text)
                self.multi_moving_upper_temp = float(method.find(
                    'temperature_limits/upper').text)

                self.multi_moving_lower_wave = float(method.find(
                    'wavelength_limits/lower').text)
                self.multi_moving_upper_wave = float(method.find(
                    'wavelength_limits/upper').text)

                window_widths = method.find('window_widths').text.split(',')

                self.multi_moving_widths = [float(width)
                    for width in window_widths]

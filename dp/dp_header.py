"""
File:       dp_header.py

Author:     Ryan LaClair <rgl8828@rit.edu>

Adapted from code written by Carl Salvaggion <salvaggio@cis.rit.edu>.
"""

import struct

class DpHeader(object):
    """A class that holds the header information for a file output by a D&P
    Instruments Model 103F MicroFT or Model 202 TurboFT.

    Attributes:
        Instance variables to hold each piece of header information.
    """

    def __init__(self):
        """DpHeader instance constructor.
        """

        self.label = ''
        self.version = 0
        self.revision = 0
        self.date = ''
        self.file_format = 0
        self.file_type = ''
        self.original_file_name = ''
        self.reference_file_name = ''
        self.related_file_name_a = ''
        self.related_file_name_b = ''
        self.related_file_name_c = ''
        self.related_file_name_d = ''
        self.annotate = ''
        self.instrument_model = ''
        self.instrument_serial_number = ''
        self.software_version_number = ''
        self.crystal_material = ''
        self.laser_wavelength_microns = 0
        self.laser_null_doubling = 0
        self.optical_ratio = 0
        self.padding = 0
        self.dispersion_constant_xc = 0
        self.dispersion_constant_xm = 0
        self.dispersion_constant_xb = 0
        self.num_chan = 0
        self.interferogram_size = 0
        self.interferogram_center = []
        self.scan_direction = 0
        self.acquire_mode = 0
        self.emissivity = 0
        self.apodization = 0
        self.zero_fill = 0
        self.run_time_math = 0
        self.fft_size = 0
        self.number_of_coadds = 0
        self.number_of_igrams = 0
        self.single_sided = 0
        self.chan_display = 0
        self.amb_temperature = 0
        self.inst_temperature = 0
        self.wbb_temperature = 0
        self.cbb_temperature = 0
        self.temperature_dwr = 0
        self.emissivity_dwr = 0
        self.laser_temperature = 0
        self.spare_i = []
        self.spare_f = []
        self.spare_l = []
        self.spare_na = ''
        self.spare_nb = ''
        self.spare_nc = ''
        self.spare_nd = ''
        self.spare_ne = ''
        self.header_end = ''

    def read_header(self, raw, model):
        """Read the header.

        Args:
            raw - The raw header data.
            model - The D&P Instrument model.
        """
        
        if (model=='202'):
            self._read_new_header(raw)

        elif (model=='102old'):
            self._read_old_header(raw)

        else:
            self._read_new_header(raw)

    def _read_new_header(self, raw):
        """Private helper method to read a header output in the "new"
        format.

        Args:
            raw - The raw header data.
        """

        byte_count = 0

        data_size = 4
        self.label = struct.unpack('<4s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.version = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.revision = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 28
        self.date = struct.unpack('<28s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.file_format = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.file_type = struct.unpack('<4s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.original_file_name = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.reference_file_name = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.related_file_name_a = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.related_file_name_b = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.related_file_name_c = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 84
        self.annotate = struct.unpack('<84s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 36
        self.instrument_model = struct.unpack('<36s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 36
        self.instrument_serial_number = struct.unpack('<36s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 36
        self.software_version_number = struct.unpack('<36s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 36
        self.crystal_material = struct.unpack('<36s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.laser_wavelength_microns = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.laser_null_doubling = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.padding = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.dispersion_constant_xc = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.dispersion_constant_xm = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.dispersion_constant_xb = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.num_chan = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.interferogram_size = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.scan_direction = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.acquire_mode = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.emissivity = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.apodization = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.zero_fill = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.run_time_math = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.fft_size = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.number_of_coadds = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.single_sided = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.chan_display = struct.unpack('<l',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.amb_temperature = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.inst_temperature = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.wbb_temperature = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.cbb_temperature = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.temperature_dwr = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.emissivity_dwr = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 8
        self.laser_temperature = struct.unpack('<d',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 40
        self.spare_i = struct.unpack('<llllllllll',
                raw[byte_count:byte_count+data_size])
        byte_count += data_size

        data_size = 80
        self.spare_f = struct.unpack('<dddddddddd',
                raw[byte_count:byte_count+data_size])
        byte_count += data_size

        data_size = 68
        self.spare_na = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.spare_nb = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.spare_nc = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.spare_nd = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 68
        self.spare_ne = struct.unpack('<68s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.header_end = struct.unpack('<4s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

    def _read_old_header(self, raw):
        """Private helper function to read a header output in the "old"
        format.

        Args:
            raw - The raw header data.
        """

        byte_count = 0

        data_size = 4
        self.label = struct.unpack('<4s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.version = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.revision = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 26
        self.date = struct.unpack('<26s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.file_format = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.file_type = struct.unpack('<4s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.original_file_name = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.reference_file_name = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.related_file_name_a = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.related_file_name_b = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.related_file_name_c = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.related_file_name_d = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 82
        self.annotate = struct.unpack('<82s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 33
        self.instrument_model = struct.unpack('<33s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 33
        self.instrument_serial_number = struct.unpack('<33s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 33
        self.software_version_number = struct.unpack('<33s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 33
        self.crystal_material = struct.unpack('<33s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.laser_wavelength_microns = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.laser_null_doubling = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.optical_ratio = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.dispersion_constant_xc = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.dispersion_constant_xm = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.dispersion_constant_xb = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.interferogram_size = struct.unpack('<H',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.interferogram_center.append(struct.unpack('<H',
                raw[byte_count:byte_count+data_size])[0])
        byte_count += data_size

        data_size = 2
        self.interferogram_center.append(struct.unpack('<H',
                raw[byte_count:byte_count+data_size])[0])
        byte_count += data_size

        data_size = 2
        self.acquire_mode = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.emissivity = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.apodization = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.zero_fill = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.run_time_math = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.fft_size = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.number_of_coadds = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 2
        self.number_of_igrams = struct.unpack('<h',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.amb_temperature = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.inst_temperature = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.wbb_temperature = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.cbb_temperature = struct.unpack('<f',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 20
        self.spare_i = struct.unpack('<hhhhhhhhhh',
                raw[byte_count:byte_count+data_size])
        byte_count += data_size

        data_size = 40
        self.spare_f = struct.unpack('<ffffffffff',
                raw[byte_count:byte_count+data_size])
        byte_count += data_size

        data_size = 40
        self.spare_l = struct.unpack('<ffffffffff',
                raw[byte_count:byte_count+data_size])
        byte_count += data_size

        data_size = 65
        self.spare_na = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.spare_nb = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.spare_nc = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.spare_nd = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 65
        self.spare_ne = struct.unpack('<65s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

        data_size = 4
        self.header_end = struct.unpack('<4s',
                raw[byte_count:byte_count+data_size])[0]
        byte_count += data_size

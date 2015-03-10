"""
File:       tes_batch_process.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import os

import tes

def process_root_directory(root, method, config):
    """
    """

    output_file = method + '_batch_process'

    with open(output_file, 'a') as out_file:
        out_file.write('Sample\t\t\t\tTemperature\n')

        for _, measurement_dirs, _ in os.walk(root):
            for measurement_dir in measurement_dirs:
                process_measurement_directory(root+measurement_dir, method, config,
                        out_file)

def process_measurement_directory(measurement_dir, method, config, out_file):
    """
    """

    for _, _, files in os.walk(measurement_dir):

        if '.DS_Store' in files:
            files.remove('.DS_Store')

        # sort by file extension
        files.sort(key=lambda f: f[-3:])

        cbb_file = measurement_dir + '/' + files[0]
        wbb_file = measurement_dir + '/' + files[3]
        sam_file = measurement_dir + '/' + files[2]
        dwr_file = measurement_dir + '/' + files[1]

        measurement = tes.DpMeasurement(cbb_file, wbb_file, sam_file, dwr_file)

        if method == 'water-band':
            tes_method = tes.WaterBand(config.water_band_lower_temp, 
                    config.water_band_upper_temp)
        elif method == 'fixed':
            tes_method = tes.FixedWindow(config.fixed_lower_temp, 
                    config.fixed_upper_temp, config.fixed_lower_wave, 
                    config.fixed_upper_wave)
        elif method == 'moving':
            tes_method = tes.MovingWindow(config.moving_lower_temp, 
                    config.moving_upper_temp, config.moving_lower_wave, 
                    config.moving_upper_wave, config.moving_window_width)
        elif method == 'multi-fixed':
            tes_method = tes.MultipleFixedWindow(config.multi_fixed_lower_temp, 
                    config.multi_fixed_upper_temp, config.multi_fixed_lower_waves, 
                    config.multi_fixed_upper_waves)
        elif method == 'multi-moving':
            tes_method = tes.MultipleMovingWindow(config.multi_moving_lower_temp, 
                    config.multi_moving_upper_temp, config.multi_moving_lower_wave, 
                    config.multi_moving_upper_wave, 
                    config.multi_moving_window_widths)

        emissivity = tes_method.find_temperature(measurement)

        out = files[2] + '\t\t' + str(emissivity.temperature) + '\n'
        out_file.write(out)

def main():
    """
    """

    path = raw_input('Path within current working directory: ')

    method = raw_input('TES type (water-band, fixed, moving, multi-fixed, multi-moving): ')

    if method == 'multi-moving':
        print 'WARNING: This will take a LONG time..'

    root = str(os.getcwd()) + '/' + path + '/'

    config = tes.TesOptionsModel()

    process_root_directory(root, method, config)

if __name__ == '__main__':
    main()

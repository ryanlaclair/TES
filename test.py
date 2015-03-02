"""Test script for temperature emissivity code.
"""

import tes
import time

cbb = 'data/2013_06_04_1435/2013_06_04_1431.cbb'
wbb = 'data/2013_06_04_1435/2013_06_04_1433.wbb'
sam = 'data/2013_06_04_1435/2013_06_04_1435.sam'
dwr = 'data/2013_06_04_1435/2013_06_04_1436.dwr'

data = tes.DpMeasurement(cbb, wbb, sam, dwr)

#start = time.time()
#tes_fixed = tes.FixedWindow(260, 360, 8.12, 8.6)
#emissivity_fixed = tes_fixed.find_temperature(data)
#print ''
#print 'standard: ', emissivity_fixed.temperature
#print 'assd: ', emissivity_fixed.assd
#print 'indices: ', emissivity_fixed.window_indices
#print 'time: ', time.time() - start

#start = time.time()
#tes_moving = tes.MovingWindow(260, 360, 8, 14, 0.48)
#emissivity_moving = tes_moving.find_temperature(data)
#print ''
#print 'moving: ', emissivity_moving.temperature
#print 'assd: ', emissivity_moving.assd
#print 'indices: ', emissivity_moving.window_indices
#print 'time: ', time.time() - start

#start = time.time()
#tes_multi_fixed = tes.MultipleFixedWindow(260, 360, [8.0, 9.6], [8.4, 9.9])
#emissivity_multi_fixed = tes_multi_fixed.find_temperature(data)
#print ''
#print 'variable: ', emissivity_multi_fixed.temperature
#print 'assd: ', emissivity_multi_fixed.assd
#print 'indices: ', emissivity_multi_fixed.window_indices
#print 'time: ', time.time() - start

start = time.time()
tes_multi_moving = tes.MultipleMovingWindow(260, 360, 8, 14, [0.5, 0.5])
emissivity_multi_moving = tes_multi_moving.find_temperature(data)
print ''
print 'multiple: ', emissivity_multi_moving.temperature
print 'assd: ', emissivity_multi_moving.assd
print 'indices: ', emissivity_multi_moving.window_indices
print 'time: ', time.time() - start

#start = time.time()
#tes_waterband = tes.WaterBand(260, 360, 13.55, 13.85)
#emissivity_waterband = tes_waterband.find_temperature(data)
#print ''
#print 'waterband: ', emissivity_waterband.temperature
#print 'time: ', time.time() - start

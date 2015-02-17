"""Test script for temperature emissivity code.
"""

import tes
import time

cbb = '../data/Stephanie/2013_06_04_1435/2013_06_04_1431.cbb'
wbb = '../data/Stephanie/2013_06_04_1435/2013_06_04_1433.wbb'
sam = '../data/Stephanie/2013_06_04_1435/2013_06_04_1435.sam'
dwr = '../data/Stephanie/2013_06_04_1435/2013_06_04_1436.dwr'

data = tes.DpMeasurement(cbb, wbb, sam, dwr)

#start = time.time()
#tes_standard = tes.Standard(260, 360, 8.12, 8.6)
#emissivity_standard = tes_standard.find_temperature(data)
#print ''
#print 'standard: ', emissivity_standard.temperature
#print 'assd: ', emissivity_standard.assd
#print 'time: ', time.time() - start
#
#start = time.time()
#tes_moving = tes.MovingWindow(260, 360, 8, 14, 0.5)
#emissivity_moving = tes_moving.find_temperature(data)
#print ''
#print 'moving: ', emissivity_moving.temperature
#print 'assd: ', emissivity_moving.assd
#print 'time: ', time.time() - start
#
#start = time.time()
#tes_variable = tes.VariableMovingWindow(260, 360, 8, 14, 0.5, 1, 5)
#emissivity_variable = tes_variable.find_temperature(data)
#print ''
#print 'variable: ', emissivity_variable.temperature
#print 'assd: ', emissivity_variable.assd
#print 'time: ', time.time() - start
#
#start = time.time()
#tes_multiple = tes.MultipleMovingWindow(260, 360, 8, 14, 0.5, 1, 5, 2)
#emissivity_multiple = tes_multiple.find_temperature(data)
#print ''
#print 'multiple: ', emissivity_multiple.temperature
#print 'assd: ', emissivity_multiple.assd
#print 'time: ', time.time() - start

start = time.time()
tes_waterband = tes.WaterBand(260, 360, 13.55, 13.85)
emissivity_waterband = tes_waterband.find_temperature(data)
print ''
print 'waterband: ', emissivity_waterband.temperature
print 'time: ', time.time() - start

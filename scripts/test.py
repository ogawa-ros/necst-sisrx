#!/usr/bin/env python3

name = 'test'

import sys
import rospy
import time
import numpy
import std_msgs.msg
import argparse

import os, sys
import matplotlib.pyplot as plt
import std_msgs.msg
import pandas

import necstdb

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)
sis = controller.sis()
att1 = tz2019_controller.loatt_h()
att2 = tz2019_controller.loatt_v()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search Lo Att level when paramater search and measure SIS I-V curve')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name1 = '/home/exito/data/logger/test/%s/level=20.db'%(args.save_name)
print(file_name1)
logger.start(file_name1)

att1.set_cur(20)
time.sleep(60)
att2.set_cur(20)
print("att_level = 20")
sis_vgap = numpy.arange(0, 1.2, 0.001)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.05)
    continue
logger.stop()


db = necstdb.necstdb()
db.open(file_name1)

d = db.read_as_pandas()
d['time'] = pandas.to_datetime(d['time'], unit='s')
d['data'] = [_[0][data] for _ in d['msgs']]
d2 = d.set_index(['topic', 'time']).sort_index()

dd = pandas.concat(
    [
        d2.loc['/tz2019/sis_v1/v'][['data']].rename(columns={'data': 'V1V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_v1/i'][['data']].rename(columns={'data': 'V1I'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h1/v'][['data']].rename(columns={'data': 'H1V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h1/i'][['data']].rename(columns={'data': 'H1I'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_v2/v'][['data']].rename(columns={'data': 'V2V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_v2/i'][['data']].rename(columns={'data': 'V2I'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h2/v'][['data']].rename(columns={'data': 'H2V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h2/i'][['data']].rename(columns={'data': 'H2I'}).astype(float).resample('0.1S').mean(),
    ],
    axis = 1,
)

#under the i-v graph plot

fig = matplotlib.pyplot.figure(figsize=(7, 6))
ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
ax[0].plot(dd['V1V'], dd['V1I'], '.')
ax[1].plot(dd['H1V'], dd['H1I'], '.')
ax[2].plot(dd['V2V'], dd['V2I'], '.')
ax[3].plot(dd['H2V'], dd['H2I'], '.')
ax[0].set_title('V1 I-V')
ax[1].set_title('H1 I-V')
ax[2].set_title('H2 I-V')
ax[3].set_title('V2 I-V')
[_.set_xlabel('Voltage (mV)') for _ in ax]
[_.set_ylabel('Current (uA)') for _ in ax]
[_.grid(True, linestyle=':') for _ in ax]

plt.savefig(args.save_name)
plt.show()

#file_name2 = '/home/exito/data/logger/test/%s/level=20.db'%(args.save_name)
#print(file_name2)
#logger.start(file_name2)

#att1.set_cur(20)
#time.sleep(60)
#att2.set_cur(20)
#print("att_level = 20")
#sis_vgap = numpy.arange(0, 1.2, 0.001)
#for vgap in sis_vgap:
#    sis.set_vgap(vgap)
#    time.sleep(0.05)
#    continue
#logger.stop()

#file_name3 = '/home/exito/data/logger/test/%s/level=30.db'%(args.save_name)
#print(file_name3)
#logger.start(file_name3)

#att1.set_cur(30)
#time.sleep(60)
#att2.set_cur(30)
#print("att_level = 30")
#sis_vgap = numpy.arange(0, 1.2, 0.001)
#for vgap in sis_vgap:
#    sis.set_vgap(vgap)
#    time.sleep(0.05)
#    continue

#sis.set_vgap(0)
#logger.stop()

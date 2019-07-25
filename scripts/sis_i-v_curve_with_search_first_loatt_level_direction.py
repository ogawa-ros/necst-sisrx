#!/usr/bin/env python3

name = 'sis_i_v_curve_with_seurch_first_loatt_level_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
loatt1 = tz2019_controller.loatt_h()
loatt2 = tz2019_controller.loatt_v()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search Lo Att level when paramater search and measure SIS I-V curve')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()


att = numpy.arange(20, 31, 5)
att = att[::-1]          #search Lo Att level when Parameter Search

for att_vol in att:
    file_name = '/home/exito/data/logger/test/%s/att_level=%d.db'%(args.save_name, att_vol)
    print(file_name)
    logger.start(file_name)             #measure I-V curve
    loatt1.set_cur(att_vol)
    time.sleep(60)
    loatt2.set_cur(att_vol)
    sis_vgap = numpy.arange(0, 1.2, 0.001)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.05)
        continue
    #time.sleep(60)
    logger.stop()


    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
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

    fig = plt.figure(figsize=(7, 6))
    ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
    ax = set_title('att_level = %d'%(att_vol))
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

    #plt.savefig(args.save_name)
    plt.show()
    continue

sis.set_vgap(0)
loatt1.set_cur(30)
time.sleep(60)
loatt2.set_cur(30)

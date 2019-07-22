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

file_name = '/home/exito/data/logger/test/%s'%(args.save_name)
print(file_name)
att = numpy.arange(15, 31)
att = att[::-1]          #search Lo Att level when Parameter Search
logger.start(file_name)
for att_vol in att:               #measure I-V curve
    loatt1.set_cur(att_vol)
    time.sleep(60)
    loatt2.set_cur(att_vol)
    sis_vgap = numpy.arange(0, 1.2, 0.001)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.1)
        continue
    #time.sleep(60)
    continue
sis.set_vgap(0)
loatt1.set_cur(30)
time.sleep(60)
loatt2.set_cur(30)
logger.stop()

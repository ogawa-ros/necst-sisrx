#!/usr/bin/env python3

name = 'sis_i_v_curve_with_seurch_first_loatt_level_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
loatt = controller.loatt()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search Lo Att level when paramater search and measure SIS I-V curve')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/test/%s'%(args.save_name)
print(file_name)
att = numpy.arange(21)          #search Lo Att level when Parameter Search
logger.start(file_name)
for att_vol in att:               #measure I-V curve
    loatt.set_cur(att_vol)
    sis_vgap = numpy.arange(0, 1.2, 0.01)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.1)
        continue
    continue
sis.set_vgap(0)
att.set_cur(20)
logger.stop()

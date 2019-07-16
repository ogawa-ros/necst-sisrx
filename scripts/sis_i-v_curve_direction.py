#!/usr/bin/env python3

name = 'sis_i_v_curve_direction'

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
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'measure SIS I-V curve only')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/test/%s'%(args.save_name)
print(file_name)
logger.start(file_name)
sis_vgap = numpy.arange(0, 1.2, 0.001)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.1)
    continue
sis.set_vgap(0)
logger.stop()

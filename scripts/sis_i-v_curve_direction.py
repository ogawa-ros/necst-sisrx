#!/usr/bin/env python3

name = 'sis_i-v_curve_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse

import sys.path.append("home/exito/ros/src/necst-core/scripts")

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
sis = numpy.arange(0, 1.2, 0.01)
for sis_vgap in sis:
    sis.set_sis_vgap(sis_vgap)
    time.sleep(0.1)
    continue
logger.stop()

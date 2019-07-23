#!/usr/bin/env python3

name = 'test'

import sys
import rospy
import time
import numpy
import std_msgs.msg
import argparse

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

file_name1 = '/home/exito/data/logger/test/%s/level=10.db'%(args.save_name)
print(file_name1)
logger.start(file_name1)

att1.set_cur(10)
time.sleep(60)
att2.set_cur(10)
print("att_level = 10")
sis_vgap = numpy.arange(0, 1.2, 0.001)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.05)
    continue
logger.stop()

file_name2 = '/home/exito/data/logger/test/%s/level=20.db'%(args.save_name)
print(file_name2)
logger.start(file_name2)

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

file_name3 = '/home/exito/data/logger/test/%s/level=30.db'%(args.save_name)
print(file_name3)
logger.start(file_name3)

att1.set_cur(30)
time.sleep(60)
att2.set_cur(30)
print("att_level = 30")
sis_vgap = numpy.arange(0, 1.2, 0.001)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.05)
    continue

sis.set_vgap(0)
logger.stop()

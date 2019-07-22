#!/usr/bin/env python3

name = 'test'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

att1 = tz2019_controller.loatt_h()
att2 = tz2019_controller.loatt_v()

att1.set_cur(10)
time.sleep(60)
att2.set_cur(10)
print("att_level = 10")
    sis_vgap = numpy.arange(0, 1.2, 0.001)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.05)
        continue

att1.set_cur(20)
time.sleep(60)
att2.set_cur(20)
print("att_level = 20")
    sis_vgap = numpy.arange(0, 1.2, 0.001)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.05)
        continue


att1.set_cur(30)
time.sleep(60)
att2.set_cur(30)
print("att_level = 30")
    sis_vgap = numpy.arange(0, 1.2, 0.001)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.05)
        continue

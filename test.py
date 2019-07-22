#!/usr/bin/env python3

name = 'test'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import tz2019_controller

rospy.init_node(name)

att1 = tz2019_controller.loatt_h()
att2 = tz2019_controller.loatt_v()

att1.set_cur(10)
time.sleep(60)
att2.set_cur(10)

time.sleep(60)

att1.set_cur(20)
time.sleep(60)
att2.set_cur(20)

time.sleep(60)

att1.set_cur(30)
time.sleep(60)
att2.set_cur(30)

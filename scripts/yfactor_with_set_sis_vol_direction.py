#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import time
import std_msgs.msg
import numpy as np
import argparse

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
loatt = controller.loatt()
logger = core_controller.logger()
switch = tz2019_controller.switch()

volp1 = np.linespace(-1, 0, 5)   #have to repeat until determining optimal voltage value
volp2 = np.linespace(-1, 0, 5)
switch.set_if_switch(switch_value)
logger.start(yfactor)
for vp1 in volp1:
    sis.set_sis_vp(vp1)
    for vp2 in volp2:
        sis.set_sis_vp(vp2)
        time.sleep(0.1)
input("Are you ready for cold measure: ")
for vp1 in volp1:
    sis.set_sis_vp(vp1)
    for vp2 in volp2:
        sis.set_sis_vp(vp2)
logger.stop()

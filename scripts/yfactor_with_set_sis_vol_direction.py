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

parser = argparse.ArgumentParser(description = 'search optical sis voltage value')

parser.add_argument('switch_value', choices = ['hu', 'hl', 'vu', 'vl'], type = float, help = 'choice IF output port')

args = parser.parse_args()

volp1 = np.linespace(-1, 0, 5)   #search optimal voltage value
volp2 = np.linespace(-1, 0, 5)
switch.set_if_switch(switch_value)
logger.start(yfactor)
for vp1 in volp1:
    sis.set_sis_vp(vp1)
    for vp2 in volp2:
        sis.set_sis_vp(vp2)
        time.sleep(0.1)
        continue
    continue
time.sleep(10)
for vp1 in volp1:
    sis.set_sis_vp(vp1)
    for vp2 in volp2:
        sis.set_sis_vp(vp2)
        time.sleep(0.1)
        continue
    continue
logger.stop()

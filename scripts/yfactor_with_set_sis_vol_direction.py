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
parser.add_argument('att', type = float, help = 'set optical Lo Att voltage value')
parser.add_argument('save_name', type = string, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s'%(args.save_name)
volp1 = np.linespace(-1, 0, 5)   #search optimal SIS voltage value
volp2 = np.linespace(-1, 0, 5)
switch.set_if_switch(args.switch_value)
loatt.set_loatt_vol(args.att)
logger.start(file_name)
for vp1 in volp1:             #measure hot
    sis.set_sis_vp(vp1)
    for vp2 in volp2:
        sis.set_sis_vp(vp2)
        time.sleep(0.1)
        continue
    continue
time.sleep(10)
for vp1 in volp1:             #measure cold
    sis.set_sis_vp(vp1)
    for vp2 in volp2:
        sis.set_sis_vp(vp2)
        time.sleep(0.1)
        continue
    continue
logger.stop()

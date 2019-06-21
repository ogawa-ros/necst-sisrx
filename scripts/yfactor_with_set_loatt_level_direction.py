#!/usr/bin/env python3

name = 'set_loatt_level_direction'

import rospy
import time
import std_msgs.msg
import numpy
import argparse

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
irrsg = controller.irrsg()
loatt = controller.loatt()
logger = core_controller.logger()
switch = tz2019_controller.switch()

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('switch_value', choices = ['hu', 'hl', 'vu', 'vl'], type = float, help = 'choice IF output port')

args = parser.parse_args()

att_vol = np.arange(21)    #have to repeat until determining optimal att voltage value
switch.set_if_switch(switch_value)
logger.start(yfactor)
for att_v in att_vol:
    loatt.set_loatt_vol(vp1)
    time.sleep(0.1)
for att_v in att_vol:
    loatt.set_loatt_vol(vp1)
    time.sleep(0.1)
logger.stop()

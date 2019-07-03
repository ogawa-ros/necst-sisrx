#!/usr/bin/env python3

name = 'measure_yfactor_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
loatt = controller.loatt()
logger = core_controller.logger()
switch = tz2019_controller.switch()

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

#parser.add_argument('switch_value', choices = ['hu', 'hl', 'vu', 'vl'], type = float, help = 'choice IF output port')
parser.add_argument('sis_vp', type = float, help = 'set optical SIS voltage value')
parser.add_argument('loatt_level', type = float, help = 'set optical Lo Att voltage value')
parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s'%(args.save_name)
#switch.set_if_switch(args.switch_value)
sis.set_sis_vp(args.sis_vp)
loatt.set_loatt_vol(args.loatt_level)
logger.start(file_name)
time.sleep()
logger.stop()

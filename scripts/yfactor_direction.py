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

parser = argparse.ArgumentParser(description = 'measure Y-factor only')

#parser.add_argument('switch_value', choices = ['hu', 'hl', 'vu', 'vl'], type = float, help = 'choice IF output port')
parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s'%(args.save_name)
#switch.set_if_switch(args.switch_value)
logger.start(file_name)
time.sleep(10)
logger.stop()

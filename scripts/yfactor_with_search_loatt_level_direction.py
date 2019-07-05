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

#parser.add_argument('switch_value', choices = ['hu', 'hl', 'vu', 'vl'], type = float, help = 'choice IF output port')
parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s'%(args.save_name)
att_vol = np.arange(21)    #search optimal Lo Att level
#switch.set_if_switch(args.switch_value)
logger.start(file_name)
for att_v in att_vol:           #measure y-factor
    loatt.set_loatt(att_v)
    time.sleep(0.1)
    continue
logger.stop()

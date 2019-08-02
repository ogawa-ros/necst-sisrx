#!/usr/bin/env python3

name = 'measure_yfactior_search_loatt_level_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

irrsg = controller.irr()
loatt1 = tz2019_controller.loatt_h()
loatt2 = tz2019_controller.loatt_v()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/test/%s.db'%(args.save_name)
att_vol = numpy.arange(21)    #search optimal Lo Att level
logger.start(file_name)
for att_v in att_vol:           #measure y-factor
    loatt1.set_cur(att_v)
    time.sleep(60)
    loatt2.set_cur(att_v)
    time.sleep(60)
    continue
loatt1.set_cur(30)
time.sleep(60)
loatt2.set_cur(30)
logger.stop()

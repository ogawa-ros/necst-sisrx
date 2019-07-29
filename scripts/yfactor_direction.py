#!/usr/bin/env python3

name = 'measure_yfactor_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller

sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")
import plot_tool

rospy.init_node(name)

logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'measure Y-factor only')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s.db'%(args.save_name)
logger.start(file_name)
time.sleep(30)
logger.stop()

plot_tool.yfactor_prot(file_name, args.save_name)

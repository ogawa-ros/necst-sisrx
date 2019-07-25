#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import time
import std_msgs.msg
import argparse
import controller
import time
import sys

sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller

sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")
import plot_tool

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'set SIS voltage V1 and V2')

parser.add_argument('v1', type = float, help = 'set SIS voltage of V1')
parser.add_argument('h1', type = float, help = 'set SIS voltage of V2')
parser.add_argument('h2', type = float, help = 'set SIS voltage of V1')
parser.add_argument('v2', type = float, help = 'set SIS voltage of V2')
parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

sis.set_v1(args.v1)
sis.set_h1(args.h1)
sis.set_h2(args.h2)
sis.set_v2(args.v2)

file_name = '/home/exito/data/logger/test/%sset_vol_data.db'%(args.save_name, att_vol)
print(file_name)
logger.start(file_name)
time.sleep(10)
logger.stop()
plot_tool.iv_plot(file_name, args.save_name)

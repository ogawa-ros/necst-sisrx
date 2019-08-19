#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import time
import sys
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import tz2019_controller

sys.path.append("/home/exito/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

logger = core_controller.logger()

sis = tz2019_controller.sis()

parser = argparse.ArgumentParser(description = 'set SIS voltage V1 and V2')

parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('v1', type = float, help = 'set SIS voltage of V1')
parser.add_argument('h1', type = float, help = 'set SIS voltage of V2')
parser.add_argument('h2', type = float, help = 'set SIS voltage of V1')
parser.add_argument('v2', type = float, help = 'set SIS voltage of V2')

args = parser.parse_args()

sis.set_v1_v(args.v1)
sis.set_h1_v(args.h1)
sis.set_h2_v(args.h2)
sis.set_v2_v(args.v2)

file_name = '/home/exito/data/logger/test/%s_iv.db'%(args.save_name)
logger.start(file_name)
time.sleep(10)
logger.stop()
#plot_tool.iv_plot(file_name, args.save_name)

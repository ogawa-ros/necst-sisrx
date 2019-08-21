#!/usr/bin/env python3

name = 'sis_iv_curve_direction'

import sys
import datetime
import rospy
import time
import std_msgs.msg
import numpy
import argparse

sys.path.append("/home/hinotoritz/ros/src/necst-core/scripts")
import controller
import core_controller

#sys.path.append("/home/hinotoritz/ros/src/necst-tz2019/scripts")
#import plot_tool


rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

#parser = argparse.ArgumentParser(description = 'measure SIS I-V curve only')
#parser.add_argument('save_name', type = str, help = 'set saving file name')
#args = parser.parse_args()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)
logger.start(file_name)
sis_vgap = numpy.arange(0, 1.2, 0.001)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.1)
    continue

logger.stop()
time.sleep(3)
sis.set_vgap(0)


#plot_tool.iv_plot(file_name, args.save_name)

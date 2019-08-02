#!/usr/bin/env python3

name = 'measure_yfactor_search_sis_vol_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical sis voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

volp1 = np.linespace(-1, 0, 5)   #search optimal SIS voltage value
volp2 = np.linespace(-1, 0, 5)
for vp1 in volp1:             #measure y-factor
    sis.set_vp1(vp1)
    for vp2 in volp2:
        file_name = '/home/exito/data/logger/test/%s-%s-%s.db'%(args.save_name, str(vp1), str(vp2))
        logger.start(file_name)
        sis.set_vp2(vp2)
        time.sleep(1)
        logger.stop()
        continue
    continue
sis.set_vgap(0)

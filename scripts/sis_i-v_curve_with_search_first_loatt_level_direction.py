#!/usr/bin/env python3

name = 'sis_i_v_curve_with_seurch_first_loatt_level_direction'

import os, sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse
import necstdb
import pandas
import matplotlib.pyplot as plt

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")
import plot_tool

rospy.init_node(name)

sis = controller.sis()
loatt1 = tz2019_controller.loatt_h()
loatt2 = tz2019_controller.loatt_v()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search Lo Att level when paramater search and measure SIS I-V curve')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()


att = numpy.arange(20, 31, 5)
att = att[::-1]          #search Lo Att level when Parameter Search

for att_vol in att:
    file_name = '/home/exito/data/logger/test/%s/att_level=%d_data.db'%(args.save_name, att_vol)
    print(file_name)
    logger.start(file_name)             #measure I-V curve
    loatt1.set_cur(att_vol)
    time.sleep(60)
    loatt2.set_cur(att_vol)
    sis_vgap = numpy.arange(0, 1.2, 0.001)
    for vgap in sis_vgap:
        sis.set_vgap(vgap)
        time.sleep(0.1)
        continue
    #time.sleep(60)
    logger.stop()
    sis.set_vgap(0)
    plot_tool.att_iv_plot(file_name, args.save_name, att_vol)

    continue

sis.set_vgap(0)
loatt1.set_cur(30)
time.sleep(60)
loatt2.set_cur(30)

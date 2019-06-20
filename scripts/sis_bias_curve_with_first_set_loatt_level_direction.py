#!/usr/bin/env python3

name = 'sis_bias_curve_direction'

import rospy
import time
import std_msgs.msg
import numpy

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
lo = controller.lo1st()
loatt = controller.loatt()
logger = core_controller.logger()

att = numpy.array([0:20])          #search Lo Att value when Parameter Search
logger.start(iv_band)
for att_vol in att:
    loatt.set_loatt_vol(att_vol)
    sis = numpy.array([])               #before ditermine vp with Ueda
    for sis_vol in sis:
        sis.set_sis_vp(sis_vol)
        time.sleep(0.1)
        continue
    continue
logger.stop()

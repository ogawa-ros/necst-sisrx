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

att = numpy.arange(21)          #search Lo Att value when Parameter Search
logger.start(iv)           #tolk with logger team
for att_vol in att:
    loatt.set_loatt_vol(att_vol)
    sis = numpy.arange(1, 85)
    for sis_vgap in sis:
        sis_vgapcount = (sis_vgap)/84
        sis.set_sis_vgap(sis_vgapcount)
        time.sleep(0.1)
        continue
    continue
logger.stop()

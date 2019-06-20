#!/usr/bin/env python3

name = 'sis_bias_curve_direction'

import rospy
import time
import std_msgs.msg

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
lo = controller.lo1st()
loatt = controller.loatt()
logger = core_controller.logger()

freq = input("1st Lo freq: ")       #set Lo SG value
power = input("1st Lo power: ")
lo.set_lo1st_freq(freq)
lo.set_lo1st_power(power)

sis.set_sis_vp()      #before ditermine vp
att = [0:20]
logger.start(iv_band)     #search Lo Att value when Parameter Search
for att_vol in att:
    loatt.set_loatt_vol(att_vol)
    time.sleep(0.1)
logger.stop()

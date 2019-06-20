#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import time
import std_msgs.msg

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
loatt = controller.loatt()
logger = core_controller.logger()
switch = tz2019_controller.switch()

volp = input("SIS vol: ")
sis.set_sis_vp(volp)
bands = {'hu':, 'hl':, 'vu':, 'vl':}
for band in bands:              #x4 repeat hu,hl,vu,vl
    switch_value = band
    switch.set_if_switch(switch_value)
    input("Are you ready for hot measure?: ")
    logger.start(hot_band)
    time.sleep(0.1)
    logger.stop()
    input("Are you ready for cold measure?: ")
    logger.start(cold_band)
    time.sleep(0.1)
    logger.stop()     #have to repeat until determining optimal voltage value

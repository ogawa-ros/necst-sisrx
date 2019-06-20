#!/usr/bin/env python3

name = 'set_lo_sg_direction'

import rospy
import time
import std_msgs.msg

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

lo = controller.lo1st()

freq = input("1st Lo freq: ")       #set Lo SG value
power = input("1st Lo power: ")
lo.set_lo1st_freq(freq)
lo.set_lo1st_power(power)

#!/usr/bin/env python3

name = 'set_lo_sg_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

lo = controller.lo1st()

parser = argparse.ArgumentParser(description = 'set freq and power of Lo SG')

parser.add_argument('freq', type = float, help = 'set freq of Lo SG')
parser.add_argument('power', type = float, help = 'set power of Lo SG')

args = parser.parse_args()

lo.set_lo1st_freq(freq)        #set Lo SG value
lo.set_lo1st_power(power)

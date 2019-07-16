#!/usr/bin/env python3

name = 'set_lo_sg_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

lo = controller.lo1st()

parser = argparse.ArgumentParser(description = 'set freq and power of Lo SG and on/off Lo SG')

parser.add_argument('freq', type = float, help = 'set freq of Lo SG')
parser.add_argument('power', type = float, help = 'set power of Lo SG')
#parser.add_argument('on_off', choices = ['on', 'off'], type = str, help = 'on/off Lo SG')

args = parser.parse_args()

lo.set_freq(args.freq)
lo.set_sg_power(args.power)

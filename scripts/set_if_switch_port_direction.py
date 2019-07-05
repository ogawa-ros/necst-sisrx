#!/usr/bin/env python3

name = 'set_switch_ch_direction'

import rospy
import time
import std_msgs.msg
import argparse

import tz2019_controller

rospy.init_node(name)

switch = tz2019_controller.switch()

parser = argparse.ArgumentParser(description = 'set IF switch ch')

parser.add_argument('switch', type = float, choices = ['hu', 'hl', 'vu', 'vl'], help = 'set IF switch ch')

args = parser.parse_args()

switch.set_ch(args.swith)

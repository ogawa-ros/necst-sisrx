#!/usr/bin/env python3

name = 'set_switch_ch_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import tz2019_controller

rospy.init_node(name)

switch = tz2019_controller.switch()

parser = argparse.ArgumentParser(description = 'set IF switch ch')

parser.add_argument('switch', type = float, choices = ['HU', 'HL', 'VU', 'VL'], help = 'set IF switch ch')

args = parser.parse_args()

switch.set_open_ch(args.switch)
switch.set_close_ch(srgs.switch)

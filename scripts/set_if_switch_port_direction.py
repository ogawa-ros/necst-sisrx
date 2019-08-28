#!/usr/bin/env python3

name = 'set_switch_ch_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse
sys.path.append("/home/hinotoritz/ros/src/necst-tz2019/scripts")
import tz2019_controller

rospy.init_node(name)

switch = tz2019_controller.switch()

#取得したいチャンネルを引数に選択
parser = argparse.ArgumentParser(description = 'set IF switch ch')
parser.add_argument('switch', choices = ['HU', 'HL', 'VU', 'VL'], help = 'set IF switch ch')
args = parser.parse_args()

#
switch.set_open_ch(args.switch)
switch.set_close_ch(args.switch)

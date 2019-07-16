#!/usr/bin/env python3

name = 'set_loatt_level_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

att = controller.loatt()

parser = argparse.ArgumentParser(description = 'set Lo Att. level')

parser.add_argument('att', type = float, help = 'set Lo Att. level')

args = parser.parse_args()

att.set_cur(args.att)

#!/usr/bin/env python3

name = 'set_sis_vol_and_att_level_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

sis = controller.sis()
att = controller.loatt()

parser = argparse.ArgumentParser(description = 'set SIS voltage V1 and V2')

parser.add_argument('v1', type = float, help = 'set SIS voltage of V1')
parser.add_argument('v2', type = float, help = 'set SIS voltage of V2')
parser.add_argument('att', type = float, help = 'set Lo Att. level')

args = parser.parse_args()

sis.set_sis_vp1(args.v1)
sis.set_sis_vp2(args.v2)
att.set_loatt(args.att)

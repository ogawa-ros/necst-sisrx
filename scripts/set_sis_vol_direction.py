#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

sis = controller.sis()

parser = argparse.ArgumentParser(description = 'set SIS voltage V1 and V2')

parser.add_argument('v1', type = float, help = 'set SIS voltage of V1')
parser.add_argument('h1', type = float, help = 'set SIS voltage of V2')
parser.add_argument('h2', type = float, help = 'set SIS voltage of V1')
parser.add_argument('v2', type = float, help = 'set SIS voltage of V2')

args = parser.parse_args()

sis.set_v1(args.v1)
sis.set_h1(args.h1)
sis.set_h2(args.h2)
sis.set_v2(args.v2)

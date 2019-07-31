#!/usr/bin/env python3

name = 'set_sis_vol_and_att_level_direction'

import rospy
import time
import sys
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-sisrx/scripts")

import controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
att1 = tz2019_controller.loatt_h()
att2 = tz2019_controller.loatt_v()

parser = argparse.ArgumentParser(description = 'set SIS voltage V1 and V2 and Lo Att. level')

parser.add_argument('v1', type = float, help = 'set SIS voltage of V1')
parser.add_argument('v2', type = float, help = 'set SIS voltage of V2')
parser.add_argument('att1', type = float, help = 'set Lo Att. level of H-side')
parser.add_argument('att2', type = float, help = 'set Lo Att. level of V-side')

args = parser.parse_args()

sis.set_vp1(args.v1)
sis.set_vp2(args.v2)
att1.set_cur(args.att)
time.sleep(60)
att2.set_cur(args.att)

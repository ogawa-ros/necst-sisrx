#!/usr/bin/env python3

name = 'set_sis_vol_and_att_level_direction'

import rospy
import time
import sys
import std_msgs.msg
import argparse

sys.path.append("/home/hinotoritz/ros/src/necst-tz2019/scripts")

import tz2019_controller

rospy.init_node(name)

sis = tz2019_controller.sis()
att1 = tz2019_controller.loatt_h()
att2 = tz2019_controller.loatt_v()

#v1, h1, h2, v2, att1, att2の値を引数に入力
parser = argparse.ArgumentParser(description = 'set SIS voltage V1 and V2 and Lo Att. level')
parser.add_argument('v1', type = float, help = 'set SIS voltage of V1')
parser.add_argument('h1', type = float, help = 'set SIS voltage of V2')
parser.add_argument('h2', type = float, help = 'set SIS voltage of V1')
parser.add_argument('v2', type = float, help = 'set SIS voltage of V2')
parser.add_argument('att1', type = float, help = 'set Lo Att. level of H-side')
parser.add_argument('att2', type = float, help = 'set Lo Att. level of V-side')
args = parser.parse_args()

#sisに指定した電圧を加える
sis.set_v1_v(args.v1)
sis.set_h1_v(args.h1)
sis.set_h2_v(args.h2)
sis.set_v2_v(args.v2)

#attのレベルを指定した値に設定する
att1.set_cur(args.att1)
time.sleep(60)
att2.set_cur(args.att2)

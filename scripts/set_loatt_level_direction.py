#!/usr/bin/env python3

name = 'set_loatt_level_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/hinotoritz/ros/src/necst-tz2019/scripts")

import tz2019_controller

rospy.init_node(name)

att1 = tz2019_controller.loatt_h()
att2 = tz2019_controller.loatt_v()

#attのレベルを引数に入力
parser = argparse.ArgumentParser(description = 'set Lo Att. level')
parser.add_argument('att1', type = float, help = 'set Lo Att. level of H-side')
parser.add_argument('att2', type = float, help = 'set Lo Att. level of V-side')
args = parser.parse_args()


#GPIBの仕様のためatt1のあとにatt2を設定するときは60s待つ必要がある
att1.set_cur(args.att1)
time.sleep(60)
att2.set_cur(args.att2)

#!/usr/bin/env python3

name = 'yfactior_search_loatt_level_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse


sys.path.append("/home/hinotoritz/ros/src/necst-core/scripts")
sys.path.append("/home/hinotoritz/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

loatt1 = tz2019_controller.loatt_h()
loatt2 = tz2019_controller.loatt_v()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('start', type = int, help = 'set start att_level')
parser.add_argument('stop', type = int, help = 'set stop att_level')
parser.add_argument('step', type = int, help = 'set step att_level')
args = parser.parse_args()


att_vol = list(range(args.start, args.stop, args.step))   #search optimal Lo Att level
date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
for att_v in att_vol:           #measure y-factor
    file_name = name + '/' + date + '/attlevel=%s.necstdb'%(str(att_v))
    print("setting att......please wait 60s")

    loatt1.set_cur(att_v)
    time.sleep(60)
    loatt2.set_cur(att_v)
    print("att_level = %s"%(att_v))
    print("now measurement yfactor")
    time.sleep(50)
    logger.start(file_name)
    time.sleep(10)
    logger.stop()
    continue

print("finish serach.....now setting loatt = 30")
print("please wait 120s ")
loatt1.set_cur(30)
time.sleep(60)
loatt2.set_cur(30)
print("please wait 60s")
time.sleep(60)
print('setting finished')

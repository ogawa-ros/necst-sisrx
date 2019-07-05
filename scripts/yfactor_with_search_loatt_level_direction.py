#!/usr/bin/env python3

name = 'search_loatt_level_direction'

import rospy
import time
import std_msgs.msg
import numpy
import argparse

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
irrsg = controller.irrsg()
loatt = controller.loatt()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s'%(args.save_name)
att_vol = np.arange(21)    #search optimal Lo Att level
logger.start(file_name)
for att_v in att_vol:           #measure y-factor
    loatt.set_loatt(att_v)
    time.sleep(1)
    continue
logger.stop()

#!/usr/bin/env python3

name = 'measure_yfactior_search_loatt_level_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse
import plot_tool

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-tz2019/scripts")

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

irrsg = controller.irr()
loatt1 = tz2019_controller.loatt_h()
loatt2 = tz2019_controller.loatt_v()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('start', type = int, help = 'set start att_level')
parser.add_argument('stop', type = int, help = 'set stop att_level')
parser.add_argument('step', type = int, help = 'set step att_level')
args = parser.parse_args()

thot = float(input("thot:"))
tcold = float(input("tcold:"))

att_vol = range(args.start, args.stop, args.step)    #search optimal Lo Att level
att_v_array = []
trxarray = []
for att_v in att_vol:           #measure y-factor
    file_name = '/home/exito/data/logger/test/%s/attlevel = %s_data/rawdata.db'%(args.save_name, str(att_v))
    save = '%s/attlevel = %s_data'%(args.save_name, str(att_v))
    print("setting att......please wait 60s")

    loatt1.set_cur(att_v)
    time.sleep(60)
    loatt2.set_cur(att_v)
    logger.start(file_name)
    print("att_level = %s"%(att_v))
    print("now measurement yfactor")
    time.sleep(60)
    logger.stop()
    trx = plot_tool.yfactor_cal(file_name, save, thot, tcold)
    print("Trx = %s"%(trx))
    att_v_array.append(att_v)
    trxarray.append(trx)
    continue

plot_tool.att_level_yfactor_plot(att_v_array, trxarray, args.save_name)
print("finish serach.....now setting loatt = 30")

loatt1.set_cur(30)
time.sleep(60)
loatt2.set_cur(30)

print(str(trxarray))
print(str(att_v_array))

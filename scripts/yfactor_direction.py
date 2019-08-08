#!/usr/bin/env python3

name = 'measure_yfactor_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse
import numpy as np

sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller


import plot_tool

rospy.init_node(name)

logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'measure Y-factor only')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

thot = float(input("thot[K]:"))
tcold = float(input("tcold[K]:"))

file_name = '/home/exito/data/logger/test/%s/rawdata.db'%(args.save_name)
logger.start(file_name)
time.sleep(10)
logger.stop()

trx = plot_tool.yfactor_plot(file_name, args.save_name, thot, tcold)
np.save(
'/home/exito/data/logger/test/'+str(args.save_name)+'/trx_data',
trx
)
print(str(trx))

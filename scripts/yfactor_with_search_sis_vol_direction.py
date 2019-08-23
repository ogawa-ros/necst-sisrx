#!/usr/bin/env python3

name = 'yfactor_search_sis_vol_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
import argparse
#import plot_tool
import matplotlib.pyplot as plt
import datetime

sys.path.append("/home/hinotoritz/ros/src/necst-core/scripts")

import controller
import core_controller
#import plot_tool

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical sis voltage value')

#parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('polarization', type = str,  choices = ['V', 'H'], help = 'choice polarization V or H')

#thot = float(input("thot[K]:"))
#tcold = float(input("tcold[K]:"))

args = parser.parse_args()

    volp1 = np.linspace(-2, 0, 20)   #search optimal SIS voltage value
    volp2 = np.linspace(-2, 0, 20)



#trxarray = []
#v1array = []
#v2array = []
date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

count = 0
for vp1 in volp1:             #measure y-factor
    sis.set_vp1(vp1)
    for vp2 in volp2:
        count+=1
        sis_v = []

        save = 'vp1=%s_vp2=%s_'%(str(vp1), str(vp2)) + args.polarization + '-pol'
        file_name = name + '/' + date + '/' + '{0:03d}'.format(count) + '.necstdb'
        print('--------------------')
        print(file_name)


        sis.set_vp2(vp2)
        time.sleep(2)

        logger.start(file_name)
        time.sleep(5)
        logger.stop()
        #trx = plot_tool.yfactor_cal(file_name, thot, tcold)
        #print('Trx = ' + str(trx))
        #print('--------------------')
        #sis_v = plot_tool.sis_vol_average(file_name)

        #if args.polarization == 'V':
        #    v1 = sis_v[0]
        #    v2 = sis_v[3]
        #if args.polarization == 'H':
        #    v1 = sis_v[1]
        #    v2 = sis_v[2]

        #trxarray.append(trx)
        #v1array.append(v1)
        #v2array.append(v2)

        continue
    continue


sis.set_vgap(0)

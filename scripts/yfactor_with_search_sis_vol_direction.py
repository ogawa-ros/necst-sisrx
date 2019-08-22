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

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical sis voltage value')

#parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('polarization', type = str,  choices = ['V', 'H'], help = 'choice polarization V or H')

#thot = float(input("thot[K]:"))
#tcold = float(input("tcold[K]:"))

args = parser.parse_args()

volp1 = np.linspace(-2, 0, 5)   #search optimal SIS voltage value
volp2 = np.linspace(-2, 0, 5)

#trxarray = []
v1array = []
v2array = []

for vp1 in volp1:             #measure y-factor
    sis.set_vp1(vp1)
    for vp2 in volp2:
        sis_v = []

        save = '%svp1=%s_vp2='%(str(vp1), str(vp2)) + args.polarization + '-pol'
        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        file_name = name + '/' + date + save + '.necstdb'
        print('--------------------')
        print(file_name)


        sis.set_vp2(vp2)
        time.sleep(2)

        logger.start(file_name)
        time.sleep(10)
        logger.stop()
        #trx = plot_tool.yfactor_cal(file_name, thot, tcold)
        #print('Trx = ' + str(trx))
        #print('--------------------')
        sis_v = plot_tool.sis_vol_average(file_name)

        if args.polarization == 'V':
            v1 = sis_v[0]
            v2 = sis_v[3]
        if args.polarization == 'H':
            v1 = sis_v[1]
            v2 = sis_v[2]

        #trxarray.append(trx)
        #print("Trxarray = " + str(trxarray))
        v1array.append(v1)
        v2array.append(v2)
        #print("v1 = "+ str(v1array))
        #print("v2 = "+ str(v2array))
        continue
    continue

#plot_tool.sis_bias_and_yfactor_matrix_plot(v1array, v2array, trxarray, args.save_name)
#trxarray = numpy.reshape(trxarray, (5,5))
#v1array = numpy.reshape(v1array, (5,5))
#v2array = numpy.reshape(v2array, (5,5))
#print('v1 = ')
#print(str(v1array))
#print('v2 = ')
#print(str(v2array))
#print('trx or tsys = ')
#print( str(trxarray))
sis.set_vgap(0)

#!/usr/bin/env python3

name = 'measure_yfactor_search_sis_vol_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical sis voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('polarization', choices = ['V', 'H'], help = 'choice polarization V or H')

args = parser.parse_args()

volp1 = np.linspace(-1, 0, 5)   #search optimal SIS voltage value
volp2 = np.linspace(-1, 0, 5)

trxarray = []
v1array = []
v2array = []

for vp1 in volp1:             #measure y-factor
    sis.set_vp1(vp1)
    for vp2 in volp2:
        sis_v = []

        h = 6.626*10**(-34)
        e = 1.602*10**(-19)
        lofreq = 92*10**9
        n = 3
        vp1_s = ((n*h*lofreq*vp1)/e + 2.8*n)
        vp2_s = ((n*h*lofreq*vp2)/e + 2.8*n)

        save = '%s_v1=%s_v2=%s_%s-pol'%(args.save_name, str(vp1_s), str(vp2_s),args.polarization)
        file_name = '/home/exito/data/logger/test/%s.db'%(save)

        sis.set_vp2(vp2)
        
        logger.start(file_name)
        time.sleep(10)
        trx = plot_tool.yfactor_prot(file_name, save)
        logger.stop()
        sis_v = plot_tool.sis_vol_average(file_name)

        if args.polarization == 'V':
            v1 = sis_v[0]
            v2 = sis_v[3]
        elif:
            v1 = sis_v[1]
            v2 = sis_v[2]

        trxarray.append(trx)
        v1array.append(v1)
        v2array.append(v2)
        continue
    continue
    plot_tool.sis_bias_and_yfactor_matrix_plot(v1array, v2array, trxarray, save)
sis.set_vgap(0)

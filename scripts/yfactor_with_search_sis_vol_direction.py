#!/usr/bin/env python3

name = 'measure_yfactor_search_sis_vol_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
import argparse
import plot_tool
import matplotlib.pyplot as plt

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

        save = '%s/vp1=%s_vp2=%s_%s-pol'%(args.save_name, str(vp1), str(vp2), args.polarization)
        file_name = '/home/exito/data/logger/test/' + save + '.db'
        print('--------------------')
        print(file_name)


        sis.set_vp2(vp2)

        logger.start(file_name)
        time.sleep(10)
        logger.stop()
        trx = plot_tool.yfactor_plot(file_name, save)
        print('Trx = ' + str(trx))
        print('--------------------')
        sis_v = plot_tool.sis_vol_average(file_name)

        if args.polarization == 'V':
            v1 = sis_v[0]
            v2 = sis_v[3]
        if args.polarization == 'H':
            v1 = sis_v[1]
            v2 = sis_v[2]

        trxarray.append(trx)
        print("Trxarray = " + str(trxarray))
        v1array.append(v1)
        v2array.append(v2)
        print("v1 = "+ str(v1array))
        print("v2 = "+ str(v2array))
        continue
    continue

x = v1array
y = v2array
z = trxarray
np.save(
'/home/exito/data/logger/test/'+str(args.save_name)+'/yfactor_map_data',
x,y,z
)


plt.scatter(x, y, c=z)
pp=plt.colorbar (orientation="vertical")
pp.set_label("Trx[K]")
plt.xlabel('v1_vol[mV]')
plt.ylabel('v2_vol[mV]')
plt.title("yfactor_map")
plt.xlim(-2, 9)
plt.ylim(-2, 9)
plt.grid()

plt.savefig('/home/exito/data/logger/test/' + str(args.save_name) + '/yfactor_matrix.png')

#plot_tool.sis_bias_and_yfactor_matrix_plot(v1array, v2array, trxarray, args.save_name)
sis.set_vgap(0)

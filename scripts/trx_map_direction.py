#!/usr/bin/env python3

#trxまたはtsysのSIS電圧マップを測定する
name = 'trx_map_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse
import matplotlib.pyplot as plt
import datetime

sys.path.append("/home/hinotoritz/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()


#測定するPolarizationの選択
pol = str(input('polarization[V or H]:'))

#電圧を振る範囲と間隔を入力
if pol == 'V':
    v1_s = float(input('v1_start:'))
    v1_f = float(input('v1_finish:'))
    v1_i = float(input('v1_interval:'))
    sis1 = numpy.linspace(v1_s, v1_f, v1_i)

    v2_s = float(input('v2_start:'))
    v2_f = float(input('v2_finish:'))
    v2_i = float(input('v2_interval:'))
    sis2 = numpy.linspace(v2_s, v2_f, v2_i)

if pol == 'H':
    h1_s = float(input('h1_start:'))
    h1_f = float(input('h1_finish:'))
    h1_i = float(input('h1_interval:'))
    sis1 = numpy.linspace(h1_s, h1_f, h1_i)

    h2_s = float(input('h2_start:'))
    h2_f = float(input('h2_finish:'))
    h2_i = float(input('h2_interval:'))
    sis2 = numpy.linspace(h2_s, h2_f, h2_i)


#測定を開始した時間を取得
date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

#sisに電圧を振る
count = 0
for s1 in sis1:
    sis.set_v1_v(s1)
    sis.set_h1_v(s1)
    for s2 in sis2:
        count+=1
        file_name = name + '/' + date + '/' + '{0:03d}'.format(count) + '.necstdb'
        print('--------------------')
        print(file_name)
        sis.set_h2_v(s2)
        sis.set_v2_v(s2)
        time.sleep(2)

        logger.start(file_name)
        time.sleep(5)
        logger.stop()
        continue
    continue

#sisの電圧を0にして終了
sis.set_vgap(0)

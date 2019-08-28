#!/usr/bin/env python3

name = 'set_phase_matrix_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

irr = controller.irr()

#onするかoffするか引数に入力
parser = argparse.ArgumentParser(description = 'set freq and power of Phase Matrix and on/off Phase Matrix')
parser.add_argument('on_off', choices = ['on', 'off'], type = str, help = 'on/off Phase Matrix')
#parser.add_argument('freq', type = float, help = 'set freq of Phase Matrix')
#parser.add_argument('power', type = float, help = 'set power of Phase Matrix')
args = parser.parse_args()

#loの逓倍実数に合わせて周波数を決める,phase_matrixは出力を変えることはできない
#86GHz = 15.33333GHz * 6
if args.on_off == 'on':
    freq = float(input("Freq[GHz]:"))
    irr.set_sg_freq(freq)
    #irr.set_sg_power(args.power)
    irr.set_sg_onoff(args.on_off)

elif args.on_off == 'off':
    irr.set_sg_onoff(args.on_off)

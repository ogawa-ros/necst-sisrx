#!/usr/bin/env python3

name = 'set_phase_matrix_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

irr = controller.irr()

parser = argparse.ArgumentParser(description = 'set freq and power of Phase Matrix and on/off Phase Matrix')

parser.add_argument('on_off', choices = ['on', 'off'], type = str, help = 'on/off Phase Matrix')
parser.add_argument('freq', type = float, help = 'set freq of Phase Matrix')
parser.add_argument('power', type = float, help = 'set power of Phase Matrix')

args = parser.parse_args()

if args.on_off == 'on':
    irr.set_freq(args.freq)
    irr.set_sg_power(args.power)
    irr.set_sg_onoff(args.on_off)

elif args.on_off == 'off':
    irr.set_sg_onoff(args.on_off)

#!/usr/bin/env python3

name = 'yfactor_irr_directions'


import rospy
import time
import std_msgs.msg

import controller
import core_controller
import tz2019_controller

rospy.init_node(name)

sis = controller.sis()
irrsg = controller.irrsg()
lo = controller.lo1st()
loatt = controller.loatt()
logger = core_controller.logger()
switch = tz2019_controller.switch()

freq = input("1st Lo freq: ")       #set Lo SG value
power = input("1st Lo power: ")
lo.set_lo1st_freq(freq)
lo.set_lo1st_power(power)

while question is not 'OK':
    att_vol = input("Lo Att vol: ")     #search Lo Att value when Parameter Search
    sis.set_sis_vp(0)
    loatt.set_loatt_vol(att_vol)
    bands = {'hu':, 'hl':, 'vu':, 'vl':}
    for band in bands:                  #x4 repeat hu,hl,vu,vl
        switch_value = band
        switch.set_if_switch(switch_value)
        logger.start(iv_band)
        time.sleep()
        logger.stop()
    question = input("Are you OK or NOT?: ")

while question is not 'OK':
    volp = input("SIS vol: ")
    sis.set_sis_vp(volp)
    bands = {'hu':, 'hl':, 'vu':, 'vl':}
    for band in bands:              #x4 repeat hu,hl,vu,vl
        switch_value = band
        switch.set_if_switch(switch_value)
        input("Are you ready for hot measure?: ")
        logger.start(hot_band)
        time.sleep()
        logger.stop()
        input("Are you ready for cold measure?: ")
        logger.start(cold_band)
        time.sleep()
        logger.stop()     #have to repeat until determining optimal voltage value
    question = input("Are you OK or NOT?: ")

while question is not 'OK':
    att_vol = input("Lo Att vol: ")
    loatt.set_loatt_vol(att_vol)   #necessary anather loatt_vol?
    bands = {'hu':, 'hl':, 'vu':, 'vl':}
    for band in bands:             #x4 repeat hu,hl,vu,vl
        switch_value = band
        switch.set_if_switch(switch_value)
        logger.start(hot_band)
        time.sleep()
        logger.stop()
        time.sleep()
        logger.start(cold_band)
        time.sleep()
        logger.stop()    #have to repeat until determining optimal att voltage value
    question = input("Are you OK or NOT?: ")

pols = ['h', 'v']
for pol in pols:
    sides = {'upper', 'lower':}
    for side in sides:
        irr_freq = input("IRRSG %s freq: "%(side))   #measure irr of h side
        irr_power = input("IRRSG %s power: "%(side))
        irrsg.set_irrsg_freq(irr_freq)
        irrsg.set_irrsg_power(irr_power)
        if pol is 'h':
            bands = ['hu', 'hl']
        elif pol is 'v':
            bands = ['vu', 'vl']
        for band in bands:
            switch.set_if_switch(band)
            input("Are you ready for IRR %s measure: "%(band))
            logger.start(band)
            time.sleep()
            logger.stop()

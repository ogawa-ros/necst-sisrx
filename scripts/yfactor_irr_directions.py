#!/usr/bin/env python3

name = 'yfactor_irr_directions'


import rospy
import time
import std_msgs.msg

import controller
import core_controller
import tz2019_controller

sisrx_node_name = 'sisrx_controller'
core_node_name = 'core_controller'
tz2019_node_name = 'tz2019_controller'
rospy.init_node(sisrx_node_name)
rospy.init_node(core_node_name)
rospy.init_node(tz2019_node_name)

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
        logger.start(hot_band)
        time.sleep()
        logger.stop()
        time.sleep()
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

irr_freq_low = input("IRRSG lower freq: ")   #measure irr of h side
irr_power_low = input("IRRSG lower power: ")
irrsg.set_irrsg_freq(irr_freq_low)
irrsg.set_irrsg_power(irr_power_low)
switch.set_if_switch(hl)
logger.start(irr_low)
time.sleep()
logger.stop()
switch.set_if_switch(hu)
logger.start(irr_low)
time.sleep()
logger.stop()
irr_freq_up = input("IRRSG upper freq: ")
irr_power_up = input("IRRSG upper power: ")
irrsg.set_irrsg_freq(irr_freq_up)
irrsg.set_irrsg_power(irr_power_up)
switch.set_if_switch(hl)
logger.start(irr_up)
time.sleep()
logger.stop()
switch.set_if_switch(hu)
logger.start(irr_up)
time.sleep()
logger.stop()

irr_freq_low = input("IRRSG lower freq: ")     #measure irr of v side
irr_power_low = input("IRRSG lower power: ")
irrsg.set_irrsg_freq(irr_freq_low)
irrsg.set_irrsg_power(irr_power_low)
switch.set_if_switch(vl)
logger.start(irr_low)
time.sleep()
logger.stop()
switch.set_if_switch(vu)
logger.start(irr_low)
time.sleep()
logger.stop()
irr_freq_up = input("IRRSG upper freq: ")
irr_power_up = input("IRRSG upper power: ")
irrsg.set_irrsg_freq(irr_freq_up)
irrsg.set_irrsg_power(irr_power_up)
switch.set_if_switch(vl)
logger.start(irr_up)
time.sleep()
logger.stop()
switch.set_if_switch(vu)
logger.start(irr_up)
time.sleep()
logger.stop()

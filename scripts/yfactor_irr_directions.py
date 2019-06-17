#!/usr/bin/env python3

name = 'yfactor_irr_directions'


import rospy
import time
import std_msgs.msg

import controller
import core_controller

sisrx_node_name = 'sisrx_controller'
core_node_name = 'core_controller'
rospy.init_node(sisrx_node_name)
rospy.init_node(core_node_name)

sis = controller.sis()
irrsg = controller.irrsg()
lo = controller.lo1st()
loatt = controller.loatt()
logger = core_controller.logger()

freq = input("1st Lo freq: ")
power = input("1st Lo power: ")
lo.set_lo1st_freq(freq)
lo.set_lo1st_power(power)

att_vol = input("Lo Att vol: ")
sis.set_sis_vp(0)
loatt.set_loatt_vol(att_vol)
logger.start(iv)
time.sleep()
logger.stop()

volp = input("SIS vol: ")
sis.set_sis_vp(volp)
logger.start(hot)
time.sleep()
logger.stop()
logger.start(cold)
time.sleep()
logger.stop()     #have to repeat until determining optimal voltage value

att_vol = input("Lo Att vol: ")
loatt.set_loatt_vol(att_vol)   #necessary anather loatt_vol?
logger.start(hot)
time.sleep()
logger.stop()
logger.start(cold)
time.sleep()
logger.stop()    #have to repeat until determining optimal att voltage value

irr_freq_low = input("IRRSG lower freq: ")
irr_power_low = input("IRRSG lower power: ")
irrsg.set_irrsg_freq(irr_freq_low)
irrsg.set_irrsg_power(irr_power_low)
logger.start(irr_low)
time.sleep()
logger.stop()
irr_freq_up = input("IRRSG upper freq: ")
irr_power_up = input("IRRSG upper power: ")
irrsg.set_irrsg_freq(irr_freq_up)
irrsg.set_irrsg_power(irr_power_up)
logger.start(irr_up)
time.sleep()
logger.stop()

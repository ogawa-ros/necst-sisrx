#!/usr/bin/env python3

name = 'yfactor_irr_directions'


import rospy

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

lo.set_lo1st_freq(freq)
lo.set_lo1st_power(power)

sis.set_sis_vp(0)
loatt.set_loatt_vol(att_vol)
logger.logger(iv)

sis.set_sis_vp(volp)
logger.logger(hot)
logger.logger(cold)     #have to repeat until determining optimal voltage value

loatt.set_loatt_vol(att_vol)   #necessary anather loatt_vol?
logger.logger(hot)
logger.logger(cold)     #have to repeat until determining optimal att voltage value

irrsg.set_irrsg_freq(irr_freq_low)
irrsg.set_irrsg_power(irr_power_low)
logger.logger(irr_low)
irrsg.set_irrsg_freq(irr_freq_up)
irrsg.set_irrsg_power(irr_power_up)
logger.logger(irr_up)

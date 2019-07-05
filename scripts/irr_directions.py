#!/usr/bin/env python3

name = 'irr_directions'


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


pols = ['h', 'v']
for pol in pols:
    sides = {'upper', 'lower':}
    for side in sides:
        irr_freq = input("IRRSG %s freq: "%(side))   #measure irr of h side
        irr_power = input("IRRSG %s power: "%(side))
        irrsg.set_irr_freq(irr_freq)
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

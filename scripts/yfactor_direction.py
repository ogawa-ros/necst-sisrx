#!/usr/bin/env python3

name = 'yfactor_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse
import numpy
import datetime

sys.path.append("/home/hinotoritz/ros/src/necst-core/scripts")
import core_controller


rospy.init_node(name)

logger = core_controller.logger()

#日時を取得し保存先を決める
date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'

#データの取得を行う
logger.start(file_name)
time.sleep(10)
logger.stop()

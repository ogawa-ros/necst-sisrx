#!/usr/bin/env python3

name = 'sisrx_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.ps = PS()
        self.sis = SIS()
        self.irrsg = IRRSG()
        self.lo1st = LO1ST()
        self.loatt = LOATT()



class PS(object):

    def __init__(self):

        self.pub = {}
        pass

    def publish(self, topic_name, msg):
        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class, queue_size, latch = True):
        if topic_name not in self.pub:
            self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size =queue_size, latch = latch)
            time.sleep(0.01)
        else:
            pass
        return


class SIS(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = PS()

    def sis_vp(self, command):
        topic_name = '/necst_sisrx/sis/vp_cmd'

        self.ps.set_publisher(topic_name = topic_name, data_class = std_msgs.msg.Float64, queue_size = 1, latch = True)

        self.ps.publish(topic_name = topic_name, msg = command)
        return


class IRRSG(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = PS()

    def irrsg_f(self, command):
        topic_name = '/necst_sisrx/irrsg/f_cmd'

        self.ps.set_publisher(topic_name = topic_name, data_class = std_msgs.msg.Float64, queue_size = 1, latch = True)

        self.ps.publish(topic_name = topic_name, msg = command)

    def irrsg_p(self, command):
        topic_name = '/necst_sisrx/irrsg/p_cmd'

        self.ps.set_publisher(topic_name = topic_name, data_class = std_msgs.msg.Float64, queue_size = 1, latch = True)

        self.ps.publish(topic_name = topic_name, msg = command)


class 

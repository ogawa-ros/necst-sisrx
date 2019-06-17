#!/usr/bin/env python3

name = 'sisrx_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.sis = sis()
        self.irrsg = irrsg()
        self.lo1st = lo1st()
        self.loatt = loatt()



class make_pub(object):

    def __init__(self):

        self.pub = {}
        pass

    def publish(self, topic_name, data_class, msg):
        if topic_name not in self.pub:
            self.set_publisher(topic_name = topic_name, data_class = data_class)
            pass

        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class):
        if topic_name not in self.pub:
            self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
            time.sleep(0.01)
        else:
            pass
        return


class sis(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = make_pub()

    def set_sis_vp(self, command):
        topic_name = '/necst_sisrx/sis/vp_cmd'
        data_class = std_msgs.msg.Float64

        self.ps.publish(topic_name, data_class, msg = command )
        return


class irrsg(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = make_pub()

    def set_irrsg_freq(self, command):
        topic_name = '/necst_sisrx/irrsg/f_cmd'
        data_class = std_msgs.msg.Float64

        self.ps.publish(topic_name, data_class, msg = command)

    def set_irrsg_power(self, command):
        topic_name = '/necst_sisrx/irrsg/p_cmd'
        data_class = std_msgs.msg.Float64

        self.ps.publish(topic_name, data_class, msg = command)


class lo1st(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = make_pub()

    def set_lo1st_freq(self, command):
        topic_name = '/necst_sisrx/lo1st/f_cmd'
        data_class = std_msgs.msg.Float64

        self.ps.publish(topic_name, data_class, msg = command)

    def set_lo1st_power(self, command):
        topic_name = '/necst_sisrx/lo1st/p_cmd'
        data_class = std_msgs.msg.Float64

        self.ps.publish(topic_name, data_class, msg = command)


class loatt(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = make_pub()

    def set_loatt_vol(self, command):
        topic_name = '/necst_sisrx/loatt/v_cmd'
        data_class = std_msgs.msg.Float64

        self.ps.publish(topic_name, data_class, msg = command)

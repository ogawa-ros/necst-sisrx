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



class make_pub(object):      #make publiher and publish of model

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
            pass
        return


class sis(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_sis_vp1(self, command):
        topic_name = '/necst/rx_sis2sb/vp1_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sis_vp2(self, command):
        topic_name = '/necst/rx_sis2sb/vp2_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sis_vgap(self):
        topic_name = '/necst/rx_sis2sb/vgap_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, mag = command)
        return


class irrsg(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_irr_freq(self, command):
        topic_name = '/necst/rx_sis2sb/irr/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_irrsg_freq(self, command):
        topic_name = '/necst/rx_sis2sb/irrsg/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_irrsg_power(self, command):
        topic_name = '/necst/rx_sis2sb/irrsg/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_irrsg_onoff(self, command):
        topic_name = '/necst/rx_sis2sb/irrsg/onoff_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class lo1st(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_lo1_freq(self, command):
        topic_name = '/necst/rx_sis2sb/lo1/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_lo1sg_freq(self, command):
        topic_name = '/necst/rx_sis2sb/lo1sg/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_lo1sg_power(self, command):
        topic_name = '/necst/rx_sis2sb/lo1sg/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_lo1sg_onoff(self, command):
        topic_name = '/necst/rx_sis2sb/lo1sg/onoff_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class loatt(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_loatt(self, command):
        topic_name = '/necst/rx_sis2sb/loatt/i_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

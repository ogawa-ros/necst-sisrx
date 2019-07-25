#!/usr/bin/env python3

name = 'sisrx_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.sis = sis()
        self.irr = irr()
        self.lo1 = lo1()
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
        self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
        time.sleep(0.1)
        return


class sis(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_vp1(self, command):
        topic_name = '/necst/rx_sis2sb/vp1_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_vp2(self, command):
        topic_name = '/necst/rx_sis2sb/vp2_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_vgap(self, command):
        topic_name = '/necst/rx_sis2sb/vgap_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v1(self, command):
        topic_name = 'tz2019/sis_v1/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h1(self, command):
        topic_name = 'tz2019/sis_h1/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h2(self, command):
        topic_name = 'tz2019/sis_h2/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v2(self, command):
        topic_name = 'tz2019/sis_v2/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

class irr(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_freq(self, command):
        topic_name = '/necst/rx_sis2sb/irr/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sg_freq(self, command):
        topic_name = '/necst/rx_sis2sb/irrsg/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sg_power(self, command):
        topic_name = '/necst/rx_sis2sb/irrsg/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sg_onoff(self, command):
        topic_name = '/necst/rx_sis2sb/irrsg/onoff_cmd'
        data_class = std_msgs.msg.String

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class lo1(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_freq(self, command):
        topic_name = '/necst/rx_sis2sb/lo1/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sg_freq(self, command):
        topic_name = '/necst/rx_sis2sb/lo1sg/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sg_power(self, command):
        topic_name = '/necst/rx_sis2sb/lo1sg/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_sg_onoff(self, command):
        topic_name = '/necst/rx_sis2sb/lo1sg/onoff_cmd'
        data_class = std_msgs.msg.String

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class loatt(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_cur(self, command):
        topic_name = '/necst/rx_sis2sb/loatt/i_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

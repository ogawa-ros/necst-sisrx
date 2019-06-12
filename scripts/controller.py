#!/usr/bin/env python3

name = 'sisrx_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.ps = PS()
        self.sis = SIS()



class PS(object):

    pub = {}

    def __init__(self):
        pass

    def publish(self, topic_name, msg):
        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class, latch = True, queue_size):
        if topic_name not in self.pub:
            rospy.Publisher(name = topic_name, data_class = data_class, latch = latch, queue_size =queue_size)
            time.sleep(0.01)
        else:
            pass
        return


class SIS(object):

    def __init__(self):
        self.ps = PS()

    def sis_vp(self):
        name = '/necst_sisrx/sis/vp_cmd'

        self.ps.set_publisher(topic_name = name, data_class = std_msgs.msg.Float64, latch = True, queue_size = 1)

        self.ps.publish(topic_name = name, msg = command)
        return


if __name__ == "__main__":
    rospy.init_node(name)
    rospy.spin()

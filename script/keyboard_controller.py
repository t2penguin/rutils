#!/usr/bin/env python

import sys, os
import rospy
from geometry_msgs.msg import Twist
# sys.path.append(os.getcwd()) # for getch
from getch import getch
from abc_motion import ABCMotion


class KeyboardController(ABCMotion):
    def __init__(
            self, 
            pub_topic_name
        ):

        super().__init__(pub_topic_name)

        self.v = 0.5
        self.w = 0.5


    def motion(self):
        self.keyboard_controller()
        
        return self.twist_msg


    def keyboard_controller(self):
        self.twist_msg.linear.x = 0.
        self.twist_msg.angular.z = 0.

        ward = getch()

        if ward == 'i':
            self.twist_msg.linear.x = self.v
        elif ward == 'k':
            self.twist_msg.linear.x = -1. * self.v
        elif ward == 'j':
            self.twist_msg.angular.z = self.w
        elif ward == 'l':
            self.twist_msg.angular.z = -1. * self.w
        else:
            pass


if __name__ == '__main__':
    print('Sample: ABCMotion')

    node = KeyboardController(
            pub_topic_name='/jackal_velocity_controller/cmd_vel')
    rospy.init_node('ABCMotion_node')

    rate = rospy.Rate(30)#Hz

    while not rospy.is_shutdown():
        node.forward()
        rate.sleep()

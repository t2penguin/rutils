#!/usr/bin/env python

import sys, os
import rospy
from geometry_msgs.msg import Twist
from getch import getch


class ABCMotion:
    """
    ABCMotion class represents a pattern of ROS-node 
    that output Twist messages.

    Attributes:
        pub_topic_name (str): Publish topic name of twist messages.
        pub (rospy.Publisher): Publisher object.
        twist_msg (Twist): Twist message.

    Methods:
        forward(): main function of this class.
        motion(): calc motion. Please over-ride this function.
    """


    def __init__(
            self, 
            pub_topic_name
        ):

        self.pub_topic_name = pub_topic_name
        self.pub = rospy.Publisher(
                self.pub_topic_name, 
                Twist, 
                queue_size=1
        )

        self.twist_msg = Twist()


    def forward(self):
        self.twist_msg = self.motion()
        self.pub.publish(self.twist_msg)


    def motion(self):
        pass


# Example usage
if __name__ == '__main__':
    print('Sample: ABCMotion')

    node = ABCMotion(
            pub_topic_name='/jackal_velocity_controller/cmd_vel'
    )

    rospy.init_node('ABCMotion_node')

    rate = rospy.Rate(30)#Hz

    while not rospy.is_shutdown():

        node.forward()

        rate.sleep()


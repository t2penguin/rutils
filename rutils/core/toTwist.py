#!/usr/bin/env python

import sys, os
import rospy
from geometry_msgs.msg import Twist
from core.rnode import RNode


class ToTwist(RNode):
    """
    ToTwist class represents a pattern of a ROS-node 
    that output Twist messages.

    Attributes:
        pub_topic_name (str): Publish topic name of twist messages.
        pub (rospy.Publisher): Publisher object.
        twist_msg (Twist): Twist message.

    Methods:
        forward(): main function of this class.
    """


    def __init__(
            self, 
            pub_topic_name,
            pub_service_class
        ):

        super(ToTwist).__init__(
                pub_topic_name=pub_topic_name,
                pub_service_class=pub_service_class
        )

        self.twist_msg = Twist()


    def forward(self):
        self.calculate_twist()

        self.pub.publish(self.twist_msg)


    def calculate_twist(self):
        self.twist_msg = Twist()


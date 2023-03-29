#!/usr/bin/env python

import sys, os
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class RNode:
    """
    RNode class represents a pattern of a ROS-node.

    Attributes:
        pub_topic_name (str): Publish topic name of twist messages.
        pub (rospy.Publisher): Publisher object.

    Methods:
        forward(): main function of this class.
    """


    def __init__(
            self, 
            sub_topic_name:str=None,
            sub_service_class=None,
            pub_topic_name:str=None,
            pub_service_class=None
        ):
        
        if sub_topic_name != None and sub_service_class != None:
            self.sub_topic_name = sub_topic_name
            print('Sub: \"' + self.sub_topic_name + '\"')
            self.sub = rospy.Subscriber(
                    self.sub_topic_name,
                    sub_service_class,
                    self.callback
            )
        else:
            print('Sub: None')

        if pub_topic_name != None and pub_service_class != None:
            self.pub_topic_name = pub_topic_name
            self.pub = rospy.Publisher(
                    self.pub_topic_name, 
                    pub_service_class, 
                    queue_size=1
            )
        else:
            print('Pub: None')

       
    def forward(self):
        pass


    def callback(self, msg):
        pass


# Example usage
if __name__ == '__main__':
    print('Sample: ABCMotion')

    rnode = RNode(
            pub_topic_name='/jackal_velocity_controller/cmd_vel'
    )

    rospy.init_node('ABCMotion_node')

    rate = rospy.Rate(30)#Hz

    while not rospy.is_shutdown():

        rnode.forward()

        rate.sleep()


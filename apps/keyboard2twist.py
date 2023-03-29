#!/usr/bin/env python

from core.toTwist import ToTwist
from utils.getch import getch


class KeyboradApp(ToTwist):
    """
    KeyboradApp class represents a pattern of a ROS-node 
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


    def calculate_twist(self):
        keyboard_controller()

    
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
    print('Sample: KeyboardApp2twist')

    node = KeyboradApp(
            pub_topic_name='/jackal_velocity_controller/cmd_vel')
    rospy.init_node('KeyboradApp_node')

    rate = rospy.Rate(30)#Hz

    while not rospy.is_shutdown():
        node.forward()
        rate.sleep()

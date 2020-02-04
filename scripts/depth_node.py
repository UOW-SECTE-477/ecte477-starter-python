#!/usr/bin/env python
"""
    depth_node.py

    A ROS node that keeps track of the latest depth map and provides a service to
    query the depth of a given pixel

    Subscribed: camera/aligned_depth/image_raw/
    Publishes: 

    Created: 2020/02/04
    Author: Brendan Halloran
"""

import rospy
from sensor_msgs.msg import Image

class depth_node:
    def __init__(self):
        self.subscriber = rospy.Subscriber('camera/aligned_depth/image_raw/', Image, self.callback_depth)

    def callback_depth(self, data):
        # Do something
    
if __name__ == '__main__':
    print "Starting ROS Depth module"
    dp = depth_node()
    rospy.init_node('depth_node', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Depth module"
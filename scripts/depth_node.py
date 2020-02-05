#!/usr/bin/env python
"""
    depth_node.py

    A ROS node that keeps track of the latest depth map and provides a service to
    query the depth of a given pixel

    Subscribed: camera/aligned_depth_to_color/image_raw/
    Publishes: 

    Created: 2020/02/04
    Author: Brendan Halloran
"""

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Constants
DEPTH_SCALE = 0.001     # Depth is given in integer values on 1mm

class depth_node:
    def __init__(self):
        self.subscriber = rospy.Subscriber('camera/aligned_depth_to_color/image_raw/', Image, self.callback_depth)

    def callback_depth(self, data):
        print "callback_depth()"
        bridge = CvBridge()
        try:
            depth_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
            depth_array = np.array(depth_image, dtype=np.float32)
            center_idx = np.array(depth_array.shape) / 2
            print "center depth: {0}".format( DEPTH_SCALE * depth_array[center_idx[0], center_idx[1]])
        except CvBridgeError, e:
            print e

	# Display the result
	cv2.imshow('cv_depth', depth_image)
	cv2.waitKey(2)
    
if __name__ == '__main__':
    print "Starting ROS Depth module"
    rospy.init_node('depth_node', anonymous=True)
    dp = depth_node()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Depth module"

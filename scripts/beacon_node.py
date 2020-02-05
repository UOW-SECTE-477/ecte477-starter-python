#!/usr/bin/env python
"""
    beacon_node.py

    A ROS node that searching in colour images for any beacons and tries to 
    find its location relative to the robot.

    Subscribed: camera/colour/image_raw/compressed
    Publishes: 

    Created: 2020/02/04
    Author: Brendan Halloran
"""

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import CompressedImage
from colours import Colours
from cv_bridge import CvBridge, CvBridgeError

class beacon_node:
    def __init__(self):
        self.subscriber = rospy.Subscriber('camera/color/image_raw/compressed', CompressedImage, self.callback_colour_image)
        self.beacons = rospy.get_param("~beacons")
        self.beacons_found = [False]*len(self.beacons)

        print self.beacons              # beacons is a list of dictionaries
        print self.beacons_found        # beacons_found is a list of booleans
        print self.beacons[1]['top']    # You can access the dict values for each beacon by name


    def callback_colour_image(self, data):
        print "callback_colour_image()"
        # Decompress image and load into numpy array
        np_arr = np.fromstring(data.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Display the result
        cv2.imshow('cv_img', frame)
        cv2.waitKey(2)

if __name__ == '__main__':
    print "Starting ROS Beacon Detector module"
    rospy.init_node('beacon_node', anonymous=True)
    bd = beacon_node()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Beacon Detector module"

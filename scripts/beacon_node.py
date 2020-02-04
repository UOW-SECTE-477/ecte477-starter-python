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
from sensor_msgs.msg import CompressedImage

class beacon_node:
    def __init__(self):
        self.subscriber = rospy.Subscriber('camera/colour/image_raw/compressed', CompressedImage, self.callback_colour_image)

    def callback_colour_image(self, data):
        # Do something
    
if __name__ == '__main__':
    print "Starting ROS Beacon Detector module"
    bd = beacon_node()
    rospy.init_node('beacon_node', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Beacon Detector module"
#!/usr/bin/env python
"""
    wall_follower_node.py

    A ROS node that commands a Turtlebot3 to follow a wall to its right
    according to the latest laser scan.

    Subscribed: scan/, cmd/
    Publishes: cmd_vel/

    Created: 2020/02/04
    Author: Brendan Halloran
"""

import rospy
import numpy as np 
import tf
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from enum import Enum

# Constants
BASE_FRAME =        "base_link"         # Param from the SLAM module
MAX_SIDE_LIMIT =    0.40                # This furthest distance we 'see' the wall to the side
MIN_APPROACH_DIST = 0.30                # The closest we want to get to a wall from the front
MAX_APPROACH_DIST = 0.50                # The distance we want to start slowing to approach a front wall
ROBOT_RADIUS =      0.17                # The bounding circle around the robot
MAX_TRANS_SPEED =   0.25                # Forward movement
MAX_TURN_SPEED =    1.8                 # Rotation

class FollowSide(Enum):
    LEFT = 1
    RIGHT = 2

class wall_follower_node:
    def __init__(self):
        self.stopped = False
        self.explore = True
        self.follow_side = FollowSide.LEFT

        self.transform_listener = tf.TransformListener()

        self.subscriber_laser_scan = rospy.Subscriber('scan/', LaserScan, self.callback_laser_scan)
        self.subscriber_command = rospy.Subscriber('cmd/', String, self.callback_command)
        self.publisher_twist = rospy.Publisher(cmd_vel, Twist, queue_size=1)

    # Send a find stop command before shutting off the node
    def shutdown(self):
        if not self.stopped:
            self.stopped = True
            self.explore = False
            vel_msg = Twist()
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            self.publisher_twist.publish(vel_msg)


    def callback_laser_scan(self, data):
        # If we are no longer exloring don't process the scan
        if not self.explore:
            # If we aren't exploring, but we haven't told the robot to stop, do so now
            if not self.stopped:
                self.stopped = True
                vel_msg = Twist()
                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
                self.publisher_twist.publish(vel_msg)
            return
        # Otherwise, process the scan.

        # Find the transform between the laser scanner and the centroid of the robot
        transform = tf.TransformStamped()
        try:
            self.transform_listener.waitForTransform(BASE_FRAME, data.header.frame_id, data.header.stamp, rospy.Duration(2.0))
            [position, quaternion] = self.transform_listener.lookupTransform(BASE_FRAME, data.header.frame_id, data.header.stamp)
        except tf.Exception:
            print "Unable to get transformation!"


        points = [None]*len(data.ranges)

    def callback_command(self, data):
        # Do something
    
if __name__ == '__main__':
    print "Starting ROS Wall Following module"
    wf = wall_follower_node()
    rospy.init_node('wall_follower_node', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Wall Following module"
    wf.shutdown()
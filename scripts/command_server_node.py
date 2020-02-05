#!/usr/bin/env python
"""
    command_server_node.py

    A ROS node that sends commands based on the current state of the 
    USAR problem. Explore, Return, Stop.

    Subscribed: 
    Publishes: cmd/

    Created: 2020/02/04
    Author: Brendan Halloran
"""

import rospy

class command_server_node:
    def __init__(self):
        # Do something

    def callback_state(self, data):
        # Do something
    
if __name__ == '__main__':
    print "Starting ROS Command Server module"
    cs = command_server_node()
    rospy.init_node('command_server_node', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Command Server module"
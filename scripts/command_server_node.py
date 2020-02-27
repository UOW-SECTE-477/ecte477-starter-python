#!/usr/bin/env python
"""
    command_server_node.py

    A ROS node that sends commands based on the current state of the 
    USAR problem. 

    Listens to the start and stop commands on the cmd/ topic. These can 
    be sent with:
    rostopic pub -1 /cmd std_msgs/String -- 'start'
    rostopic pub -1 /cmd std_msgs/String -- 'stop'

    Subscribed: cmd/
    Publishes:

    Created: 2020/02/04
    Author: Brendan Halloran
"""

import rospy

from commands import Commands, RobotState

class command_server_node:
    def __init__(self):
        self.subscriber_command = rospy.Subscriber('cmd/', String, self.callback_command)


    def callback_command(self, data):
        command = Commands(data.data)

        if command is Commands.START:
            # Do something
        elif command is Commands.STOP:
            # Do something
    
if __name__ == '__main__':
    print "Starting ROS Command Server module"
    cs = command_server_node()
    rospy.init_node('command_server_node', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Command Server module"
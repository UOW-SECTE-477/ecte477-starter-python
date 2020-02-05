"""
    commands.py

    Defines an Enum for valid commands to be sent over cmd/ topic

    Created: 2020/02/05
    Author: Brendan Halloran
"""

from enum import Enum

class  Commands(Enum):
    START = 'start'
    EXPLORE = 'explore'
    RETURN = 'return'
    HALT = 'halt'
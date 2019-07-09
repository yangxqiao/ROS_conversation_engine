#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import Float64MultiArray
import subprocess

def move_head(HeadYaw, HeadPitch):
    ref = Float64MultiArray()
    ref.data.append(HeadYaw)
    ref.data.append(HeadPitch)

    # head_pub.publish(ref)
    strmsg = "{}".format(ref)
    os.system('rostopic pub --once /qt_robot/head_position/command std_msgs/Float64MultiArray "'+strmsg+"\"")

if __name__ == '__main__':
    # rospy.init_node('moving_head_example', anonymous=True)
    # head_pub = rospy.Publisher('/qt_robot/head_position/command', std_msgs/Float64MultiArray, queue_size=1)

    try:
        move_head(2.0, -20.0)
        move_head(2.0, 25.0)
            # rospy.spin()
    except rospy.ROSInterruptException:
        pass
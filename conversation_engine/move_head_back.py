#!/usr/bin/env python
import rospy
from qt_motors_controller.srv import *

def move_head_back():
	home('HeadPitch')
	home('HeadYaw')

if __name__ == '__main__':
	rospy.init_node('move_head_back')
	move_back_head_pub = rospy.ServiceProxy('/qt_robot/motors/home', home)
	rospy.wait_for_service('/qt_robot/motors/home')
	rospy.loginfo("ready...")
   
    try:
        move_head_back()
        rospy.loginfo("finish.")
    except rospy.ROSInterruptException:
        pass
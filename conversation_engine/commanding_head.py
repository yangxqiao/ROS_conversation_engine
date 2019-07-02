#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

def move_head():
	ref = Float64MultiArray()
    HeadYaw = 10
    HeadPitch = 0
    ref.data = [HeadYaw, HeadPitch]
    head_pub.publish(ref)

if __name__ == '__main__':
    rospy.init_node('moving_head_example')
    
    # create pubisher
    head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)

    try:
        move_head()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

if __name__ == '__main__':
    rospy.init_node('moving_joints_example')
    right_pub = rospy.Publisher('/qt_robot/right_arm_position/command', Float64MultiArray, queue_size=1)
    ref = Float64MultiArray()
    RightShoulderPitch = 0
    RightShoulderRoll = 0
    RightElbowRoll = -10
    ref.data = [RightShoulderPitch ,RightShoulderRoll ,RightElbowRoll]
    right_pub.publish(ref)

    rospy.spin()

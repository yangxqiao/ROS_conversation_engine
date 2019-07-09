#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

if __name__ == '__main__':
    rospy.init_node('moving_joints_example')
    print("Initialize the node")
    right_pub = rospy.Publisher("/qt_robot/right_arm_position/command", Float64MultiArray, queue_size=1)
    ref = Float64MultiArray()
    RightShoulderPitch = 0.0
    RightShoulderRoll = 10.0
    RightElbowRoll = 10.0
    ref.data = [0, 10, 10]

    right_pub.publish(ref)
    print(ref)
    rospy.spin()

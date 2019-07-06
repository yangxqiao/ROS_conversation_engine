#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

if __name__ == '__main__':
    rospy.init_node('moving_joints_example')
    print("Initialize the node")
    right_pub = rospy.Publisher('/qt_robot/right_arm_position/command', Float64MultiArray, queue_size=10)
    # ref = Float64MultiArray()
    RightShoulderPitch = -10
    RightShoulderRoll = 0
    RightElbowRoll = 0
    # ref.data = [RightShoulderPitch, RightShoulderRoll, RightElbowRoll]
    ref = [RightShoulderPitch, RightShoulderRoll, RightElbowRoll]
    my_array_for_publishing = Float64MultiArray(data=ref)
    right_pub.publish(my_array_for_publishing)
    print(my_array_for_publishing.data)
    print(my_array_for_publishing.layout.dim)

rospy.spin()

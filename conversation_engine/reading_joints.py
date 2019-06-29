#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

def joint_states_callback(msg):
    strmsg = ""
    for i, joint_name in enumerate(msg.name):
        strmsg += "%s: %.2f, " % (joint_name, msg.position[i])
    rospy.loginfo(strmsg)

if __name__ == '__main__':
    rospy.init_node('joints_example')
    rospy.Subscriber('/qt_robot/joints/state', JointState, joint_states_callback)

rospy.spin()

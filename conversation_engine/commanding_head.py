#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

def move_head(HeadYaw, HeadPitch):
    ref = Float64MultiArray()
    ref.data.append(HeadYaw)
    ref.data.append(HeadPitch)
    # my_dict = {'label': '', 'size': 0, 'stride': 0}

    print(ref.layout.dim[0])

    print(type(ref.layout.dim))
    print(ref)

    head_pub.publish(ref)

if __name__ == '__main__':
    rospy.init_node('moving_head_example', anonymous=True)
    
    # create pubisher
    head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)

    try:
        move_head(2, 0)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
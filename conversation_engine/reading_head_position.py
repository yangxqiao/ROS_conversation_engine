#!/usr/bin/env python
import rospy
from qt_nuitrack_app.msg import Faces

def head_callback(msg):
    strmsg = "---------------------'\n'"
    for i in enumerate(msg.left_eye):
        strmsg += "left_eye: %.2f'\n'" % (msg.left_eye[i])
    for i in enumerate(msg.right_eye):
    	strmsg += "right_eye: %.2f'\n'" % (msg.right_eye[i])
    rospy.loginfo(strmsg)

if __name__ == '__main__':
    rospy.init_node('reading_head_example')

    # create subscriber
    rospy.Subscriber('/qt_nuitrack_app/faces', Faces, head_callback)

rospy.spin()
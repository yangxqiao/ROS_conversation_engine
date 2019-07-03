#!/usr/bin/env python
import rospy
from qt_nuitrack_app.msg import Faces

def head_callback(msg):
#    strmsg = "---------------------'\n'"
#    strmsg += "left_eye: %.2f'\n'" % (msg.faces.left_eye[0])
#    strmsg += "left_eye: %.2f'\n'" % (msg.faces.left_eye[1])
#    strmsg += "right_eye: %.2f'\n'" % (msg.faces.right_eye[0])
#    strmsg += "right_eye: %.2f'\n'" % (msg.faces.right_eye[1])
  	
    # rospy.loginfo(type(msg.faces))
    rospy.loginfo(msg.faces[0].left_eye)
    # rospy.loginfo(len(msg.faces))
    return True

def show_expression(file_path):
	gesturePlay_pub = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=10)
	gesturePlay_pub.publish(file_path)


if __name__ == '__main__':
    rospy.init_node('reading_head_example')
    print("Initialize the node")

    # create subscriber
    recognize_face = rospy.Subscriber('/qt_nuitrack_app/faces', Faces, head_callback)
    if recognize_face:
    	show_expression("QT/happy")
    	recognize_face = False

rospy.spin()

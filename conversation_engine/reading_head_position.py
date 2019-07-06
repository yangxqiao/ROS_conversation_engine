#!/usr/bin/env python
import rospy
from qt_nuitrack_app.msg import Faces
from std_msgs.msg import String

def head_callback(msg):
#    strmsg = "---------------------'\n'"
#    strmsg += "left_eye: %.2f'\n'" % (msg.faces.left_eye[0])
#    strmsg += "left_eye: %.2f'\n'" % (msg.faces.left_eye[1])
#    strmsg += "right_eye: %.2f'\n'" % (msg.faces.right_eye[0])
#    strmsg += "right_eye: %.2f'\n'" % (msg.faces.right_eye[1])
  	
    # rospy.loginfo(type(msg.faces))
    rospy.loginfo(msg.faces[0].left_eye)
    # rospy.loginfo(len(msg.faces))
    show_expression("QT/happy")
    play_gesture("QT/happy")
    print("---------------------")
    return msg.faces[0].left_eye

def show_expression(file_path):
	emotionShow_pub = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=1)
	emotionShow_pub.publish(file_path)

def play_gesture(file_path):
    gesturePlay_pub = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=1)
    gesturePlay_pub.publish(file_path)


if __name__ == '__main__':
    rospy.init_node('reading_head_example')
    print("Initialize the node")

    # create subscriber
    rospy.Subscriber('/qt_nuitrack_app/faces', Faces, head_callback)

rospy.spin()

#!/usr/bin/env python
import rospy
from qt_nuitrack_app.msg import Faces
from std_msgs.msg import String

class PositionInfo:
    def __init__(self):
        self.left_eye = [0.5, 0.5]
        self.right_eye = [0.5, 0.5]

    def get_left_eye(self):
        return self.left_eye

    def get_right_eye(self):
        return self.right_eye

    def set_left_eye(self, new_position):
        self.left_eye[0] = new_position[0]
        self.left_eye[0] = new_position[1]

    def set_right_eye(self, new_position):
        self.right_eye[0] = new_position[0]
        self.right_eye[1] = new_position[1]


def head_callback(msg):
    global count
    count = count + 1
    if count == 5:

        strmsg_left = "Left eye: (%.4f, %.4f)" % (msg.faces[0].left_eye[0], msg.faces[0].left_eye[1])
        strmsg_right = "Right eye: (%.4f, %.4f)" % (msg.faces[0].right_eye[0], msg.faces[0].right_eye[1])

        my_position.set_left_eye(msg.faces[0].left_eye)
        my_position.set_right_eye(msg.faces[0].right_eye)

        show_expression("QT/happy")
        play_gesture("QT/happy")
        
        rospy.loginfo(strmsg_left)
        rospy.loginfo(strmsg_right)

        print("---------------------")

        count = 0


def show_expression(file_path):
	emotionShow_pub = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=1)
	emotionShow_pub.publish(file_path)


def play_gesture(file_path):
    gesturePlay_pub = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=1)
    gesturePlay_pub.publish(file_path)


if __name__ == '__main__':
    rospy.init_node('reading_head_example')
    print("Initialize the node")

    count = 0
    my_position = PositionInfo()
    # create subscriber
    rospy.Subscriber('/qt_nuitrack_app/faces', Faces, head_callback)

rospy.spin()

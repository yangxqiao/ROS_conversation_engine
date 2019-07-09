#!/usr/bin/env python
import rospy
from qt_nuitrack_app.msg import Faces
from std_msgs.msg import String

class PositionInfo:
    def __init__(self):
        self.coordinate_x = 0.5
        self.coordinate_y = 0.5

    def get_coordinate_x(self):
        return self.coordinate_x

    def get_coordinate_y(self):
        return self.coordinate_y

    def set_coordinate_x(self, new_position):
        self.coordinate_x = (new_position[0] + new_position[1]) / 2

    def set_coordinate_y(self, new_position):
        self.coordinate_y = (new_position[0] + new_position[1]) / 2


def head_callback(msg):
    global count
    count = count + 1
    if count == 5:

        strmsg_left = "Left eye: (%.4f, %.4f)" % (msg.faces[0].left_eye[0], msg.faces[0].left_eye[1])
        strmsg_right = "Right eye: (%.4f, %.4f)" % (msg.faces[0].right_eye[0], msg.faces[0].right_eye[1])

        my_position.set_coordinate_x([msg.faces[0].left_eye[0], msg.faces[0].right_eye[0]])
        my_position.set_coordinate_y([msg.faces[0].left_eye[0], msg.faces[0].right_eye[1]])

        strmsg_x = "The coordinate_x of the head: %.4f" % my_position.get_coordinate_x()
        strmsg_y = "The coordinate_y of the head: %.4f" % my_position.get_coordinate_y()

        show_expression("QT/happy")
        play_gesture("QT/happy")
        
        rospy.loginfo(strmsg_x)
        rospy.loginfo(strmsg_y)

        print("-----------------------------------------")

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

    print("Finish subscribing to the topic.")

rospy.spin()
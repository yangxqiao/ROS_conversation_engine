#!/usr/bin/env python
import rospy
import numpy as np
from qt_nuitrack_app.msg import Faces
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray


class PositionInfo:
    def __init__(self):
        self.coordinate_x = 0.5
        self.coordinate_y = 0.5
        self.current_head_pos = np.array([0, 0])
        self.step_size = 10
        self.threshold = 1e-6

    def get_coordinate_x(self):
        return self.coordinate_x

    def get_coordinate_y(self):
        return self.coordinate_y

    def set_coordinate_x(self, new_position):
        self.coordinate_x = (new_position[0] + new_position[1]) / 2

    def set_coordinate_y(self, new_position):
        self.coordinate_y = (new_position[0] + new_position[1]) / 2

    def process_new_head_position(self):
        desired_face_location = np.array([0.5, 0.5])
        actual_face_location = np.array([self.coordinate_x, self.coordinate_y])

        diff_face_loc = desired_face_location - actual_face_location
        if abs(diff_face_loc[0]) > self.threshold and abs(diff_face_loc[1]) > self.threshold:
            self.current_head_pos[0] += self.step_size * diff_face_loc[0]
            self.current_head_pos[1] -= self.step_size * diff_face_loc[1]

        print("diff_face_loc:")
        print(diff_face_loc)
        print("actual_face_location:")
        print(actual_face_location)
        print("current_head_pos")
        print(self.current_head_pos)
        
        publish_data = self.current_head_pos
        if self.current_head_pos[0] > 45: 
            publish_data[0] = 45
        elif self.current_head_pos[0] < -45:
            publish_data[0] = -45
        if self.current_head_pos[1] > 20:
            publish_data[1] = 20
        elif self.current_head_pos[1] < -20:
            self.current_head_pos[1] = -20
        head_pub.publish(Float64MultiArray(data=publish_data))

        # HeadYaw = 90*(1-self.get_coordinate_x())-45 + self.absolute_x
        # HeadPitch = 30*(self.get_coordinate_x()-1)+15 + self.absolute_y
        # self.absolute_x = HeadYaw 
        # self.absolute_y = HeadPitch 

        # print("[HeadYaw, HeadPitch]")
        # print([90*(1-self.coordinate_x)-45, 30*(self.coordinate_y-1)+15])
        # print("Absolute position")
        # print([self.absolute_x, self.absolute_y])

        # self.publish_head_position(HeadYaw, HeadPitch)

    # def publish_head_position(self, HeadYaw, HeadPitch):
    #     head = [HeadYaw, HeadPitch]
    #     head_pub.publish(Float64MultiArray(data=head))


def callback(msg):

    strmsg_left = "Left eye: (%.4f, %.4f)" % (msg.faces[0].left_eye[0], msg.faces[0].left_eye[1])
    strmsg_right = "Right eye: (%.4f, %.4f)" % (msg.faces[0].right_eye[0], msg.faces[0].right_eye[1])

    my_position.set_coordinate_x([msg.faces[0].left_eye[0], msg.faces[0].right_eye[0]])
    my_position.set_coordinate_y([msg.faces[0].left_eye[0], msg.faces[0].right_eye[1]])

    strmsg_x = "The coordinate_x of the head: %.4f" % my_position.get_coordinate_x()
    strmsg_y = "The coordinate_y of the head: %.4f" % my_position.get_coordinate_y()

    # show_expression("QT/happy")
    # play_gesture("QT/happy")
    
    rospy.loginfo(strmsg_x)
    rospy.loginfo(strmsg_y)
    my_position.process_new_head_position()
    print("---------------------------------------------------")


def show_expression(file_path):
    emotionShow_pub = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=1)
    emotionShow_pub.publish(file_path)


def play_gesture(file_path):
    gesturePlay_pub = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=1)
    gesturePlay_pub.publish(file_path)


if __name__ == '__main__':
    rospy.init_node('joints_command_example')
    head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)

    # wait for publisher/subscriber connections
    wtime_begin = rospy.get_time()
    while (head_pub.get_num_connections() == 0) :
        rospy.loginfo("waiting for subscriber connections")
        if rospy.get_time() - wtime_begin > 10.0:
            rospy.logerr("Timeout while waiting for subscribers connection!")
            sys.exit()
        rospy.sleep(1)
    
    rate = rospy.Rate(0.5) 
    count = 0
    my_position = PositionInfo()   

    rospy.loginfo("publishing motor commnad...")
    try:    
        rospy.Subscriber('/qt_nuitrack_app/faces', Faces, callback)

    except rospy.ROSInterruptException:
        rospy.logerr("could not publish motor commnad!")   

    rospy.spin()
    rate.sleep()
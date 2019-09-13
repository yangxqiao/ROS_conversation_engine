import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Bool


class StatusInfo:
	def __init__(self):
		self.is_speaking = False
		self.human_pos_x = 0.5
		self.human_pos_y = 0.5

	def set_is_speaking(is_speaking):
		self.is_speaking = is_speaking

	def update_human_head_pos(pos_x, pos_y):
		self.human_pos_x = pos_x
		self.human_pos_y = pos_y

	def process_new_head_position(self):
        desired_face_location = np.array([0.5, 0.5])
        actual_face_location = np.array([self.coordinate_x, self.coordinate_y])

        diff_face_loc = desired_face_location - actual_face_location
        if abs(diff_face_loc[0]) > self.threshold and abs(diff_face_loc[1]) > self.threshold:
            self.current_head_pos[0] += self.step_size * diff_face_loc[0]
            self.current_head_pos[1] -= self.step_size * diff_face_loc[1]
        
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


def is_speaking_callback(msg):
		QT_status_info.set_is_speaking(msg.data)

def my_head_position_callback(msg):
	pos_x = (msg.faces[0].left_eye[0] + msg.faces[0].right_eye[0]) * 0.5
	pos_y = (msg.faces[0].left_eye[1] + msg.faces[0].right_eye[1]) * 0.5
	QT_status_info.update_human_head_pos(pos_x, pos_y)
	

def publish_angle_to_QT_head_motor:

	# finite state machine for publishing the correct angle
	# Requirement:
	# Not totally predictable/ random
	# Using establish design choices
	# Defferentiate between speaking and listening
	while not rospy.is_shutdown():
		# start timing
		# case I: QT is speaking
		if QT_status_info.is_speaking:
			# perform Intimacy-modulating gaze aversions
			# Length: M = 1.14s, SD = 0.27s
			# Time between consecutive gaze aversions: M = 7.21s, SD = 1.88s
			# What we need: 
				# QT's current head position
				# pick an abosolute angle and call the process_new_head_position


			# perform gaze tracing


		# case II: QT is listening
		else:
			# perform floor management gaze aversions
			# Length: M = 2.3s, SD = 1.1s
			# Start time in relation to the start of the next utterance: M = -1.03s, SD = 0.39s


			# perform Intimacy-modulating gaze aversions
			# Length: M = 1.96s, SD = 0.32s
			# Time between consecutive gaze aversions: M = 4.75s, SD = 1.39s



if __name__ == '__main__':
	rospy.init_node('gaze_behavior_controller')
	# create the publisher
	qtHeadMotor_pub = rospy.Publisher('/qt_robot/head_position/command', 
		Float64MultiArray, 
		queue_size=1)

	# wait for publisher/subscriber connections
    wtime_begin = rospy.get_time()
    while (head_pub.get_num_connections() == 0) :
        rospy.loginfo("waiting for subscriber connections")
        if rospy.get_time() - wtime_begin > 10.0:
            rospy.logerr("Timeout while waiting for subscribers connection!")
            sys.exit()
        rospy.sleep(1)
    

	rospy.loginfo("ready...")    
    try:    
    	# create two subscribers
    	QT_status_info = StatusInfo()
    	rospy.Subscriber('speaker', Bool, is_speaking_callback)
    	rospy.Subscriber('/qt_nuitrack_app/faces', Faces, my_head_position_callback)
    	# do I need another subscriber to read the current head position of QT
    	# publishing data to QT head motor
    	publish_angle_to_QT_head_motor()
    except rospy.ROSInterruptException:
        rospy.logerr("could not successfully subscribe!")   

    rospy.spin()
    rate.sleep()


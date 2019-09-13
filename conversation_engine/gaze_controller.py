import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Bool
from sensor_msgs import JointState


class StatusInfo:
	def __init__(self):
		self._is_speaking = False
		self._human_pos_x = 0.5
		self._human_pos_y = 0.5
		self._robot_head_pitch = 0
		self._robot_head_yaw = 0

	def set_is_speaking(self, msg):
		self._is_speaking = msg.data

	def set_skeleton(self, msg):
		self._human_pos_x = (msg.faces[0].left_eye[0] + msg.faces[0].right_eye[0]) * 0.5
		self._human_pos_y = (msg.faces[0].left_eye[1] + msg.faces[0].right_eye[1]) * 0.5

	def set_sensor_msg(self, msg):
		self._robot_head_pitch = msg.position[0]
		self._robot_head_yaw = msg.position[1]

	@property
	def human_pos_x(self):
		return self._human_pos_x
	
	@property
	def human_pos_y(self):
		return self._human_pos_y
	
	@property
	def is_speaking(self):
		return self._is_speaking

	@property
	def robot_head_pitch(self):
		return self._robot_head_pitch

	@property
	def robot_head_Yaw(self):
		return self._robot_head_Yaw

	def run(msg):
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
					# pick an absolute angle and call the process_new_head_position()


				# perform gaze tracing
				pass

			# case II: QT is listening
			else:
				# perform floor management gaze aversions
				# Length: M = 2.3s, SD = 1.1s
				# Start time in relation to the start of the next utterance: M = -1.03s, SD = 0.39s


				# perform Intimacy-modulating gaze aversions
				# Length: M = 1.96s, SD = 0.32s
				# Time between consecutive gaze aversions: M = 4.75s, SD = 1.39s
				pass
	

if __name__ == '__main__':
	rospy.init_node('gaze_behavior_controller')
	# create the publisher
	qtHeadMotor_pub = rospy.Publisher('/qt_robot/head_position/command', 
		Float64MultiArray, 
		queue_size=1)

    # create three subscribers
	QT_status_info = StatusInfo()
	rospy.Subscriber('speaker', Bool, QT_status_info.set_is_speaking)
	rospy.Subscriber('/qt_nuitrack_app/faces', Faces, QT_status_info.set_skeleton)
	rospy.Subscriber('/qt_robot/joints/state', JointState, QT_status_info.set_sensor_msg)

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
    	QT_status_info.run()
    except rospy.ROSInterruptException:
        rospy.logerr("could not successfully subscribe!")   

    rospy.spin()
    rate.sleep()


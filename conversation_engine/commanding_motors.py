#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

if __name__ == '__main__':
    rospy.init_node('joints_command_example')
    
    # create a publisher
    head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)
    right_pub = rospy.Publisher('/qt_robot/right_arm_position/command', Float64MultiArray, queue_size=1)
    left_pub = rospy.Publisher('/qt_robot/left_arm_position/command', Float64MultiArray, queue_size=1)

    # wait for publisher/subscriber connections
    wtime_begin = rospy.get_time()
    while (right_pub.get_num_connections() == 0) :
        rospy.loginfo("waiting for subscriber connections")
        if rospy.get_time() - wtime_begin > 10.0:
            rospy.logerr("Timeout while waiting for subscribers connection!")
            sys.exit()
        rospy.sleep(1)
        

    rate = rospy.Rate(0.5) 
    toggle = False
    while not rospy.is_shutdown():
        rospy.loginfo("publishing motor commnad...")
        try:    
            if toggle:
                head = [20 ,0]
                rarm = [90 ,0 , -70]
                larm = [-90 ,0 , -70]
            else:
                head = [-20 ,0]
                rarm = [90 ,0 , -10]
                larm = [-90 ,0 , -10]
                    
            head_pub.publish(Float64MultiArray(data=head))
            right_pub.publish(Float64MultiArray(data=rarm))
            left_pub.publish(Float64MultiArray(data=larm))
            toggle = not toggle
        except rospy.ROSInterruptException:
            rospy.logerr("could not publish motor commnad!")        
       
        rate.sleep()
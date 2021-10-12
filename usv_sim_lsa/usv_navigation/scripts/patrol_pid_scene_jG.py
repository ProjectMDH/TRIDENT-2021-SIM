#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist, Point, Quaternion
from std_srvs.srv import Empty
import rosbag
import subprocess
import os

waypoints = [
    #[(440.0, 135.0, 0.0), (0.0, 0.0, 0.0, 1.0)],
    [(446.0, 124.5, 0.0), (0.0, 0.0, 0.0, 1.0)],    
    [(469.0, 122.5, 0.0), (0.0, 0.0, 0.0, 1.0)],
    [(475.0, 111.0, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(465.0, 103.0, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(446.0, 104, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(440.0, 110.0, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(446.0, 119.0, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(469.0, 117.5, 0.0), (0.0, 0.0, 0.0, 1.0)],

    [(468.0, 98.0, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(446.0, 99.0, 0.0), (0.0, 0.0, 0.63, 0.78)],
    [(433.0, 145.0, 0.0), (0.0, 0.0, 0.63, 0.78)]
]

result = Float64()
result.data = 0
x_offset = 0 
y_offset = 0
maxSimulations = 1

def goal_pose(pose):
    goal_pose = Odometry()
    goal_pose.header.stamp = rospy.Time.now()
    goal_pose.header.frame_id = 'world'
    goal_pose.pose.pose.position = Point(pose[0][0]+x_offset, pose[0][1]+y_offset, 0.)
    return goal_pose

def get_result(result_aux):
    global result
    result.data = result_aux.data

if __name__ == '__main__':
    pub = rospy.Publisher('move_usv/goal', Odometry, queue_size=10)
    rospy.init_node('patrol')
    rate = rospy.Rate(1) # 10h
    rospy.Subscriber("move_usv/result", Float64, get_result)
    rospy.wait_for_service('/gazebo/unpause_physics')
    rospy.wait_for_service('/gazebo/pause_physics')
    rospy.wait_for_service('/gazebo/reset_simulation')
    unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
    pause = rospy.ServiceProxy('/gazebo/pause_physics', Empty)
    resetSimulation = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
    #unpause()


    simulationNumber = 1
    while not rospy.is_shutdown():    
        try:
	    rospy.logerr("Simulation number %d", simulationNumber)
            for pose in waypoints:
                goal = goal_pose(pose)
                pub.publish(goal)
                rate.sleep()
		if (rospy.get_time() > 12 *60):
			break;
                while result.data == 0.0:
                    pub.publish(goal)
                    rate.sleep()
		    if (rospy.get_time() > 12 *60):
			break;
            simulationNumber = simulationNumber + 1
            if (simulationNumber > maxSimulations):
		rospy.logerr("All simulations have been done. Pausing gazebo")
                pause() 
	    else:
                resetSimulation()
                rate.sleep()
        except rospy.ROSInterruptException:
	    rospy.logerr("ROS InterruptException! Just ignore the exception!") 
        except rospy.ROSTimeMovedBackwardsException:
	    rospy.logerr("ROS Time Backwards! Just ignore the exception!")


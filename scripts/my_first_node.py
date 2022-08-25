#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
  rospy.init_node("test_node_py")
  
  rospy.loginfo("Test node has been started.")
  
  rate = rospy.Rate(4)
  
  while not rospy.is_shutdown():
    rospy.loginfo("Hello")
    rate.sleep()
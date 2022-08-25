#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg: Pose):
  rospy.loginfo("(" + str(msg.x) + ", " + str(msg.y) + ")")


if __name__ == '__main__':
  rospy.init_node("pose_subscriber_py")
  
  sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
  
  rospy.loginfo("Test node has been started.")

  rospy.spin()
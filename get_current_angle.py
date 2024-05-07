# 現在のアームの関節角度を取得

import rospy
import numpy as np
from moveit_commander import RobotCommander, MoveGroupCommander

rospy.init_node("xArm6")
robot = RobotCommander()
xarm = MoveGroupCommander("xarm6")

flag = input("Enter e key if you use \"e\" notation, or other key if you don't. >> ")
if (flag == "e"):
    current_joint_values = xarm.get_current_joint_values()
    current_joint_values_np = np.array(current_joint_values)
    np.set_printoptions(suppress=True) # e表記を無効にする
    print("Current joint values:")
    print(current_joint_values_np)

else:
    current_joint_values = xarm.get_current_joint_values()
    print("Current joint values:")
    print(current_joint_values)
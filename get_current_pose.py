# 現在のアームの座標を取得

import rospy
from moveit_commander import RobotCommander, MoveGroupCommander

rospy.init_node("get_current_pose")
robot = RobotCommander()
xarm = MoveGroupCommander("xarm6")

current_pose = xarm.get_current_pose().pose
x = current_pose.position.x
y = current_pose.position.y
z = current_pose.position.z
ox = current_pose.orientation.x
oy = current_pose.orientation.y
oz = current_pose.orientation.z
w = current_pose.orientation.w

print("Current Pose:")
print(f"(x, y, z, ox, oy, oz, w) = ({x}, {y}, {z}, {ox}, {oy}, {oz}, {w})")
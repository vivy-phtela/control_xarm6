import rospy
from moveit_commander import RobotCommander, MoveGroupCommander

rospy.init_node("xArm6")
robot = RobotCommander()
xarm = MoveGroupCommander("xarm6")

# ゴールの設定(関節角度で指定)
fixed_joint_values = [0.9704946662267524, -0.5775184827066822, -0.9503822306458227, 0.00010799484719203889, 1.5279174894136958, 0.9704959568637523]

xarm.set_start_state_to_current_state()
xarm.set_joint_value_target(fixed_joint_values)

# プランニング
success, plan, _, _ = xarm.plan()

if success:
    xarm.execute(plan)
else:
    print("Planning failed.")
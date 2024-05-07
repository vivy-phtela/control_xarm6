# 任意の複数のウェイポイントを通過する(プランニングなし)

import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('xArm6')

joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']

# ウェイポイント
waypoints = [
    [0.14874049993137733, 0.22356793296788185, -0.7956666059443569, 0.5287485195619754, 0.3572557926068257, 0.7309218850089781],
    [0.16527193520395222, 0.24840584099393878, -0.8840718069955558, 0.5875005234134539, 0.39695198861565256, 0.8121346582244002],
    [0.19833480574910178, 0.2980816570460525, -1.0608822090979535, 0.7050045311164104, 0.47634438063330636, 0.9745602046552441],
    [0.21486624102167684, 0.32291956507210956, -1.1492874101491528, 0.7637565349678889, 0.5160405766421333, 1.0557729778706662],
    [0.5661783371443472, 0.578120219992803, -1.8919463153712992, 1.3066922692642677, 1.016341391899957, 1.7623516494016698],
    [1.230512663389329, 0.7221678276857286, -1.8786401830931072, 0.4356886782819483, 1.1895469922286355, 1.4920525620716105],
    [1.2628288202980198, 0.7266039457240783, -1.8666200793926353, 0.29042539286031616, 1.1620817216506727, 1.43718798222228],
    [1.295144977206711, 0.731040063762428, -1.8545999756921632, 0.14516210743868446, 1.1346164510727101, 1.382323402372949]
]


trajectory = JointTrajectory()
trajectory.joint_names = joint_names

for i, positions in enumerate(waypoints):
    point = JointTrajectoryPoint()
    point.positions = positions
    point.time_from_start = rospy.Duration(0.2*i) # 各ウェイポイントにどのくらいの時間に到達するか(現在は0.2秒ごとに到達するようにしている)
    trajectory.points.append(point)

client = actionlib.SimpleActionClient('/xarm/xarm6_traj_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
client.wait_for_server()

goal = FollowJointTrajectoryGoal()
goal.trajectory = trajectory

client.send_goal(goal)
client.wait_for_result()

result = client.get_result()
if result.error_code == result.SUCCESSFUL:
    print("successful!")
else:
    print("failed!")
# グリッパーの開閉

import sys
import rospy
import moveit_commander

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('gripper_control', anonymous=True)
    gripper_group_name = "xarm_gripper"
    gripper_group = moveit_commander.MoveGroupCommander(gripper_group_name)


    for i in range(5):
        # グリッパーを閉じる
        open_position = 0.0
        gripper_group.set_joint_value_target({'drive_joint': open_position})
        gripper_group.go(wait=True)
        gripper_group.stop()

        rospy.sleep(1)

        # グリッパーを開く
        close_position = 0.7
        gripper_group.set_joint_value_target({'drive_joint': close_position})
        gripper_group.go(wait=True)
        gripper_group.stop()

if __name__ == '__main__':
    main()
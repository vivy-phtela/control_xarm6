import sys

import time

import datetime

import threading


from xarm import version

from xarm.wrapper import XArmAPI

print('xArm-Python-SDK Version:{}'.format(version.__version__))


arm = XArmAPI('192.168.1.195')

arm.clean_warn()

arm.clean_error()

arm.motion_enable(True)

arm.set_mode(0)

arm.set_state(0)

time.sleep(1)


arm.set_position(*[425.9, 0.0, 678.8, 180.0, 0.0, 0.0], speed=200, mvacc=20000, radius=-1.0, wait=True)

arm.set_position(*[430.4, 0.0, 389.7, 180.0, -1.2, 0.1], speed=200, mvacc=20000, radius=-1.0,wait=True)

arm.set_suction_cup(True, False)


for i in range(int(6)):

    if arm.get_suction_cup()[1] == 1:
        break

    time.sleep(0.5)


    if arm.get_suction_cup()[1] == 1:

        arm.set_servo_angle(angle=[97.8, -23.9, -93.9, 0.0, 116.1, 0.0],speed=20,  mvacc=500,wait=True)

        arm.set_position(*[-36.9, 344.5, 471.8, 180.0, -1.7, 97.8], speed=200,mvacc=20000, radius=-1.0, wait=True)

        arm.set_suction_cup(False, False)

        arm.set_position(*[425.9, 0.0, 678.8, 180.0, 0.0, 0.0], speed=200,mvacc=20000, radius=-1.0, wait=True)

    else:
        arm.set_servo_angle(angle=[-81.9, -23.9, -93.9, 0.0, 116.1, 0.0],speed=20, mvacc=500, wait=True)
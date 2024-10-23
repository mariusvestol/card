#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
#Create a robotic arm object
Arm = Arm_Device()
time.sleep(.1)


for i in range(90):
	Arm.Arm_serial_servo_write(4, 180-i, 500)
	time.sleep(.01)
	Arm.Arm_serial_servo_write(3, 0+i, 500)
	time.sleep(.01)

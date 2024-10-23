#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
import math
#Create a robotic arm object
Arm = Arm_Device()
time.sleep(.1)


def degtorad(vinkel_i_radianer):
	return vinkel_i_radianer*((2*math.pi)/360)

def deg(r):
	return r*360/2/math.pi

a = 36
b = deg(math.acos(math.sin(degtorad(a))-10/8.5)-degtorad(a))
c = 180-(a+b)


print(deg(b))

Arm.Arm_serial_servo_write(4, c, 500)
time.sleep(.2)

Arm.Arm_serial_servo_write(2, a, 500)
time.sleep(0.2)
Arm.Arm_serial_servo_write(3, b, 500)
time.sleep(.2)

Arm.Arm_serial_servo_write(1, 180, 500)
time.sleep(.2)
time.sleep(2)

for i in range(100):
	a+=1
	b = deg(math.acos(math.sin(degtorad(a))-10/8.5)-degtorad(a))
	c = 180-(a+b)
	Arm.Arm_serial_servo_write(2, a, 500)
	time.sleep(0.01)
	Arm.Arm_serial_servo_write(3, b, 500)
	time.sleep(0.01)
	Arm.Arm_serial_servo_write(4, c, 500)
	time.sleep(0.01)


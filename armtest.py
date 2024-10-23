#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
import math
#Create a robotic arm object
Arm = Arm_Device()
time.sleep(.1)

#Arm.Arm_serial_servo_write(6, 168, 500)

#ARMEN ER INNTIL KORTLESEREN PÅ a=153 GRADER, IKKE GÅ NÆRMERE


def degtorad(vinkel_i_radianer):
	return vinkel_i_radianer*((2*math.pi)/360)

def deg(r):
	return r*360/2/math.pi

a = 140

print(deg(math.acos(math.sin(degtorad(a))-10/8.5)-degtorad(a)))
"""
c = 180-(a+b)

Arm.Arm_serial_servo_write(1, 90, 500)

print(deg(b))

Arm.Arm_serial_servo_write(4, c, 500)
time.sleep(1)

Arm.Arm_serial_servo_write(2, a, 500)
time.sleep(1)
Arm.Arm_serial_servo_write(3, b, 500)
time.sleep(2)

Arm.Arm_serial_servo_write(1, 90, 500)
time.sleep(.2)
time.sleep(2)

"""

grader_test=30


time.sleep(1)


for y in range(5):
	grader_test-=1

	for i in range(grader_test):
		a-=1
		b = deg(math.acos(math.sin(degtorad(a))-10/8.5)-degtorad(a))
		c = 180-(a+b)
		Arm.Arm_serial_servo_write(2, a, 500)
		time.sleep(0.001)
		Arm.Arm_serial_servo_write(3, b, 500)
		time.sleep(0.001)
		Arm.Arm_serial_servo_write(4, c, 500)
		time.sleep(0.001)
		
	print(a)

	time.sleep(1)

	for i in range(grader_test):
		a+=1
		b = deg(math.acos(math.sin(degtorad(a))-10/8.5)-degtorad(a))
		c = 180-(a+b)
		Arm.Arm_serial_servo_write(2, a, 500)
		time.sleep(0.001)
		Arm.Arm_serial_servo_write(3, b, 500)
		time.sleep(0.001)
		Arm.Arm_serial_servo_write(4, c, 500)
		time.sleep(0.001)

	time.sleep(4)


	





import time
from Arm_Lib import Arm_Device
import math

class Arm():
	
	def __init__(self):
		self.arm = Arm_Device()
		self.cards = [120]
		#self.distance = {105: 15, 106: 16, 107: 1.7, 108: 1.9, 109: 2.15, 110: 2.3, 111: 2.4, 112: 2.5}
	
	def startposition(self):
		self.arm.Arm_serial_servo_write(1, 90, 500)
		time.sleep(.1)
		self.arm.Arm_serial_servo_write(2, 135, 500)
		time.sleep(.1)
		self.arm.Arm_serial_servo_write(3, -10, 500)
		time.sleep(.1)
		self.arm.Arm_serial_servo_write(4, 45, 500)
		time.sleep(1)
		
	def open(self):
		self.arm.Arm_serial_servo_write(6, 0, 500)
		time.sleep(1)
		
	def close(self):
		self.arm.Arm_serial_servo_write(6, 170, 500)
		time.sleep(1)
		
	def getCard(self, card):
		self.arm.Arm_serial_servo_write(1, card, 500)
		time.sleep(.1)
		self.arm.Arm_serial_servo_write(2, 78, 500)
		time.sleep(.1)
		self.arm.Arm_serial_servo_write(3, 0, 500)
		time.sleep(.1)	
		self.arm.Arm_serial_servo_write(4, 7, 500)
		time.sleep(1)
		
	def reload(self, card):
		self.startposition()
		self.open()
		self.getCard(card)
		self.close()
		self.startposition()
	
	def degtorad(self, deg):
		return deg*((2*math.pi)/360)

	def deg(self, radians):
		return radians*360/2/math.pi

	def testCard(self, degrees):
		a = 135
		for i in range(degrees):
			a-=1
			b = self.deg(math.acos(math.sin(self.degtorad(a))-10/8.5)-self.degtorad(a)) + 16  # legger til 16 grader i høyde
			c = 180-(a+b)
			
			self.arm.Arm_serial_servo_write(2, a, 500)
			time.sleep(0.0000001)
			self.arm.Arm_serial_servo_write(3, b, 500)
			time.sleep(0.0000001)
			self.arm.Arm_serial_servo_write(4, c, 500)
			time.sleep(0.0000001)

		print(a)		
		time.sleep(1.5)

		for i in range(degrees):
			a+=1
			b = self.deg(math.acos(math.sin(self.degtorad(a))-10/8.5)-self.degtorad(a)) + 16
			c = 180-(a+b)
			self.arm.Arm_serial_servo_write(2, a, 500)
			time.sleep(0.0000001)
			self.arm.Arm_serial_servo_write(3, b, 500)
			time.sleep(0.000001)
			self.arm.Arm_serial_servo_write(4, c, 500)
			time.sleep(0.0000001)

		time.sleep(4)

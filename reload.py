import time
from Arm_Lib import Arm_Device
import math


Arm = Arm_Device()
time.sleep(.1)

#Arm.Arm_serial_servo_write(6, 0, 500)
time.sleep(.1)

def startposition():
	Arm.Arm_serial_servo_write(1, 90, 500)
	time.sleep(.1)
	Arm.Arm_serial_servo_write(2, 135, 500)
	time.sleep(.1)
	Arm.Arm_serial_servo_write(3, -10, 500)
	time.sleep(.1)
	Arm.Arm_serial_servo_write(4, 45, 500)
	time.sleep(1)



startposition()

def neger(pos1, pos2):
	Arm.Arm_serial_servo_write(1, pos1, 500)
	time.sleep(.1)
	Arm.Arm_serial_servo_write(2, 78, 500)
	time.sleep(.1)
	Arm.Arm_serial_servo_write(3, 0, 500)
	time.sleep(.1)	
	Arm.Arm_serial_servo_write(4, 7, 500)
	time.sleep(1)
	Arm.Arm_serial_servo_write(6, pos2, 500)
	time.sleep(1)

#120 55 



startposition()
neger(195, 0)
startposition()
neger(195, 170)
neger(-20, 0)
startposition()
neger(-20, 170)
neger(120, 0)
startposition()
neger(120, 170)
neger(55, 170)
startposition()


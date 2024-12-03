import time
from Arm_Lib import Arm_Device
import math


Arm = Arm_Device()
time.sleep(.1)


def startposition():
	pass

Arm.Arm_serial_servo_write(2, 100, 500)
time.sleep(0.001)

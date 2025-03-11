from UserInterface import UserInterface
from Arm import Arm
import threading

arm = Arm()
test = UserInterface(arm)
test.mainloop()


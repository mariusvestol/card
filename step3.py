import gpiozero as GPIO
import tkinter as tk
import time
import threading

c = 0

root = tk.Tk()


led = GPIO.LED(18)
drc = GPIO.LED(23)

liste = []


def changeDrc():
	global c
	liste.append(c)
	c = 0
	if drc.is_lit:
		drc.off()
	else:
		drc.on()

def newcc():
	if drc.is_lit:
		drc.off()
	else:
		drc.on()

def double():
	for e in liste:
		for i in range(e):
			led.on()
			time.sleep(0.0000001)
			led.off()
			time.sleep(0.0000001)
		newcc()

def test(i):
	global c
	for p in range(i):
		led.on()
		time.sleep(0.0000001)
		led.off()
		c += 1
		time.sleep(0.0000001)
	print(sum(liste))
	print(liste)

button = tk.Button(root, text="press me!", command = changeDrc)
button.pack()

threading.Thread(target=lambda: test(128000)).start()
#test(128000)


newb = tk.Button(root, text="sameRound", command = double)
newb.pack()

root.mainloop()

#if GPIO.input(pin)

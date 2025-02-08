import tkinter as tk
import pickle
import time
from Arm_Lib import Arm_Device
import math
import threading
#Create a robotic arm object
Arm = Arm_Device()
time.sleep(.1)

#Arm.Arm_serial_servo_write(6, 168, 500)

#ARMEN ER INNTIL KORTLESEREN PÅ a=153 GRADER, IKKE GÅ NÆRMERE


"""

Kortet må høyere, gå raskere, lenger bak
Integrere mediapipe for bedre håndtering av kamera
Finne ulike avstander 


"""


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

Arm.Arm_serial_servo_write(6, 170, 500)

grader_test=30


time.sleep(1)


def testarm():
    global grader_test, a
    for y in range(8):
        grader_test+=1

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
        print(7.4+(8.5*math.cos(degtorad(b-a-90))-8.5*math.cos(degtorad(a))))
        push()
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


	






label_texts = []

def reInfo(li):
    global infoLabel
    infoLabel.config(text=f"""
Navn:                  {li[0]}
                
Avstand:             {li[1]}
                      
Tid:                     {li[2]}     
                   
Antall forsøk:      {li[3]}                 
                """)

def save(db, file):
    f = open(file, "wb")
    pickle.dump(db, f)
    f.close()
    return

def loadd(file):
    f = open(file, "rb")
    out = pickle.load(f)
    f.close()
    return out

db = loadd("db.txt")


def refreshLabel(db):
    global label_texts
    label_texts = []
    for x in db:
        label_texts.append(x)

def deleteLabel(name):
    global db
    del db[name]
    print(db)
    refreshData()


def refreshData():
    global scrollFrame, db
    for widget in scrollFrame.winfo_children():
        widget.destroy()
    save(db, "db.txt")
    db = loadd("db.txt")
    refreshLabel(db)
    check()
    return


def check():
    for text in label_texts:
        frame = tk.Frame(scrollFrame, borderwidth=1, pady=5, relief="solid")
        label1 = tk.Label(frame,text=text, width=25, anchor="w")
        label2 = tk.Label(frame, text="X")
        # relief for synlig kant
        label2.bind("<Button-1>", lambda e, text=text: deleteLabel(text))
        label1.bind("<Button-1>", lambda e, text=text: reInfo(db[text]))
        frame.pack(anchor="w")
        label1.grid(column=0, row=0)
        label2.grid(column=1, row=0)


root = tk.Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

cardDisplay = tk.Frame(root)

dispCanvas = tk.Canvas(cardDisplay)
scrollBar = tk.Scrollbar(cardDisplay, orient="vertical", command=dispCanvas.yview)
scrollFrame = tk.Frame(dispCanvas)

scrollFrame.bind("<Configure>", lambda e: dispCanvas.configure(scrollregion=dispCanvas.bbox("all")))

#denne linjen har jeg ikke sett på
window = dispCanvas.create_window((0, 0), window=scrollFrame, anchor="nw")

#må legge til attribute senere fordi scollbar fantes ikke
dispCanvas.configure(yscrollcommand=scrollBar.set)

# lambda e - der e bare er navnet på parameteren som har mye info vi ser etter

#root.bind("<Configure>", lambda e: cardDisplay.config(height=root.winfo_height()//2))


slett = 0

def push():
    global slett, db, scrollFrame
    slett+=1
    db[f"card{slett}"] = [f"card{slett}","24 mm",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),40]
    print(slett)



    for widget in scrollFrame.winfo_children():
        widget.destroy()    
    save(db, "db.txt")
    db = loadd("db.txt")
    refreshLabel(db)
    check()
    return



cPad = tk.Frame(root, padx=100, pady=100)
cPad.grid(column=1, row=0)

testb = tk.Button(cPad, text="Press me", command=push, anchor="center")
testb.pack()



cardDisplay.grid(column=0, row=0)


dispCanvas.pack(side="left", fill="both", expand=True)
scrollBar.pack(side="right", fill="y")

#f"Label {i}" for i in range(1, 51)
 
refreshLabel(db)
print(db)
print(label_texts)
check()




infoFrame = tk.Frame(root, height=100)
infoFrame.grid(column=0, row=1)
infoLabel = tk.Label(infoFrame, text="""
Navn:
                
Avstand:
                      
Tid:     
                   
Antall forsøk:                 
                """, justify="left", anchor="w")

infoLabel.pack()



testT = threading.Thread(target=testarm)
testT.start()
root.mainloop()

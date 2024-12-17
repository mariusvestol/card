import tkinter as tk
import pickle
import time

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




root.mainloop()
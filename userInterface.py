import tkinter as tk
import DataHandler

class userInterface(tk.Tk):

    def __init__(self):
        super().__init__()
    
        self.dh = DataHandler("db.txt")
        self.infoFrame = tk.Frame(self, height=100)
        self.infoFrame.grid(column=0, row=1)
        self.infoLabel = tk.Label(self.infoFrame, text="""
Navn:
                
Avstand:
                      
Tid:     
                   
Antall forsøk:                 
                """, justify="left", anchor="w")

    def reInfo(li):
        global infoLabel
        infoLabel.config(text=f"""
Navn:                  {li[0]}
                
Avstand:             {li[1]}
                      
Tid:                     {li[2]}     
                   
Antall forsøk:      {li[3]}                 
                """)

    def check(self):
        for text in label_texts:
            frame = tk.Frame(scrollFrame, borderwidth=1, pady=5, relief="solid")
            label1 = tk.Label(frame,text=text, width=25, anchor="w")
            label2 = tk.Label(frame, text="X")
            # relief for synlig kant
            label2.bind("<Button-1>", lambda e, text=text: self.deleteLabel(text))
            label1.bind("<Button-1>", lambda e, text=text: self.reInfo(self.dh.db[text]))
            frame.pack(anchor="w")
            label1.grid(column=0, row=0)
            label2.grid(column=1, row=0)

    def refreshLabel(self):
        global label_texts
        label_texts = []
        for x in self.dh.db:
            label_texts.append(x)

    def deleteLabel(self, name):
        global db
        del db[name]
        print(db)
        self.refreshData()
        #kanskje det er her vi skal fikse metodene?


    def refreshData(self):
        global scrollFrame, db
        for widget in scrollFrame.winfo_children():
            widget.destroy()
        self.save(db, "db.txt")
        db = self.loadDb("db.txt")
        self.refreshLabel(db)
        self.check()
        return

    
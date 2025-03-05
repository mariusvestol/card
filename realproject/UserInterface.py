import tkinter as tk
from DataHandler import DataHandler

class UserInterface(tk.Tk):

    def __init__(self):
        super().__init__()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    

        self.dh = DataHandler("db.txt")
        self.infoFrame = tk.Frame(self, height=100)
        self.infoFrame.grid(column=0, row=1)
        
        self.cardDisplay = tk.Frame(self)
        self.dispCanvas = tk.Canvas(self.cardDisplay)
        self.scrollBar = tk.Scrollbar(self.cardDisplay, orient="vertical", command=self.dispCanvas.yview)
        self.scrollFrame = tk.Frame(self.dispCanvas)

        self.scrollFrame.bind("<Configure>", lambda e: self.dispCanvas.configure(scrollregion=self.dispCanvas.bbox("all")))

        #denne linjen har jeg ikke sett på
        self.window = self.dispCanvas.create_window((0, 0), window=self.scrollFrame, anchor="nw")

        #må legge til attribute senere fordi scollbar fantes ikke
        self.dispCanvas.configure(yscrollcommand=self.scrollBar.set)
        
                
        self.cPad = tk.Frame(self, padx=100, pady=100)
        self.cPad.grid(column=1, row=0)

        self.testb = tk.Button(self.cPad, text="Press me", command=self.pushLabel, anchor="center")
        self.testb.pack()

        self.cardDisplay.grid(column=0, row=0)


        self.dispCanvas.pack(side="left", fill="both", expand=True)
        self.scrollBar.pack(side="right", fill="y")

#f"Label {i}" for i in range(1, 51)

        self.refreshLabel()


# dette skal være mulig å gjøre bedre..
        self.infoLabel = tk.Label(self.infoFrame, text="""

        
Navn:
                
Avstand:
                      
Tid:     
                   
Antall forsøk:                 
                """, justify="left", anchor="w")
        
        self.infoLabel.pack()


    def reInfo(self,li):
        self.infoLabel.config(text=f"""
Navn:                  {li[0]}
                
Avstand:             {li[1]}
                      
Tid:                     {li[2]}     
                   
Antall forsøk:      {li[3]}                 
                """)

    def check(self):
        for text in self.label_texts:
            frame = tk.Frame(self.scrollFrame, borderwidth=1, pady=5, relief="solid")
            label1 = tk.Label(frame,text=text, width=25, anchor="w")
            label2 = tk.Label(frame, text="X")
            # relief for synlig kant
            label2.bind("<Button-1>", lambda e, text=text: self.deleteLabel(text))
            label1.bind("<Button-1>", lambda e, text=text: self.reInfo(self.dh.db[text]))
            frame.pack(anchor="w")
            label1.grid(column=0, row=0)
            label2.grid(column=1, row=0)
 
    def refreshLabel(self):
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
        self.dh.refresh()
        self.label_texts = []
        for x in self.dh.db:
            self.label_texts.append(x)
        self.check()


    def pushLabel(self):
        self.dh.push()
        self.refreshLabel()

    def deleteLabel(self, name):
        del self.dh.db[name]
        self.refreshLabel()


test = UserInterface()
test.mainloop()

import pickle
import time

class DataHandler():

    def loadDb(self):
        f = open(self.file, "rb")
        out = pickle.load(f)
        f.close()
        return out
    
    def save(self):
        f = open(self.file, "wb")
        pickle.dump(self.db, f)
        f.close()
        return
    
    def __init__(self, file):
        self.file = file
        
        self.slett = 0
        # slett 
        
        try:
            self.db = self.loadDb()
        except:
            self.db = {}
            self.save()

    def push(self):
        self.slett+=1
        self.db[f"card{self.slett}"] = [f"card{self.slett}","24 mm",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),40]
        self.refresh()
        
        
    def refresh(self):
        self.save()
        self.db = self.loadDb()

def main():
        test = DataHandler("test")
        #test.push()
        #test.save()
        print(test.db)

if __name__ == "__main__":
    main()


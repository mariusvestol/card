from tkinter import *
import db
import importlib


root = Tk()





class NewButton(Button):
	def __init__(self, parent, buttonId, **kwargs):
		super().__init__(parent, **kwargs)
		self.buttonId = buttonId


def delete(dId):
	print(dId)
	for b in buttons:
		if b.buttonId == dId:
			goneButton = b
			goneButton.destroy()
			buttons.remove(b)
			with open("db.py", "r") as file:
				content = file.readlines()
			content.remove(dId)
			with open("db.py", 'w') as file:
				file.writelines(content)
	importlib.reload(db)
	print(db.database)



with open("db.py", "r") as file:
	content = file.readlines()

new_code = []
buttons = []




#line = f"""database.append('{input()}')"""
"""
new_code.append('\n' + line)  # Adding newline to maintain line breaks


content.extend(new_code)


# vi skriver hele på nytt writelines tar kodeblokken så alt vi må gjøre er å lokalisere hvor det vi vil fjerne er også fjerne dette fra listen

#thislist.remove(det du vil slette) 


#with gjor at vi lukker dokumentet etter vi har jobbet med det
with open("db.py", 'w') as file:
	file.writelines(content)
"""

importlib.reload(db)
print(db.database)

#sjekke hver milimeter

with open("db.py", "r") as file:
	print(file.readlines())




#vi mangler fortsatt å få inn nye tror jeg - med mindre den duplicater liksom idk

with open("db.py", "r") as file:

	for line in file.readlines():
		if line[:15] == "database.append":
	
			button = NewButton(root, text=line, command=lambda line=line: delete(line), buttonId=line)
# vi skriver lambda i=i fordi vi vil ha argumenter i funksjonen og fordi vi ønsker i da knappen var laget
			button.pack()
			buttons.append(button)




text = Text(root, height=1)
text.pack()

def pushText():

	with open("db.py", "r") as file:
		content = file.readlines()

	print("hello world")

	line = f"""database.append('{text.get("1.0","end-1c")}')"""

	new_code.append('\n' + line)  # Adding newline to maintain line breaks


	content.extend(new_code)

	with open("db.py", 'w') as file:
		file.writelines(content)
	button = NewButton(root, text=line, command=lambda line=line: delete(line), buttonId=line)
# vi skriver lambda i=i fordi vi vil ha argumenter i funksjonen og fordi vi ønsker i da knappen var laget
	button.pack()
	buttons.append(button)




button = Button(root, command=pushText, text="push")
button.pack()


"""

green = True

#pip3 install opencv-python


def drive():
	print("tester")


#morendin

def test():
	if green:
		print("yes")
		#break ???

	else:
		print("no")




"""
root.mainloop()



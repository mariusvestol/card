from tkinter import *
import db
import importlib


#root = Tk()



script_path = "db.py"

with open(script_path, "r") as file:
	content = file.readlines()

new_code = []


line = f"""database.append('{input()}')"""
new_code.append('\n' + line)  # Adding newline to maintain line breaks


content.extend(new_code)

with open(script_path, 'w') as file:
	file.writelines(content)


importlib.reload(db)
print(db.database)

#sjekke hver milimeter


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
#root.mainloop()



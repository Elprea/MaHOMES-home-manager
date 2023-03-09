# add messages

from tkinter import Button, Entry, Canvas, Tk, messagebox, Label, Text
import features_db
import main_GUI_parent
import sqlite3

def add(parentID, firstname, child, title, message):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur. execute("select * from child where childID=:childID", {"childID": child})
	if cur.fetchone():
		status="Sent"
		print("Message Added")
		features_db.add_messages(firstname, title.strip(), message.strip(), status, parentID, child.strip())
		window.destroy()
		main_GUI_parent.mailbox(parentID, firstname)
		content = 'You have a new message!'
		cur.execute("insert into childAlert values(?,?)",
			(content, child.strip())
		)
	else:
		messagebox.showinfo("Worker # failed", "Worker # doesn't exist.")
		window.destroy()

	conn.commit()
	conn.close()	

	
def message(parentID, firstname):
	global window
	window = Tk()
	window.title("Home Manager - Send Message")
	window.geometry("320x360")

	header = Label(window,
		text="Send Message",
		font="Arial, 15"
		)
	header.place(x=110, y=30)

	childlbl = Label(window,
		text="Child ID: ",
		font="Arial, 10"
		)
	childlbl.place(x=10, y=82)

	titlelbl = Label(window,
		text="Title: ",
		font="Arial, 10"
		)
	titlelbl.place(x=10, y=122)

	messagelbl = Label(window,
		text="Message: ",
		font="Arial, 10"
		)
	messagelbl.place(x=10, y=212)

	childEn = Entry(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	childEn.place(
		x=90, y=80,
		width=200, height=30
		)

	titleEn = Entry(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	titleEn.place(
		x=90, y=120,
		width=200, height=30
		)

	messageTx = Text(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	messageTx.place(
		x=90, y=160,
		width=200, height=110
		)

	assignBtn = Button(window,
		text="Deploy",
		font="Arial, 12",
		command=lambda: add(parentID, firstname, childEn.get(), titleEn.get(), messageTx.get("1.0", 'end-1c'))
		)
	assignBtn.place(
		x=80, y=295,
		width=60, height=30
		)

	cancelBtn = Button(window,
		text="Cancel",
		font="Arial, 12",
		command=lambda: window.destroy()
		)
	cancelBtn.place(
		x=160, y=295,
		width=60, height=30
		)

	window.resizable(False, False)
	window.mainloop()

if __name__ == "__main__":
	message()
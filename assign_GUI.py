# add assignments
from tkinter import Button, Entry, Canvas, Tk, messagebox, Label, Text
import features_db
import main_GUI_parent
import sqlite3

def add(parentID, worker, task, occur, reward, firstname):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur. execute("select * from child where childID=:childID", {"childID": worker})
	if cur.fetchone():
		status="Working"
		features_db.add_tasks(task.strip(), status, occur.strip(), reward.strip(), parentID, worker.strip())
		window.destroy()
		main_GUI_parent.assignment(parentID, firstname)
	else:
		messagebox.showinfo("Worker # failed", "Worker # doesn't exist.")
		window.destroy()

	conn.commit()
	conn.close()	

def assign(parentID, firstname):
	global window
	window = Tk()
	window.title("Home Manager - Create task")
	window.geometry("320x360")

	header = Label(window,
		text="Create Task",
		font="Arial, 15"
		)
	header.place(x=110, y=30)

	childlbl = Label(window,
		text="Worker ID: ",
		font="Arial, 10"
		)
	childlbl.place(x=10, y=82)

	tasklbl = Label(window,
		text="Task: ",
		font="Arial, 10"
		)
	tasklbl.place(x=10, y=122)

	occurlbl = Label(window,
		text="Occurence: ",
		font="Arial, 10"
		)
	occurlbl.place(x=10, y=212)

	rewardlbl = Label(window,
		text="Reward: ",
		font="Arial, 10"
		)
	rewardlbl.place(x=10, y=252)
	
	workerEn = Entry(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	workerEn.place(
		x=90, y=80,
		width=200, height=30
		)

	taskTx = Text(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	taskTx.place(
		x=90, y=120,
		width=200, height=80
		)

	occurEn = Entry(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	occurEn.place(
		x=90, y=210,
		width=200, height=30
		)

	rewardEn = Entry(window,
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	rewardEn.place(
		x=90, y=250,
		width=200, height=30
		)

	assignBtn = Button(window,
		text="Deploy",
		font="Arial, 12",
		command=lambda: add(parentID, workerEn.get(), taskTx.get("1.0",'end-1c'), occurEn.get(), rewardEn.get(), firstname)
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
	assign()
# main child gui

from tkinter import *
from tkinter import ttk
import sqlite3

def dashboard():
	global dashboardFr
	dashboardFr = Frame(window, width=1400, height=650, background="gray")
	dashboardFr.place(x=5, y=100, width=1390, height=645)

	todolbl = Label(dashboardFr,
		text="Todo",
		font="Arial, 15"
		)
	todolbl.place(x=20, y=15)


	# to do table
	todoTr = ttk.Treeview(dashboardFr)
	todoTr['columns'] = ("From", "Work", "Occurence", "Status", "Reward")
	todoTr.column("#0", width=0, stretch=0)
	todoTr.column("From", width=80, anchor=CENTER)
	todoTr.column("Work", width=800, anchor=CENTER)
	todoTr.column("Occurence", width=80, anchor=CENTER)
	todoTr.column("Status", width=60, anchor=CENTER)
	todoTr.column("Reward", width=200, anchor=CENTER)
	todoTr.heading("#0", text="", anchor=CENTER)
	todoTr.heading("From", text="From", anchor=CENTER)
	todoTr.heading("Work", text="Work", anchor=CENTER)
	todoTr.heading("Occurence", text="Occurence", anchor=CENTER)
	todoTr.heading("Status", text="Status", anchor=CENTER)
	todoTr.heading("Reward", text="Reward", anchor=CENTER)
	todoTr.place(x=10, y=60, height=200)


	alertlbl = Label(dashboardFr,
		text="Alert",
		font="Arial, 15"
		)
	alertlbl.place(x=20, y=320)

	# alert table
	alertTr = ttk.Treeview(dashboardFr)
	alertTr['columns'] = ("Content")
	alertTr.column("#0", width=0, stretch=0)
	alertTr.column("Content", width=1220, anchor=CENTER)
	alertTr.heading("#0", text="", anchor=CENTER)
	alertTr.heading("Content", text="Content", anchor=CENTER)
	alertTr.place(x=10, y=360, height=200)

def assignment():

	global assignmentFr
	assignmentFr = Frame(window, width=1400, height=650, background="bisque")
	assignmentFr.place(x=5, y=100, width=1390, height=645)

	# assignment label
	tasklbl = Label(assignmentFr,
		text="Main Tasks",
		font="Arial, 15"
		)
	tasklbl.place(x=20, y=15)

	# other assignment table
	otherTr = ttk.Treeview(assignmentFr)
	otherTr['columns'] = ("From", "Work", "Occurence", "Status", "Reward")
	otherTr.column("#0", width=0, stretch=0)
	otherTr.column("From", width=80, anchor=CENTER)
	otherTr.column("Work", width=800, anchor=CENTER)
	otherTr.column("Occurence", width=80, anchor=CENTER)
	otherTr.column("Status", width=60, anchor=CENTER)
	otherTr.column("Reward", width=200, anchor=CENTER)
	otherTr.heading("#0", text="", anchor=CENTER)
	otherTr.heading("From", text="From", anchor=CENTER)
	otherTr.heading("Work", text="Work", anchor=CENTER)
	otherTr.heading("Occurence", text="Occurence", anchor=CENTER)
	otherTr.heading("Status", text="Status", anchor=CENTER)
	otherTr.heading("Reward", text="Reward", anchor=CENTER)
	otherTr.place(x=10, y=60, height=200)
	

	recurlbl = Label(assignmentFr,
		text="Recurring Tasks",
		font="Arial, 15"
		)
	recurlbl.place(x=20, y=320)

	# recurring assignment table
	recurringTr = ttk.Treeview(assignmentFr)
	recurringTr['columns'] = ("From", "Work", "Occurence", "Status", "Reward")
	recurringTr.column("#0", width=0, stretch=0)
	recurringTr.column("From", width=80, anchor=CENTER)
	recurringTr.column("Work", width=800, anchor=CENTER)
	recurringTr.column("Occurence", width=80, anchor=CENTER)
	recurringTr.column("Status", width=60, anchor=CENTER)
	recurringTr.column("Reward", width=200, anchor=CENTER)
	recurringTr.heading("#0", text="", anchor=CENTER)
	recurringTr.heading("From", text="From", anchor=CENTER)
	recurringTr.heading("Work", text="Work", anchor=CENTER)
	recurringTr.heading("Occurence", text="Occurence", anchor=CENTER)
	recurringTr.heading("Status", text="Status", anchor=CENTER)
	recurringTr.heading("Reward", text="Reward", anchor=CENTER)
	recurringTr.place(x=10, y=360, height=200)

	completeBtn = Button(assignmentFr,
		text="Complete",
		font="Arial, 10"
		)
	completeBtn.place(
		x=800, y=300,
		width=80, height=40
		)

	evadeBtn = Button(assignmentFr,
		text="Evade",
		font="Arial, 10"
		)
	evadeBtn.place(
		x=900, y=300,
		width=80, height=40
		)

	protestBtn = Button(assignmentFr,
		text="Protest",
		font="Arial, 10",
		command=lambda: mailbox()
		)
	protestBtn.place(
		x=1000, y=300,
		width=80, height=40
		)


def mailbox():

	global mailboxFr
	mailboxFr = Frame(window, width=1400, height=650, background="light blue")
	mailboxFr.place(x=5, y=100, width=1390, height=645)


def account():

	global accountFr
	accountFr = Frame(window, width=1400, height=650, background="yellow")
	accountFr.place(x=5, y=100, width=1390, height=645)


def main_gui_child():
	global window
	window = Tk()
	window.title("Welcome to HOME MANAGER")
	window.geometry("1400x750")

	fname = "Reigin"
	welcome = Label(
		text="Welcome "+fname+"!",
		font="Arial, 25"
		)
	welcome.place(
		x=30, y=30
		)

	# buttons to show features
	dashboardBtn = Button(
		text="Dashboard",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		command=lambda: dashboard()
		)
	dashboardBtn.place(
		x=780, y=60,
		width=120, height=40
		)

	assignmentBtn = Button(
		text="Assignment",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		command=lambda: assignment()
		)
	assignmentBtn.place(
		x=900, y=60,
		width=120, height=40
		)

	mailboxBtn = Button(
		text="Mailbox",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		command=lambda: mailbox()
		)
	mailboxBtn.place(
		x=1020, y=60,
		width=120, height=40
		)

	accountBtn = Button(
		text="Account",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		command=lambda: account()
		)
	accountBtn.place(
		x=1140, y=60,
		width=120, height=40
		)

	dashboard()

	window.resizable(False, False)
	window.mainloop()


if __name__ == "__main__":
	main_gui_child()
# main parent gui

from tkinter import Button, Canvas, Entry, Tk, Frame, CENTER, BOTTOM, Label
from tkinter import ttk
import assign_GUI
import message_GUI
import features_db
import sqlite3
import login_GUI

def logout():
	window.destroy()
	login_GUI.login_gui()

# deletes row for messages table
def deleteRow(parentID, inboxValue, firstname):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("select rowid from messages where parentID=:parentID",{
		"parentID":parentID
		})
	count =0
	for i in cur.fetchall():
		if i[0] == inboxValue['values'][4]:
			features_db.delete_msg_parent(parentID, i[0])
			mailbox(parentID, firstname)
		count+=1

	conn.commit()
	conn.close()

# deletes row for tasks table
def deleteRow_task(parentID, taskValue, firstname):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("select rowid from tasks where parentID=:parentID",{
		"parentID":parentID
		})
	count =0
	for i in cur.fetchall():
		if i[0] == taskValue['values'][5]:
			features_db.delete_tasks_parent(parentID, i[0])
			assignment(parentID, firstname)
		count+=1

	conn.commit()
	conn.close()


def dashboard(parentID):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	global dashboardFr
	dashboardFr = Frame(window, width=1250, height=650, background="#cfc1e3")
	dashboardFr.place(x=0, y=100, width=1250, height=650)

	todolbl = Label(dashboardFr,
		text="Working Tasks",
		font="Arial, 20",
		bg="#cfc1e3"
		)
	todolbl.place(x=550, y=15)

	# to do table
	todoTr = ttk.Treeview(dashboardFr)
	todoTr['columns'] = ("Worker", "Work", "Occurence", "Status", "Reward")
	todoTr.column("#0", width=0, stretch=0)
	todoTr.column("Worker", width=80, anchor=CENTER)
	todoTr.column("Work", width=780, anchor=CENTER)
	todoTr.column("Occurence", width=80, anchor=CENTER)
	todoTr.column("Status", width=80, anchor=CENTER)
	todoTr.column("Reward", width=200, anchor=CENTER)
	todoTr.heading("#0", text="", anchor=CENTER)
	todoTr.heading("Worker", text="Worker", anchor=CENTER)
	todoTr.heading("Work", text="Work", anchor=CENTER)
	todoTr.heading("Occurence", text="Occurence", anchor=CENTER)
	todoTr.heading("Status", text="Status", anchor=CENTER)
	todoTr.heading("Reward", text="Reward", anchor=CENTER)
	todoTr.place(x=10, y=60, height=200, width=1225)

	count=0
	cur.execute("select child.firstName, taskContent, taskOccurence, taskStatus, taskReward from tasks inner join child on tasks.childID = child.childID where taskStatus = 'Working' and parentID = :parentID",{
		"parentID":parentID
		})
	for i in cur.fetchall():
		todoTr.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2], i[3], i[4]))
		count += 1

	alertlbl = Label(dashboardFr,
		text="Alert",
		font="Arial, 20",
		bg="#cfc1e3"
		)
	alertlbl.place(x=600, y=320)

	# alert table
	alertTr = ttk.Treeview(dashboardFr)
	alertTr['columns'] = ("Content")
	alertTr.column("#0", width=0, stretch=0)
	alertTr.column("Content", width=1220, anchor=CENTER)
	alertTr.heading("#0", text="", anchor=CENTER)
	alertTr.heading("Content", text="Content", anchor=CENTER)
	alertTr.place(x=10, y=360, height=200)

	count=0
	cur.execute("select alertContent from parentAlert where parentID=:parentID",{"parentID":parentID})
	for i in cur.fetchall():
		alertTr.insert(parent='', index='end', iid=count, text='', values=(i))
		count += 1

	conn.commit()
	conn.close()

def assignment(parentID, firstname):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	global assignmentFr
	assignmentFr = Frame(window, width=1250, height=650, background="bisque")
	assignmentFr.place(x=0, y=100, width=1250, height=650)

	# assignment label
	tasklbl = Label(assignmentFr,
		text="Main Tasks",
		font="Arial, 20",
		bg="bisque"
		)
	tasklbl.place(x=500, y=15)

	# other assignment table
	otherTr = ttk.Treeview(assignmentFr)
	otherTr['columns'] = ("Worker", "Work", "Occurence", "Status", "Reward", "rowID")
	otherTr.column("#0", width=0, stretch=0)
	otherTr.column("Worker", width=80, anchor=CENTER)
	otherTr.column("Work", width=780, anchor=CENTER)
	otherTr.column("Occurence", width=80, anchor=CENTER)
	otherTr.column("Status", width=80, anchor=CENTER)
	otherTr.column("Reward", width=200, anchor=CENTER)
	otherTr.column("rowID", width=200, anchor=CENTER)
	otherTr.heading("#0", text="", anchor=CENTER)
	otherTr.heading("Worker", text="Worker", anchor=CENTER)
	otherTr.heading("Work", text="Work", anchor=CENTER)
	otherTr.heading("Occurence", text="Occurence", anchor=CENTER)
	otherTr.heading("Status", text="Status", anchor=CENTER)
	otherTr.heading("Reward", text="Reward", anchor=CENTER)
	otherTr.heading("rowID", text="rowID", anchor=CENTER)
	otherTr.place(x=10, y=60, height=200, width=1225)

	# get selected items ready for delete button
	def selectedMails(a):
		global clicked1
		clicked1 = otherTr.focus()
	otherTr.bind('<ButtonRelease-1>', selectedMails)

	count=0
	cur.execute("select child.firstName, taskContent, taskOccurence, taskStatus, taskReward, tasks.rowid from tasks inner join child on tasks.childID = child.childID where not lower(taskOccurence) in ('daily', 'weekly', 'monthly', 'yearly') and parentID=:parentID",{"parentID":parentID})
	for i in cur.fetchall():
		otherTr.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]))
		count += 1

	recurlbl = Label(assignmentFr,
		text="Recurring Tasks",
		font="Arial, 20",
		bg="bisque"
		)
	recurlbl.place(x=480, y=300)

	# recurring assignment table
	recurringTr = ttk.Treeview(assignmentFr)
	recurringTr['columns'] = ("Worker", "Work", "Occurence", "Status", "Reward", "rowID")
	recurringTr.column("#0", width=0, stretch=0)
	recurringTr.column("Worker", width=80, anchor=CENTER)
	recurringTr.column("Work", width=780, anchor=CENTER)
	recurringTr.column("Occurence", width=80, anchor=CENTER)
	recurringTr.column("Status", width=80, anchor=CENTER)
	recurringTr.column("Reward", width=200, anchor=CENTER)
	recurringTr.column("rowID", width=200, anchor=CENTER)
	recurringTr.heading("#0", text="", anchor=CENTER)
	recurringTr.heading("Worker", text="Worker", anchor=CENTER)
	recurringTr.heading("Work", text="Work", anchor=CENTER)
	recurringTr.heading("Occurence", text="Occurence", anchor=CENTER)
	recurringTr.heading("Status", text="Status", anchor=CENTER)
	recurringTr.heading("Reward", text="Reward", anchor=CENTER)
	recurringTr.heading("rowID", text="rowID", anchor=CENTER)
	recurringTr.place(x=10, y=360, height=200, width=1225)

	# get selected items ready for delete button
	def selectedMailss(a):
		global clicked2
		clicked2 = recurringTr.focus()
	recurringTr.bind('<ButtonRelease-1>', selectedMailss)

	count=0
	cur.execute("select child.firstName, taskContent, taskOccurence, taskStatus, taskReward, tasks.rowid from tasks inner join child on tasks.childID = child.childID where lower(taskOccurence) in ('daily', 'weekly', 'monthly', 'yearly') and parentID=:parentID",{"parentID":parentID})
	for i in cur.fetchall():
		recurringTr.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]))
		count += 1

	createBtn = Button(assignmentFr,
		text="Create",
		font="Arial, 10",
		command=lambda: assign_GUI.assign(parentID, firstname)
		)
	createBtn.place(
		x=410, y=570,
		width=80, height=50
		)

	cancelBtn = Button(assignmentFr,
		text="Cancel in\nMain",
		font="Arial, 10",
		command=lambda: deleteRow_task(parentID, otherTr.item(clicked1), firstname)
		)
	cancelBtn.place(
		x=510, y=570,
		width=80, height=50
		)

	cancelBtn = Button(assignmentFr,
		text="Cancel in\nRecurring",
		font="Arial, 10",
		command=lambda: deleteRow_task(parentID, recurringTr.item(clicked2), firstname)
		)
	cancelBtn.place(
		x=610, y=570,
		width=80, height=50
		)

	messageBtn = Button(assignmentFr,
		text="Message",
		font="Arial, 10",
		command=lambda: mailbox(parentID, firstname)
		)
	messageBtn.place(
		x=710, y=570,
		width=80, height=50
		)

	conn.commit()
	conn.close()


def mailbox(parentID, firstname):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	global mailboxFr
	mailboxFr = Frame(window, width=1250, height=650, background="light blue")
	mailboxFr.place(x=0, y=100, width=1250, height=650)

	msglbl = Label(mailboxFr,
		text="Messages",
		font="Arial, 20",
		bg="light blue"
		)
	msglbl.place(x=600, y=15)

	inboxTr = ttk.Treeview(mailboxFr)
	inboxTr['columns'] = ("From", "To", "Title", "Content", "rowID")
	inboxTr.column("#0", width=0, stretch=0)
	inboxTr.column("From", width=80, anchor=CENTER)
	inboxTr.column("To", width=80, anchor=CENTER)
	inboxTr.column("Title", width=160, anchor=CENTER)
	inboxTr.column("Content", width=900, anchor=CENTER)
	inboxTr.column("rowID", width=900, anchor=CENTER)
	inboxTr.heading("#0", text="", anchor=CENTER)
	inboxTr.heading("From", text="From", anchor=CENTER)
	inboxTr.heading("To", text="To", anchor=CENTER)
	inboxTr.heading("Title", text="Title", anchor=CENTER)
	inboxTr.heading("Content", text="Content", anchor=CENTER)
	inboxTr.heading("rowID", text="rowID", anchor=CENTER)
	inboxTr.place(x=10, y=60, height=450, width=1222)

	# get selected items ready for delete button
	def selectedMail(a):
		global clicked
		clicked = inboxTr.focus()
	inboxTr.bind('<ButtonRelease-1>', selectedMail)

	count=0
	cur.execute("select msgSender, child.firstName, parent.firstName, msgTitle, msgContent, messages.rowid from messages inner join child on messages.childID=child.childID inner join parent on messages.parentID=parent.parentID where messages.parentID=:parentID",{
		"parentID":parentID
		})
	for i in cur.fetchall():
		# checks if sender is parent or child
		if i[0] == i[2]:
			inboxTr.insert(parent='', index='end', iid=count, text='', values=(i[2], i[1], i[3], i[4], i[5]))
		else:
			inboxTr.insert(parent='', index='end', iid=count, text='', values=(i[1], i[2], i[3], i[4], i[5]))
		count += 1

	writeBtn = Button(mailboxFr,
		text="Write",
		font="Arial, 10",
		command=lambda: message_GUI.message(parentID, firstname)
		)
	writeBtn.place(
		x=510, y=550,
		width=80, height=40
		)

	deleteBtn = Button(mailboxFr,
		text="Delete",
		font="Arial, 10",
		command=lambda: deleteRow(parentID, inboxTr.item(clicked), firstname)
		)
	deleteBtn.place(
		x=610, y=550,
		width=80, height=40
		)

	markBtn = Button(mailboxFr,
		text="Trademark",
		font="Arial, 10",
		)
	markBtn.place(
		x=710, y=550,
		width=80, height=40
		)

	conn.commit()
	conn.close()

def account(parentID, username, password, firstname, lastname, gender, dob, address, contact):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	global accountFr
	accountFr = Frame(window, width=1250, height=650, background="#a3e879")
	accountFr.place(x=0, y=100, width=1250, height=650)

	accntlbl = Label(accountFr,
		text="Account Informations: ",
		font="Arial, 20",
		bg="#a3e879"
		)
	accntlbl.place(x=30, y=50)

	lbl1 = Label(accountFr,
		text="Name: " +firstname+" "+ lastname,
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl1.place(x=30, y=95)

	lbl2 = Label(accountFr,
		text="Gender: "+gender,
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl2.place(x=30, y=120)

	lbl3 = Label(accountFr,
		text="Date of Birth: " +dob,
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl3.place(x=30, y=145)

	lbl4 = Label(accountFr,
		text="Address: "+address,
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl4.place(x=30, y=170)

	lbl5 = Label(accountFr,
		text="Contact #: " +str(contact),
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl5.place(x=30, y=195)

	lbl6 = Label(accountFr,
		text="Username: "+username,
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl6.place(x=30, y=220)

	lbl7 = Label(accountFr,
		text="Password: " +password,
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl7.place(x=30, y=245)

	lbl8 = Label(accountFr,
		text="Your ID: "+str(parentID),
		font="Arial, 10",
		bg="#a3e879"
		)
	lbl8.place(x=30, y=270)

	logoutBtn = Button(accountFr,
		text="LOGOUT",
		font="Arial, 10",
		command=lambda: logout()
		)
	logoutBtn.place(x=30, y=330)

	conn.commit()
	conn.close()


def main_gui_parent(parentID, username, password, firstname, lastname, gender, dob, address, contact):
	global window
	window = Tk()
	window.title("HOME MANAGER")
	window.geometry("1250x750")
	window.configure(background="white")

	welcome = Label(
		text="Welcome "+firstname+"!",
		font="Arial, 30",
		bg="white"
		)
	welcome.place(
		x=30, y=30
		)

	# buttons to show features
	global dashboardBtn
	dashboardBtn = Button(
		text="Dashboard",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		bg="#cfc1e3",
		command=lambda: dashboard(parentID)
		)
	dashboardBtn.place(
		x=780, y=60,
		width=120, height=40
		)

	global assignmentBtn
	assignmentBtn = Button(
		text="Assignment",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		bg="bisque",
		command=lambda: assignment(parentID, firstname)
		)
	assignmentBtn.place(
		x=900, y=60,
		width=120, height=40
		)

	global mailboxBtn
	mailboxBtn = Button(
		text="Mailbox",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		bg="light blue",
		command=lambda: mailbox(parentID, firstname)
		)
	mailboxBtn.place(
		x=1020, y=60,
		width=120, height=40
		)

	global accountBtn
	accountBtn = Button(
		text="Account",
		font="Arial, 12",
		borderwidth=2,
		relief="flat",
		bg="#a3e879",
		command=lambda: account(parentID, username, password, firstname, lastname, gender, dob, address, contact)
		)
	accountBtn.place(
		x=1140, y=60,
		width=120, height=40
		)

	dashboard(parentID)

	window.resizable(False, False)
	window.mainloop()


if __name__ == "__main__":
	main_gui_parent()
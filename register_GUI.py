# register gui

from tkinter import Button, Entry, Canvas, Tk, messagebox
import register_db
import login_GUI
import random
import sqlite3
import features_db

def checker(role, child, parent):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	errorCode=0
	if role=='Parent':
		cur.execute("select * from child where childID=:childID", {"childID": child})
		if not cur.fetchone():
			errorCode=1	
	elif role=='Child':
		cur.execute("select * from parent where parentID=:parentID", {"parentID": parent})
		if not cur.fetchone():
			errorCode=1	
	conn.commit()
	conn.close()

	return errorCode

def verify(role, randID, username, password, reenter, fname, lname, gender, dob, address, contact, child1, child2, child3, child4, child5, child6, parent1, parent2):

	errorCode=0
	errorFound=0
	if role=='Parent':
		if child1:
			errorCode=checker(role, child1, role)
			if errorCode==1:
				errorFound=1
		if child2:
			errorCode=checker(role, child2, role)
			if errorCode==1:
				errorFound=1
		if child3:
			errorCode=checker(role, child3, role)
			if errorCode==1:
				errorFound=1
		if child4:
			errorCode=checker(role, child4, role)
			if errorCode==1:
				errorFound=1
		if child5:
			errorCode=checker(role, child5, role)
			if errorCode==1:
				errorFound=1
		if child6:
			errorCode=checker(role, child6, role)
			if errorCode==1:
				errorFound=1
	elif role=='Child':
		if parent1:
			errorCode=checker(role, role, parent1)
			if errorCode==1:
				errorFound=1
		if parent2:
			errorCode=checker(role, role, parent2)
			if errorCode==1:
				errorFound=1


	if errorFound == 1:
		messagebox.showinfo("Content error", "Information given cannot be taken. Please try again")
	elif register_db.check_username(role, username.strip())==1:
		messagebox.showinfo("Error", "Username already exists. Try again")
	elif password.strip() != reenter.strip():
		messagebox.showinfo("Password failed", "Re-entered password didn't match. Try again")
	else:
		if role=="Parent":
			if child1:
				features_db.add_relationship(child1, randID)
			if child2:
				features_db.add_relationship(child2, randID)
			if child3:
				features_db.add_relationship(child3, randID)
			if child4:
				features_db.add_relationship(child4, randID)
			if child5:
				features_db.add_relationship(child5, randID)
			if child6:
				features_db.add_relationship(child6, randID)
			register_db.register_parent(randID, username.strip(), password.strip(), fname.strip(), lname.strip(), gender.strip(), dob.strip(), address.strip(), contact.strip())
		elif role=="Child":
			if parent1:
				features_db.add_relationship(parent1, randID)
			if parent2:
				features_db.add_relationship(parent2, randID)
			register_db.register_child(randID, username.strip(), password.strip(), fname.strip(), lname.strip(), gender.strip(), dob.strip(), address.strip(), contact.strip())

		window.destroy()
		login_GUI.login_gui()



def register_gui(role):

	# window gui
	global window
	window = Tk()
	window.title("Register to HOME MANAGER")
	window.geometry("700x700")

	canvas = Canvas(window,
		height=700,
		width=700,
		bd=0
		)
	canvas.place(x=0, y=0)

	canvas.create_text(
		360, 100,
		text="REGISTER",
		font=("Arial BOLD", 25)
		)

	canvas.create_text(
		250, 210,
		text="---------------------------------------------",
		fill="red",
		font=("Arial", 10)
		)

	# Texts
	canvas.create_text(
		147, 240,
		text="First Name: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		420, 240,
		text="Last Name: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		150, 280,
		text="Date of Birth: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		410, 280,
		text="Gender: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		139, 320,
		text="Address: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		142, 360,
		text="Contact #: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		145, 480,
		text="Username: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		145, 520,
		text="Password: ",
		font=("Arial", 10)
		)

	canvas.create_text(
		170, 560,
		text="Re-enter password: ",
		font=("Arial", 10)
		)

	# entry boxes
	fname = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	fname.place(
		x=200, y=225,
		width=150, height=30
		)

	lname = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	lname.place(
		x=460, y=225,
		width=150, height=30
		)

	dob = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	dob.place(
		x=200, y=265,
		width=150, height=30
		)

	gender = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	gender.place(
		x=460, y=265,
		width=150, height=30
		)

	address = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	address.place(
		x=200, y=305,
		width=350, height=30
		)

	contact = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	contact.place(
		x=200, y=345,
		width=150, height=30
		)

	username = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	username.place(
		x=200, y=465,
		width=150, height=30
		)

	password = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	password.place(
		x=200, y=505,
		width=150, height=30
		)

	reenter = Entry(
		bd=4,
		fg="black",
		bg="white",
		font=("Arial", 10)
		)
	reenter.place(
		x=240, y=545,
		width=150, height=30
		)


	# context depend on which role is registering
	if role=="Parent":
		canvas.create_text(
			151.5, 400,
			text="Enter Child #: ",
			font=("Arial", 10)
			)

		canvas.create_text(
			300, 440,
			text="*you can enter more child # when you log-in*",
			font=("Arial", 10)
			)

		child1 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		child1.place(
			x=200, y=385,
			width=55, height=30
			)

		child2 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		child2.place(
			x=270, y=385,
			width=55, height=30
			)

		child3 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		child3.place(
			x=340, y=385,
			width=55, height=30
			)

		child4 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		child4.place(
			x=410, y=385,
			width=55, height=30
			)

		child5 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		child5.place(
			x=480, y=385,
			width=55, height=30
			)

		child6 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		child6.place(
			x=550, y=385,
			width=55, height=30
			)
	elif role=="Child":
		canvas.create_text(
			151.5, 400,
			text="Enter Parent #: ",
			font=("Arial", 10)
			)

		canvas.create_text(
			300, 440,
			text="*you can edit parent # when you log-in*",
			font=("Arial", 10)
			)

		parent1 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		parent1.place(
			x=200, y=385,
			width=100, height=30
			)

		parent2 = Entry(
			bd=4,
			fg="black",
			bg="white",
			font=("Arial", 10)
			)
		parent2.place(
			x=320, y=385,
			width=100, height=30
			)

	randID = random.randint(10000, 99999)
	if register_db.verify_id(role, randID) == 1:
		randID = random.randint(10000, 99999)


	# submit button
	if role=='Parent':
		submitBtn = Button(
			text="SUBMIT",
			font=("Arial, 10"),
			command=lambda: verify(role, randID, username.get(), password.get(), reenter.get(), fname.get(), lname.get(), gender.get(), dob.get(), address.get(), contact.get(), child1.get(), child2.get(), child3.get(), child4.get(), child5.get(), child6.get(), 0, 0)
			)
	else:
		submitBtn = Button(
			text="SUBMIT",
			font=("Arial, 10"),
			command=lambda: verify(role, randID, username.get(), password.get(), reenter.get(), fname.get(), lname.get(), gender.get(), dob.get(), address.get(), contact.get(), 0,0,0,0,0,0, parent1.get(), parent2.get())
			)
	submitBtn.place(
		x=452, y=467,
		width=150, height=100
		)


	window.resizable(False, False)
	window.mainloop()

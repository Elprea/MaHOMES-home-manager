# login gui
from tkinter import Button, Canvas, Entry, Tk, messagebox
import sqlite3
import register_GUI_prompt
import main_db
import main_GUI_child
import main_GUI_parent

def register():
	window.destroy()
	register_GUI_prompt.prompt()

def goto_main(username, password):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()
	catch=0
	# check account if exist in parent table
	cur.execute("select * from parent where username=:username and password=:password", {
		"username": username.strip(),
		"password": password.strip()
		})
	approveID=cur.fetchone()
	if approveID:
		window.destroy()
		# Transfer all values from table to parent main gui
		main_GUI_parent.main_gui_parent(approveID[0], approveID[1], approveID[2], approveID[3], approveID[4], approveID[5], approveID[6], approveID[7], approveID[8])
		catch=1

	# check account if exist in child table
	cur.execute("select * from child where username=:username and password=:password", {
		"username": username.strip(),
		"password": password.strip()
		})
	approveID=cur.fetchone()
	if approveID:
		window.destroy()
		# Transfer all values from table to child main gui
		main_GUI_child.main_gui_child(approveID[0], approveID[1], approveID[2], approveID[3], approveID[4], approveID[5], approveID[6], approveID[7], approveID[8])
	else:
		if catch==0:
			messagebox.showinfo("Incorrect", "Wrong username or password. Please try again.")

	conn.commit()
	conn.close()


def login_gui():
	#call main database
	main_db.main()

	# create main gui window
	global window
	window = Tk()
	window.title("Login to HOME MANAGER")
	window.geometry("400x400")

	# canvas widgets
	canvas = Canvas(window,
		height=400,
		width=400,
		bd=0,
		)
	canvas.place(x=0,y=0)

	canvas.create_text(
		200, 50,
		text="MaHOMES",
		fill="black",
		font=("Arial BOLD", 40)
		)

	canvas.create_text(
		200, 80,
		text="Manage your HOME",
		fill="gray",
		font=("Arial BOLD", 10)
		)

	canvas.create_text(
		200, 150,
		text="LOG-IN"
		)

	# entry field functions
	def user_entry_clicked(e):
		if username.get() == 'Username':
			username.delete(0,"end")
			username.insert(0, '')
			username.config(show="", fg="black")
	def user_entry_out(e):
		if username.get() == '':
			username.insert(0, "Username")
			username.config(fg="gray")
	def pass_entry_clicked(e):
		if password.get() == 'Password':
			password.delete(0, "end")
			password.insert(0, '')
			password.config(show="*", fg="black")
	def pass_entry_out(e):
		if password.get() == '':
			password.config(show="", fg="gray")
			password.insert(0, "Password")

	# entry fields
	username = Entry(
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	username.insert(0, "Username")
	username.place(
		x=100, y=160,
		width=200, height=30
		)
	username.bind('<FocusIn>', user_entry_clicked)
	username.bind('<FocusOut>', user_entry_out)

	password = Entry(
		bd=4,
		fg="gray",
		bg="white",
		font=("Arial", 10)
		)
	password.insert(0, "Password")
	password.place(
		x=100, y=190,
		width=200, height=30
		)
	password.bind('<FocusIn>', pass_entry_clicked)
	password.bind('<FocusOut>', pass_entry_out)

	# buttons
	loginBtn = Button(
		text="ENTER",
		font=("Arial, 10"),
		command=lambda: goto_main(username.get(), password.get())
		)
	loginBtn.place(
		x=175, y=230,
		width=50, height=30
		)

	registerBtn = Button(
		text="REGISTER",
		font=("Arial, 7"),
		borderwidth=0,
		relief="flat",
		fg="blue",
		command=lambda: register()
		)
	registerBtn.place(
		x=175, y=260,
		width=50, height=30
		)

	window.resizable(False, False)
	window.mainloop()

	# database
	conn = sqlite3.connect("MaHomes.db")
	cur = conn.cursor()


	conn.commit()
	conn.close()


if __name__ == "__main__":
	login_gui()
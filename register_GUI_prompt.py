# asks user if parent or child

from tkinter import Button, Entry, Canvas, Tk
import register_GUI


def register(role):
	window.destroy()
	register_GUI.register_gui(role)

def prompt():
	global window
	window = Tk()
	window.title("Register Prompt")
	window.geometry("300x200")

	canvas = Canvas(window,
		height=300,
		width=200,
		bd=0
		)
	canvas.place(x=0,y=0)

	canvas.create_text(
		150, 50,
		text="Are you..     ",
		font=("Arial BOLD", 25)
		)

	parentBtn = Button(
		text="the Parent",
		font=("Arial, 10"),
		command=lambda: register("Parent")
		)
	parentBtn.place(
		x=100, y=90,
		width=80, height=30
		)

	childBtn = Button(
		text="the Child",
		font=("Arial, 10"),
		command=lambda: register("Child")
		)
	childBtn.place(
		x=100, y=125,
		width=80, height=30
		)

	window.resizable(False, False)
	window.mainloop()

if __name__ == "__main__":
	prompt()

# register in console
import login_console
import sqlite3
import random



def register():
	conn = sqlite3.connect('MaHomes.db')
	c = conn.cursor
	print("\n [REGISTER] ")

	# check role: (0 -> parent) (1 -> child)
	while True:
		checkRole = input("Are you the parent or child?: ")
		if checkRole.lower() == 'parent':
			role = 0
			break
		if checkRole.lower() == 'child':
			role = 1
			break
		print("  *Please enter 'Parent' or 'Child'.*")

	# show if role is parent
	if role == 0:
		# get random parent ID
		randID = random.randint(10000, 99999)

		# enter child id if exists
		childCount = int(input("Enter number of child: "))
		x = 1
		child = [0] * 100
		while x <= childCount:
			child[x]=input(f"Enter child ID of child {x}: ")
			print("  *Child added in list. Wait for child confirmation.*")
			x += 1

	#show if role is child
	if role == 1:
		# get random child ID
		randID = random.randint(10000, 99999)

		# enter parents id if exists
		mom = int(input("Enter mom parent ID (enter 0 if none): "))
		if mom == 0:
			print("  *Nothing has been added.*")
		else: print("  *Mom Added in list. Wait for parent confirmation.*")

		dad = int(input("Enter dad parent ID (enter 0 if none): "))
		if dad == 0:
			print("  *Nothing has been added.*")
		else: print("  *Dad Added in list. Wait for parent confirmation.*")

	username = input("Enter username: ")
	password = input("Enter password: ")
	firstName = input("Enter first name: ")
	lastName = input("Enter last name: ")
	gender = input("Enter gender: ")
	dob = input("Enter date of Birth: ")
	address = input("Enter address: ")
	contact = input("Enter contact number: ")

	if role == 0:
		c.execute("insert into parent values ('?', '?', '?', '?', '?', '?', '?', '?', '?')", randID,  username, password, firstName, lastName, gender, dob, address, contact)

	conn.commit()
	conn.close()

	print("  *Account created. You may login now.*")
	login_console.login()
			#checkFam = input(" ")
# main program section

def intro():
	print("+-+-+-+-+-+-+-+-+-+--+-+-+-+--+-+-+-+-+-+-+-+-+--+-+-+-+-+\n")
	print("-+-+-+-+- Manage your home with Home Manager App -+-+-+-+-\n")
	print("+-+-+-+-+-+-+-+-+-+--+-+-+-+--+-+-+-+-+-+-+-+-+--+-+-+-+-+\n")
	print("\n")
	main()

def main():
	print("                  Welcome [Raul Pig]!\n")
	while True:
		print(" Menu: [1]Alert  [2]Mail  [3]Tasks  [4]Account  [5]Guide\n")
		choice = input("Choose from menu the purpose of your visit: ")
		if choice == '1' or choice.lower() == 'alert':
			alert()
			break
		elif choice == '2' or choice.lower() == 'mail':
			mail()
			break
		elif choice == '3' or choice.lower() == 'tasks':
			tasks()
			break
		elif choice == '4' or choice.lower() == 'account':
			account()
			break
		elif choice == '5' or choice.lower() == 'guide':
			alert()
			break
		else:
			print("  Choice not accepted. Try again.")

# alert menu
def alert():
	print("[Alert]\n")

	

	choice = input("Choose from menu the purpose of your visit: ")
	if choice == 0:
		main()

# mail menu
def mail():
	print("[Mail]\n")
	choice = input("Choose from menu the purpose of your visit: ")
	if choice == 0:
		main()

# tasks menu
def tasks():
	print("[Tasks]\n")
	choice = input("Choose from menu the purpose of your visit: ")
	if choice == 0:
		main()

# account menu
def account():
	print("[Account]\n")
	print("First name: ")
	print("\n")
	print("Last name: ")
	print("\n")
	print("Username: ")
	print("\n")
	print("Password: ")
	print("\n")
	print("Gender: ")
	print("\n")
	print("Date of Birth: ")
	print("\n")
	print("Address: ")
	print("\n")
	print("Contact #: ")
	print("\n")
	print("Parent ID: ")
	print("\n")
	print("Your ID: ")
	print("\n")

	choice = input("Choose from menu the purpose of your visit: ")
	if choice == 0:
		main()

# guide menu
def guide():
	print("[Guide]\n")
	print("[Menu - Alert]   Shows important informations from mail or tasks.\n")
	print("                   i.e New appoint task received / Child finished his task\n")
	print("[Menu - Mail]    Shows messages received from family member\n")
	print("[Menu - Tasks]   Shows task lists placed by parent or received by child.\n")
	print("                 Parent can deploy tasks in here.\n")
	print("[Menu - Account] Shows user account information.\n")
	print("\n")
	main()


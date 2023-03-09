# database project
import main_console
import register_console

def intro():
	print("\n********** WELCOME TO HOME MANAGER APP **********\n")

	while True:
		checkLogin = input("Do you already have an account? [Y/N]: ")
		if checkLogin.upper() == 'Y':
			login()
			break
		if checkLogin.upper() == 'N':
			register_console.register()
			exit()
		print("  *Invalid Selection. Please try again!*")


def login():
	print("\n  [LOGIN] ")

	while True:
		username = input("Enter your username: ")
		password = input("Enter your password: ")

		if username == 'Raul':
			if password == 'Pig':
				print("\n  Account accepted. \n\n")
				main_console.intro()

		print("  *Wrong username or password. Enter again..*")


if __name__ == "__main__":
	intro()


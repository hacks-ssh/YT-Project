# Imports
import os
import colorama
from colorama import Fore
import time
import sys

# Functions
def menu():
	global onstart
	print(f"""{Fore.RED}
╔╦╗┬ ┬┬ ┌┬┐┬  ╔╦╗┌─┐┌─┐┬  
║║║│ ││  │ │   ║ │ ││ ││  
╩ ╩└─┘┴─┘┴ ┴   ╩ └─┘└─┘┴─┘

[0] EXIT
[1] IP Lookup
""")
  
  # Input
	command = input("User1@MultiTool>")
  
  # Checking To See What You Chose
	if command == "0":
		print("Exiting")
		time.sleep(1)
		sys.exit(0)
	elif command == "1":
		print("Coming Soon")
		time.sleep(1)
		onstart()

def onstart():
  # Clearing The Screen And Adding A Title
	os.system("cls && title Youtube Project")
	menu()

# On Startup
onstart()

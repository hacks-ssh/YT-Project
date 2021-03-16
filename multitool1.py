import sys
import time
import colorama
import os
from colorama import Fore
import webbrowser

user = input("Enter a new username: ")
password = input("Enter your password: ")

def main():
    os.system("cls && title YT Project")
    print(f'''
    ╦ ╦╔╦╗  ╔═╗┌─┐┬─┐ ┬┌─┐┌─┐┌┬┐
    ╚╦╝ ║   ╠═╝│ │├┬┘ │├┤ │   │ 
     ╩  ╩   ╩  └─┘┴└─└┘└─┘└─┘ ┴
     [0] Youtube
     [1] Instagram 
    ''')

    command = input(f"{user}@YT Project: ")

    if command == "0":
        webbrowser.open("https://www.youtube.com/channel/UC8w3Ycr3IBmbAz2SkaIxP_g")
        main()
    elif command == "1":
        webbrowser.open("https://www.instagram.com/solo_jakey/")
        main()
    else:
        print("Unknown command")
        os.system("cls && title YT Project")
        main()

if password == "YT":
    print("Logged in")
    time.sleep(1)
    main()
else:
    print("Wrong password exiting")
    exit()

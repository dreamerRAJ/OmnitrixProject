#!/usr/bin/python3

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f Sub-Zero 'FTP LOGIN'|lolcat -a -d 1 -F 0.5")
	os.system('echo "╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "|           Created By: Rajnish Kumar           |" | lolcat -a -d 1 -F 0.3')
	os.system('echo "┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')
	os.system('echo "[1] CHECK ANONYMOUS PRIVILEGES \n[2] FTP BRUTEFORCER\n[3] FTP LOGIN WITH USERNAME & PASSWORD\n\n[9] MAIN MENU\n[0] EXIT" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored("|> Select Your Option: ",'green',attrs=['bold'])))
	if option == 1:
		os.system('python3 anonftplogin.py && cd ..')

	elif option == 2:
		os.system('python3 ftpbrute.py && cd ..')

	elif option == 3:
		os.system('python3 ftplogin.py | lolcat -F 0.3 && cd ..')

	elif option == 9:
		os.system("cd .. && python3 omnitrix.py")

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()

	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		execute()
		
execute()


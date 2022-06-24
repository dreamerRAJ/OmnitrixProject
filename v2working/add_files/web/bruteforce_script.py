#!/usr/bin/python3

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f ascii_new_roman 'BRUTEFORCERS'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t╔─────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t|      Created By: Rajnish Kumar      |" | lolcat -a -d 1 -F 0.3')
	os.system('echo "\t┖─────────────────────────────────────┙\n\n" | lolcat -a -d 1')
	os.system('echo "[1] LOGIN PAGE BRUTEFORCER\n[2] SSH BRUTEFORCER\n[3] FTP BRUTEFORCER\n[4] DIRECTORY BRUTEFORCER\n\n[9] MAIN MENU\n[0] EXIT" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored("\n|> Select Your Option: ",'green',attrs=['bold'])))
	if option == 1:
		os.system('python3 login_brute_3.py && cd ..')

	elif option == 2:
		os.system('python3 bruteforcessh.py && cd ..')

	elif option == 3:
		os.system('python3 ftpbrute.py && cd ..')

	elif option == 4:
		os.system('python3 dir_bruteforce3.py && cd ..')

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

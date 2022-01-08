#!/usr/bin/python3

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f Graffiti 'NETWORK SCANNER'|lolcat -a -d 1")
	os.system('echo "           ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "           |           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "           ┖───────────────────────────────────────────────┙\n" | lolcat -a -d 1')
	os.system('echo "[1] Manual Port Scanner \n[2] Multiple Port Scanner\n[3] Automatic Port Scanner\n[4] Service Scanner\n[5] Network Vulnerability Scanner\n\n[9] Main Menu\n[0] Exit" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored(">>> Select Your Option: ",'yellow')))
	if option == 1:
		os.system('python3 man_portscanner.py && cd ..')

	elif option == 2:
		os.system('python3 multiportscanner.py && cd ..')

	elif option == 3:
		os.system('python3 auto_op_scan.py && cd ..')  #| lolcat -F 0.3')

	elif option == 4:
		os.system('python3 returnbanner.py && cd ..')

	elif option == 5:
		os.system('python3 vulnscan.py vulnbanner.txt && cd ..')

	elif option == 9:
		os.system("cd .. && python3 omnitrix.py")

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()

	else:
		print(colored("\n[-] Error! Select Correct Option","red"))
		input(colored("{#} Press Key To Continue . . .","green"))
		execute()

execute()

#coded and created by rajnish

#!/usr/bin/python3

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f Graffiti 'NETWORK SCANNER'|lolcat -a -d 1")
	os.system('echo "           ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "           |           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "           ┖───────────────────────────────────────────────┙\n" | lolcat -a -d 1')
	os.system('echo "[1] SINGLE PORT SCANNER \n[2] MULTIPLE PORT SCANNER\n[3] AUTO PORT SCANNER\n[4] SERVICE SCANNER\n[5] NETWORK VULNERABILITY SCANNER\n[6] NMAP INTENSE IP LIST SCANNER WITH OUTPUT\n\n[9] MAIN MENU\n[0] EXIT" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored("\n|> Select Your Option: ",'yellow',attrs=['bold'])))
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
		
	elif option == 6:
		os.system("./list_scanner.sh | lolcat -F 0.3 && cd ..")

	elif option == 9:
		os.system("cd .. && python3 omnitrix.py")

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit(0)

	else:
		print(colored("\n[-] Error! Select Correct Option","red"))
		input(colored("{#} Press Key To Continue . . .","green"))
		execute()

execute()

#coded and created by rajnish

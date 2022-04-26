#!/usr/bin/python3

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f swampland 'SPOOFERS'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t  ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t  |           Created By: Rajnish Kumar           |" | lolcat -a -d 1 -F 0.3')
	os.system('echo "\t  ┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')
	os.system('echo "[1] MAC ADDRESS CHANGER \n[2] ARP SPOOFER\n[3] SYN FLOOD DoS ATTACK\n\n[9] MAIN MENU\n[0] EXIT" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored("\n|> Select Your Option: ",'green',attrs=['bold'])))
	if option == 1:
		os.system('python3 macchanger.py && cd ..')

	elif option == 2:
		os.system('python3 arpspoofer.py && cd ..')

	elif option == 3:
		os.system('python3 synflood.py && cd ..')

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

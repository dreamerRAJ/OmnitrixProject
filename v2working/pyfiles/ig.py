#!/usr/bin/python

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f broadway_kb 'GATHER INFO'|lolcat -a -d 1")
	os.system('echo "     ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "     |           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "     ┖───────────────────────────────────────────────┙\n" | lolcat -a -d 1')
	os.system('echo "[1] WHOIS \n[2] NSLOOKUP\n[3] RECON-NG TOOL\n[4] NETDISCOVER\n[5] OPEN SOURCE INFORMATION GATHERING\n\n[9] MAIN MENU\n[0] EXIT" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored("\n|> Select Your Option: ",'yellow',attrs=['bold'])))
	if option == 1:
		os.system('python3 who_is.py && cd ..')

	elif option == 2:
		os.system('python3 nslookup.py && cd ..')

	elif option == 3:
		os.system('recon-ng | lolcat -F 0.3 && cd ..')
		execute()

	elif option == 4:
		os.system('netdiscover | lolcat -F 0.3 && cd ..')
		execute()

	elif option == 5:
		os.system('python3 open_source.py && cd ..')

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

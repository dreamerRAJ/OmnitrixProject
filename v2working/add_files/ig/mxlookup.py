#!/usr/bin/python

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f Fuzzy 'MXTOOLBOX'|lolcat -a -d 1")
	os.system('echo "  ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "  |           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "  ┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')


def domains():
	execute()
	domain=input(colored("|> ENTER THE DOMAIN TO ANALYZE WITH MXTOOLBOX: ",'yellow',attrs=['bold']))
	os.system('echo "OPENING . . . PLEASE WAIT!!!"|lolcat -a -i -d 50 -F 0.5')
	os.system("firefox https://mxtoolbox.com/SuperTool.aspx?action=mx%3a{}&run=toolpage".format(domain))
	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Check Again\n[2] Go Back\n[3] Gather Info\n[4] Main Menu\n[5] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 mxlookup.py && cd ..')

	elif option == 2:
		os.system('python3 open_source.py && cd ..')

	elif option == 3:
		os.system('python3 ig.py && cd ..')

	elif option == 4:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 5:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()



domains()

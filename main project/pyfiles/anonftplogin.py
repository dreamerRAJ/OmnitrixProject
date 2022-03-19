#!/usr/bin/python3

import ftplib
import os
from termcolor import colored, cprint

def anonlogin(hostname):
	try:
		anonftp=ftplib.FTP(hostname)
		anonftp.login('anonymous','anonymous')
		print(colored("[+] {} FTP Anonymous Login Allowed.\n".format(hostname),'green',attrs=['bold']))
		#print(colored("[+] Welcome To FTP Route Of {}.".format(hostname),'green', attrs=['bold','blink']))
		print(colored("-> FTP Service Version: {}".format(anonftp.getwelcome()),'green', attrs=['bold']))
		print(colored("\n[$] Username: anonymous\n[$] Password: anonymous".format(hostname),'green',attrs=['reverse','bold']))
		anonftp.quit()
		return True
	except(Exception, e):
		print(colored("[-] {} FTP Anonymous Login Not Allowed".format(hostname),'on_red'))

def execute():
	os.system("clear")
	os.system("figlet -f Digital 'FTP ANONYMOUS LOGIN CHECK'|lolcat -a -d 1")
	os.system('echo "╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "|           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')
	
def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Check Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 anonftplogin.py && cd ..')

	elif option == 2:
		os.system('python3 ftpscript.py && cd ..')

	elif option == 3:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 4:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

execute()
host=input(colored("|> Enter the IP Address: ",'green', attrs=["bold"]))
anonlogin(host)
menu()
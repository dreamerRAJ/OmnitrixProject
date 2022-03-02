#!/usr/bin/python3

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f 3D-ASCII 'HASHERS'|lolcat -a -d 1 -F 0.5")
	os.system('echo "	╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "	|           Created By: Rajnish Kumar           |" | lolcat -a -d 1 -F 0.5')
	os.system('echo "	┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')

def main():
	os.system('echo "[1] HASHING IN VARIETIES\n[2] MD5 CRACKER\n[3] SHA1 HASH CRACKER\n[4] SHA224 HASH CRACKER\n[5] SHA256 or SHA2 HASH CRACKER\n[6] SHA512 HASH CRACKER\n\n[9] MAIN MENU\n[0] Exit" |lolcat -a -d 1 -F 0.3')
	option = int(input(colored("|> Select Your Option: ",'green',attrs=['bold'])))
	if option == 1:
		os.system('python3 hasher.py && cd ..')

	elif option == 2:
		os.system('python3 md5brute.py && cd ..')

	elif option == 3:
		os.system('python3 sha1hash.py && cd ..')

	elif option == 4:
		os.system('python3 sha224hash.py && cd ..')

	elif option == 5:
		os.system('python3 sha256hash.py && cd ..')
		
	elif option == 6:
		os.system('python3 sha512hash.py && cd ..')

	elif option == 9:
		os.system("cd .. && python3 omnitrix.py")

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()

	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		execute()
#	menu()


execute()
main()

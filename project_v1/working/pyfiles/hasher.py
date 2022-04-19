#!/usr/bin/python3

import hashlib
from termcolor import colored
import os

def main():
	hashvalue = input(colored("\n|> Enter A String To Hash: ",'yellow',attrs=['bold']))

	hashobj1 = hashlib.md5()
	hashobj1.update(hashvalue.encode())
	print(colored("\n\n[*] MD5: {}".format(hashobj1.hexdigest()),'green',attrs=['bold']))

	hashobj2 = hashlib.sha1()
	hashobj2.update(hashvalue.encode())
	print(colored("[*] SHA1: {}".format(hashobj2.hexdigest()),'grey',attrs=['bold']))

	hashobj3 = hashlib.sha224()
	hashobj3.update(hashvalue.encode())
	print(colored("[*] SHA224: {}".format(hashobj3.hexdigest()),'blue',attrs=['bold']))

	hashobj4 = hashlib.sha256()
	hashobj4.update(hashvalue.encode())
	print(colored("[*] SHA256: {}".format(hashobj4.hexdigest()),'cyan',attrs=['bold']))

	hashobj5 = hashlib.sha512()
	hashobj5.update(hashvalue.encode())
	print(colored("[*] SHA512: {}".format(hashobj5.hexdigest()),'magenta',attrs=['bold']))


def menu():
	option = int(input(colored("\n\n{#} Do you want to:\n[1] Use Hasher Again\n[2] MD5 Decrypter\n[3] SHA1 Decrypter\n[4] SHA224 HASH CRACKER\n[5] SHA256 or SHA2 HASH CRACKER\n[6] SHA512 HASH CRACKER\n\n[9] Main Menu\n[0] Exit\n|>Select Your Choice: ",'yellow', attrs=['bold'])))
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
		os.system('cd .. && python3 omnitrix.py')

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{#} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

print("\n\n")
os.system("figlet -f Digital 'HASHING IN VARIETIES'|lolcat -a -d 1 -F 0.5")
main()
menu()
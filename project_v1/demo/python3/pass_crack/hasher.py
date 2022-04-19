
#!/usr/bin/python

import hashlib
from termcolor import colored
import os

def main():
	hashvalue = input("|> Enter A String To Hash: ")

	hashobj1 = hashlib.md5()
	hashobj1.update(hashvalue.encode())
	print("MD5: "+hashobj1.hexdigest())

	hashobj2 = hashlib.sha1()
	hashobj2.update(hashvalue.encode())
	print("SHA1: "+hashobj2.hexdigest())

	hashobj3 = hashlib.sha224()
	hashobj3.update(hashvalue.encode())
	print("SHA224: "+hashobj3.hexdigest())

	hashobj4 = hashlib.sha256()
	hashobj4.update(hashvalue.encode())
	print("SHA256: "+hashobj4.hexdigest())

	hashobj5 = hashlib.sha512()
	hashobj5.update(hashvalue.encode())
	print("SHA512: "+hashobj5.hexdigest())


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

main()
menu()
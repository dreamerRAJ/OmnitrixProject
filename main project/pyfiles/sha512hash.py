#!/usr/bin/python3

from urllib.request import urlopen
import hashlib
from termcolor import colored
import os

sha1hash = input(colored("|> Enter SHA512 Hash Value: ",'yellow',attrs=["bold"]))

#passlist = str(urlopen("https://raw.githubusercontent.com/dreamer1eh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')

passlist = str(urlopen("https://raw.githubusercontent.com/dreamer1eh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").read(), 'utf-8')

def main():
	for password in passlist.split('\n'):
		hashguess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
		if hashguess == sha1hash:
			print(colored("[+] The password is: "+str(password),'green',attrs=["bold"]))
			break
			menu()
			#quit()
		else:
			print(colored("[-] Password guess: "+str(password)+" does not match, trying next . . .","red",attrs=["bold"]))

	print(colored("\n[!] If You Didn\'t Get The Password, Then Password Is Not In The Password List [!]",'cyan',attrs=["blink"]))
	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Use It Again\n[2] Hasher\n[3] Go Back\n[4] Main Menu\n[0] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 sha256hash.py && cd ..')
		
	elif option == 2:
		os.system('python3 hasher.py && cd ..')

	elif option == 3:
		os.system('python3 hashscript.py && cd ..')

	elif option == 4:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{#} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()


main()

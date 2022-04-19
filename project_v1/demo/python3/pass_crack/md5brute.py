
#!/usr/bin/python

from termcolor import colored
import hashlib
import os

def tryOpen(wordlist):
	global pass_file
	try:
		pass_file = open(wordlist, "r")
	except:
		print("[-] No Such File At That Path!")


pass_hash = input("|> Enter MD5 Hash Value: ")
wordlist = input("|> Enter Path To The Password File: ")
tryOpen(wordlist)

def main():
	for word in pass_file:
		print(colored("[*] Trying: "+word.strip("\n"),'blue'))
		enc_wrd = word.encode('utf-8')
		md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

		if md5digest == pass_hash:
			print(colored("[+] Password Found: "+word,'green',attrs=["bold"]))
			exit(0)

	print("[!!] Password Not In List!")

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
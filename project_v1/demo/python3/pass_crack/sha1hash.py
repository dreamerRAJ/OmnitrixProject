
#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input(colored("|> Enter SHA1 Hash Value: ",'yellow',attrs=["bold"]))

#passlist = str(urlopen("https://raw.githubusercontent.com/dreamer1eh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')

passlist = str(urlopen("https://raw.githubusercontent.com/dreamer1eh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").read(), 'utf-8')

def main():
	for password in passlist.split('\n'):
		hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
		if hashguess == sha1hash:
			print(colored("[+] The password is: "+str(password),'green',attrs=["bold"]))
			quit()
		else:
			print(colored("[-] Password guess: "+str(password)+" does not match, trying next . . .","red",attrs=["bold"]))

	print("Password not in the passwordlist")
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


main()
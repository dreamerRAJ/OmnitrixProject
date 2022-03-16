#!/usr/bin/python

import os
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f Cybermedium ' OPEN SOURCE'|lolcat -a -d 1")
	os.system('echo "       ╔──────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "       |        Created By: Rajnish Kumar         |" | lolcat -a -d 1')
	os.system('echo "       ┖──────────────────────────────────────────┙\n" | lolcat -a -d 1')
	print(colored("[!] ALL OPTIONS USED HERE WILL OPEN YOUR DEFAULT BROWSER, SOMETIMES BROWSER OPENING SPEED DEPENDS ON YOUR PROCESSING SPEED\n",'red',attrs=['bold']))
	os.system('echo "[1] SIMILAR WEB \n[2] MXTOOLBOX\n[3] NETCRAFT SITE REPORT\n[4] SHODAN (FOR DOMAIN AND IP)\n[5] SUBDOMAIN FINDER\n\n[8] GATHER INFO\n[9] MAIN MENU\n[0] EXIT" |lolcat -a -d 1 -F 0.3')

	option = int(input(colored("\n|> Select Your Option: ",'yellow',attrs=['bold'])))
	if option == 1:
		os.system('python3 similar_web.py && cd ..')

	elif option == 2:
		os.system('python3 mxlookup.py && cd ..')

	elif option == 3:
		os.system('python3 netcraft.py && cd ..')  #| lolcat -F 0.3')

	elif option == 4:
		os.system('python3 shodan.py && cd ..')

	elif option == 5:
		os.system('firefox https://subdomainfinder.c99.nl/  && cd ..')
		execute()

	elif option == 8:
		os.system("python3 ig.py && cd ..")

	elif option == 9:
		os.system("cd .. && python3 omnitrix.py")

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit(0)

	else:
		print(colored("\n[-] Error! Select Correct Option","red"))
		input(colored("{#} Press Key To Continue . . .","green"))
		execute()

execute()

#coded and created by rajnish

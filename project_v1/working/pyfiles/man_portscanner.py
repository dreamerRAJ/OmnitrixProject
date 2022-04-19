#!/usr/bin/python3

import socket
import os
from termcolor import colored, cprint

os.system("clear")
os.system("figlet -f miniwi '     Manual Port Scanner' | lolcat")
os.system('echo "\t ╔───────────────────────────────────────╗" | lolcat -a -d 1')
os.system('echo "\t |       Created By: Rajnish Kumar       |" | lolcat -a -d 1')
os.system('echo "\t ┖───────────────────────────────────────┙" | lolcat -a -d 1') 



host = input(colored("|> Enter IP Address: ",'green',attrs=['bold']))
port = int(input(colored("|> Enter Port: ",'green',attrs=['bold'])))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def portscanner(port):
	if sock.connect_ex((host,port)):
		cprint("\n[-] Port {} is closed.".format(port), 'green', 'on_red', attrs=['bold'])
	else:
		cprint("\n[+] Port {} is open.".format(port), 'red', 'on_cyan', attrs=['bold'])
	menu()

def menu():
	option = int(input(colored("\n\n=> Do you want to:\n[1] Scan Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow',attrs=['bold'])))
	if option == 1:
		os.system('python3 man_portscanner.py && cd ..')

	elif option == 2:
		os.system('python3 networkscanner.py && cd ..')

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

portscanner(port)


#Coded by Rajnish

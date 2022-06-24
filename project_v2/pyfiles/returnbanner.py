#!/usr/bin/python3

import socket
from termcolor import colored, cprint
import os

os.system("clear")
os.system("figlet -f Avatar 'SERVICE SCANNER' | lolcat")
os.system('echo " ╔───────────────────────────────────────╗" | lolcat -a -d 1')
os.system('echo " |       Created By: Rajnish Kumar       |" | lolcat -a -d 1')
os.system('echo " ┖───────────────────────────────────────┙" | lolcat -a -d 1')


def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(3)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	ip = input(colored("|> Enter Target IP: ","green",attrs=['bold']))
	cprint("\n{#} Super Scanning is under progress . . .\n", 'red', attrs=['bold', 'blink'])
#	print("\n{#} Super Scanning is under progress . . .\n")
	for port in range(1,65535):
		banner = retBanner(ip,port)
		if banner:
			print("{}/{} : {}".format(ip,port,banner.strip(b'\n\r')))

def menu():
	option = int(input(colored("\n\n=> Do you want to:\n[1] Scan Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 returnbanner.py && cd ..')

	elif option == 2:
		os.system('python3 networkscanner.py && cd ..')

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
cprint("\n{#} Super Scanning Completed.\n", 'green', attrs=['bold', 'blink'])
menu()
#print(colored("\n{#} Super Scanning Completed.",'green'))

#!/usr/bin/python

from scapy.all import *
import os
from termcolor import colored


def banner():
	os.system("clear")
	os.system("figlet -f Braced ' DNS QUERY\n  SPOOFER'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t  ╔───────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t  |       Created By: Rajnish Kumar       |" | lolcat -a -d 1')
	os.system('echo "\t  ┖───────────────────────────────────────┙\n\n" | lolcat -a -d 1')


def findDNS(p):   #p = parameter of the function
	try:
		if p.haslayer(DNS):
			print(p[IP].src, p[DNS].summary())
	except KeyboardInterrupt:
		menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Run Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 dns_query.py && cd ..')

	elif option == 2:
		os.system('python3 spooferscript.py && cd ..')

	elif option == 3:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 4:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

banner()
print(colored("\n{#} Spoofing Started . . .\n", 'green', attrs=['bold', 'blink']))
sniff(prn=findDNS)

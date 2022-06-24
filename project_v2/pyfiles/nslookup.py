#!/usr/bin/python

import dns
import dns.resolver
import os
from termcolor import colored


def execute():
	os.system("clear")
	os.system("figlet -f Cricket 'N S L OO K UP'|lolcat -a -d 1")
	os.system('echo "  \t\t╔────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "  \t\t|      Created By: Rajnish Kumar     |" | lolcat -a -d 1')
	os.system('echo "  \t\t┖────────────────────────────────────┙\n\n" | lolcat -a -d 1')

def main():
	execute()
	domain = input(colored("|> ENTER A DOMAIN FOR NSLOOKUP: ",'cyan',attrs=['bold']))
	result = dns.resolver.resolve('{}'.format(domain),'A')
	result1 = dns.resolver.resolve('{}'.format(domain),'AAAA')
	result2 = dns.resolver.resolve('{}'.format(domain),'NS')
	result3 = dns.resolver.resolve('{}'.format(domain),'MX')
	result4 = dns.resolver.resolve('{}'.format(domain),'SOA')
	print("")
	for ipval in result:
		print(colored('[+] A RECORD (IPv4): {}'.format(ipval.to_text()),'green',attrs=['bold']))
	print("")
	for ipval in result1:
		print(colored('[+] AAAA RECORD (IPv6): {}'.format(ipval.to_text()),'yellow',attrs=['bold']))
	print("")
	for ipval in result2:
		print(colored('[+] NS RECORD: {}'.format(ipval.to_text()),'cyan',attrs=['bold']))
	print("")
	for ipval in result3:
		print(colored('[+] MX RECORD: {}'.format(ipval.to_text()),'magenta',attrs=['bold']))
	print("")
	for ipval in result4:
		print(colored('[+] SOA RECORD: {}'.format(ipval.to_text()),'red',attrs=['bold']))

	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Check Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 nslookup.py && cd ..')

	elif option == 2:
		os.system('python3 ig.py && cd ..')

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

main()
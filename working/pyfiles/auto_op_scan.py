
#!/usr/bin/python3

import nmap
import os
from termcolor import colored,cprint

scanner = nmap.PortScanner()


os.system("clear")
os.system("figlet -f Chunky 'AUTO PORT SCANNER'|lolcat -a -d 1")
os.system('echo "           ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
os.system('echo "           |           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
os.system('echo "           ┖───────────────────────────────────────────────┙\n" | lolcat -a -d 1')

ip_addr = input(colored("|> Enter The IP Address You Want To Scan: ",'yellow',attrs=['bold']))

resp = int(input(colored("\n=> SCAN METHODS:\n[1] VERBOSE SCAN\n[2] SYN ACK SCAN\n[3] UDP SCAN\n[4] COMPREHENSIVE SCAN\n\n>>> Select Your Option: ",'green', attrs=['bold'])))

def net_scan():
	if resp == 1: #verbose
		print(colored("[*] NMAP VERSION: {}".format(scanner.nmap_version()),'blue',attrs=['bold','reverse']))
		scanner.scan(ip_addr, '1-10000', '-v')
		print(scanner.scaninfo())
		print(colored("[#] IP STATUS: {}".format(scanner[ip_addr].state()), 'red','on_green',attrs=['bold']))
		print(scanner[ip_addr].all_protocols())
		print(colored("[+] OPEN PORTS: {}".format(scanner[ip_addr]['tcp'].keys()),'blue','on_white',attrs=['bold']))

	elif resp == 2: #SYN ACK SCAN
		print(colored("[*] NMAP VERSION: {}".format(scanner.nmap_version()),'blue',attrs=['bold','reverse']))
		scanner.scan(ip_addr, '1-10000', '-v -sS')
		print(scanner.scaninfo())
		print(colored("[#] IP STATUS: {}".format(scanner[ip_addr].state()), 'red','on_green',attrs=['bold']))
		print(scanner[ip_addr].all_protocols())
		print(colored("[+] OPEN PORTS: {}".format(scanner[ip_addr]['tcp'].keys()),'white','on_magenta',attrs=['bold']))

	elif resp == 3: #UDP SCAN
		print(colored("[*] NMAP VERSION: {}".format(scanner.nmap_version()),'blue',attrs=['bold','reverse']))
		scanner.scan(ip_addr, '1-10000', '-v -sU')
		print(scanner.scaninfo())
		print(colored("[#] IP STATUS: {}".format(scanner[ip_addr].state()), 'red','on_green',attrs=['bold']))
		print(scanner[ip_addr].all_protocols())
		print(colored("[+] OPEN PORTS: {}".format(scanner[ip_addr]['tcp'].keys()),'white','on_magenta',attrs=['bold']))

	elif resp == 4: #COMPREHENSIVE SCAN
		print(colored("[*] NMAP VERSION: {}".format(scanner.nmap_version()),'blue',attrs=['bold','reverse']))
		scanner.scan(ip_addr, '1-10000', '-v -sS -sV -sC -A -O')
		print(scanner.scaninfo())
		print(colored("[#] IP STATUS: {}".format(scanner[ip_addr].state()), 'red','on_green',attrs=['bold']))
		print(scanner[ip_addr].all_protocols())
		print(colored("[+] OPEN PORTS: {}".format(scanner[ip_addr]['tcp'].keys()),'white','on_magenta',attrs=['bold']))

	else:
		print(colored("[-] Please Enter A Valid Option . . .",'red',attrs=['bold','blink']))

	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] SCAN AGAIN\n[2] GO BACK\n[3] MAIN MENU\n[4] EXIT\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 auto_op_scan.py && cd ..')

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

net_scan()

#!/usr/bin/python

import subprocess
from termcolor import colored
import os

def execute():
	os.system("clear")
	os.system("figlet -f Shadow ' MAC CHANGER'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t  ╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t  |           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "\t  ┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')

def change_mac_addr(interface,mac):
	os.system("ifconfig {} down".format(interface))
	os.system("ifconfig {} hw ether {}".format(interface,mac))
	os.system("ifconfig {} up".format(interface))
	
	#subprocess.call(["ifconfig",interface,"down"])
	#subprocess.call(["ifconfig",interface,"hw","ether",mac])
	#subprocess.call(["ifconfig",interface,"up"])

def main():
	execute()
	print(colored("[*] LIST OF YOUR NETWORK INTERFACES\n",'cyan', attrs=['bold']))
	os.system("nmcli device status")
	print("\n")
	interface = str(input(colored("|> Enter Network Interface To Change Mac Address On: ",'yellow', attrs=['bold'])))
	new_mac_addr = str(input(colored("|> Enter Mac Address To Change: ",'yellow', attrs=['bold'])))

#	before_change = subprocess.check_output(["ifconfig",interface])
#	change_mac_addr(interface,new_mac_addr)
#	after_change = subprocess.check_output(["ifconfig",interface])

	print("Device Mac Address: ")
	before_change = os.system("cat /sys/class/net/{}/address".format(interface,interface))
	change_mac_addr(interface,new_mac_addr)
	after_change = os.system("cat /sys/class/net/{}/address".format(interface))


#	mac_before_change = str(os.system("cat /sys/class/net/{}/address".format(interface)))
#	before_change = subprocess.check_output(["cat /sys/class/net/{}/address".format(interface)])
#	before_change = mac_before_change
#	change_mac_addr(interface,new_mac_addr)
#	after_change = subprocess.check_output(["cat /sys/class/net/{}/address".format(interface)])
#	mac_after_change = str(os.system("cat /sys/class/net/{}/address".format(interface)))
#	after_change = mac_after_change

#	if before_change == after_change:
#		print(colored("[-] Failed To Change MAC Address To: {}".format(new_mac_addr),'red', attrs=['bold']))
	#elif before_change != after_change:
	#	print(colored("[+] MAC Address Changed To {} On Interface {}".format(new_mac_addr,interface),'green', attrs=['bold']))
#	else:
#		print(colored("[+] MAC Address Changed To {} On Interface {}".format(new_mac_addr,interface),'green', attrs=['bold']))

	if before_change != after_change:
		print(colored("[+] MAC Address Changed To {} On Interface {}".format(new_mac_addr,interface),'green', attrs=['bold']))
	else:
		print(colored("[-] Failed To Change MAC Address To: {}".format(new_mac_addr),'red', attrs=['bold']))

	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Change Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 macchanger.py && cd ..')

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
	
main()

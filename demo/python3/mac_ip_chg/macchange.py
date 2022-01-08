#!/usr/bin/python

import subprocess
from termcolor import colored, cprint

def change_mac_address(interface,mac):
	subprocess.call(["ifconfig ",interface," down"])
	subprocess.call(["ifconfig ",interface," hw ","ether ",mac])
	subprocess.call(["ifconfig ",interface," up"])


def main():
	interface = input(colored("=> Enter Interface To Change Mac Address On: ",'yellow'))
	new_mac_address = input(colored("=> Enter The Mac Address To Change It: ",'yellow'))

	before_change = subprocess.check_output(["ifconfig " + interface])
	change_mac_address(interface,new_mac_address)
	after_change = subprocess.check_output(["ifconfig " + interface])

	if before_change == after_change:
		print("[-] Failed To Change MAC Address To: "+new_mac_address)
	else:
		print("[+] MAC Address Changed To: " + new_mac_address + " On Interface " +interface)

#main()
if __name__ == '__main__':
	main()

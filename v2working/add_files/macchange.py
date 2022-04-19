#!/usr/bin/python

import subprocess
from termcolor import colored


def change_mac_addr(interface,mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])

def main():
	interface = str(input("[*] Enter Network Interface To Change Mac Address On: "))
	new_mac_addr = str(input("[*] Enter Mac Address To Change: "))

	before_change = subprocess.check_output(["ifconfig",interface])
	change_mac_addr(interface,new_mac_addr)
	after_change = subprocess.check_output(["ifconfig",interface])

	if before_change == after_change:
		print(colored("[-] Failed To Change MAC Address To: {}".format(new_mac_addr),'red'))
	else:
		print(colored("[+] MAC Address Changed To {} On Interface {}".format(new_mac_addr,interface),'green'))

main()

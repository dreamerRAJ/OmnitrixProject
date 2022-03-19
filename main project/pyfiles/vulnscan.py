#!/usr/bin/python3

import socket
import os
import sys
from termcolor import colored

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	f = open(filename, "r")
	for line in f.readlines():
		if line.strip("\n") is banner:
			print("[+] Server is vulnerable: {}".format(banner.strip("\n")))

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print("[-] File Doesn't Exist!")
			exit(0)
		if not os.access(filename, os.R_OK):
			print("[-] Access Denied!")
			exit(0)
	else:
		print("[-] Usage: {} <vuln filename>".format(str(sys.argv[0])))
		exit(0)
	portlist = [21,22,23,25,53,80,111,135,139,443,445,512,513,514,1524]
	for x in range(1,9):
		ip = "192.168.0.10" + str(x)
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print("{}/{} : {}".format(ip,port,banner))
				checkVulns(banner, filename)

	menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] SCAN AGAIN\n[2] GO BACK\n[3] MAIN MENU\n[4] EXIT\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 vulnscan.py vulnbanner.txt && cd ..')

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

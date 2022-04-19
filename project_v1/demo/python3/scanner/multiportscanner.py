#!/usr/bin/python3

from socket import *
import os
from threading import *
from termcolor import colored, cprint

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print(colored("[+] {}/tcp Open".format(tgtPort),'green'))
	except:
		print(colored("[-] {}/tcp Closed".format(tgtPort),'red'))
	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print("Can't Resolve the hostname {}".format(tgtHost))
	try:
		tgtName = gethostbyaddr(tgtIP)
		print(colored("[*] Scan Results For: " + tgtName[0],'cyan'))
	except:
		print(colored("[*] Scan Results For: " + tgtIP, 'cyan'))
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	os.system("clear")
	os.system("figlet -f Cricket 'Multi-Port Scanner' | lolcat -a -d 2 -F 0.5")
	tgtHost = input(colored("Enter IP Address: ",'yellow'))
	tgtPorts = input(colored("Port Numbers For Scanning (separate using comma ','): ",'yellow')).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		exit(0)
	portScan(tgtHost,tgtPorts)


if __name__ == '__main__':
	main()

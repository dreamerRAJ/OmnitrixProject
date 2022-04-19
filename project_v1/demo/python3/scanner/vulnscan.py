
#!/usr/bin/python

import socket
import os
import sys

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
			print("[+] Server is vulnerable: {}".format(banner)) #.strip("\n")))

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
	portlist = [21,22,23,25,80,443,445]
	for x in range(1,6):
		ip = "192.168.0.10" + str(x)
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print("{}/{} : {}".format(ip,port,banner))
				checkVulns(banner, filename)

main()

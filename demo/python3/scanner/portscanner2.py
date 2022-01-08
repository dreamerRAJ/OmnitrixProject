
#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

host = input("[#] Enter IP Address: ")


def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("[-] Port {} is closed.".format(port),'red'))
	else:
		print(colored("[+] Port {} is open.".format(port), 'green'))

for port in range(1,1000):
	portscanner(port)

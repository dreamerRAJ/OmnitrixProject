
#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = input(colored("[#] Enter IP Address: ",'green'))
port = int(input(colored("[#] Enter Port: ",'green')))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print("[-] Port {} is closed.".format(port))
	else:
		print("[+] Port {} is opened.".format(port))


portscanner(port)

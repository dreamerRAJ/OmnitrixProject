#port scanner- input host and port both

#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

host = raw_input("[#] Enter IP Address: ")
port = int(raw_input("[#] Enter Port: "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print "[-] Port %d is closed."%(port)
	else:
		print "[+] Port %d is open."%(port)


portscanner(port)

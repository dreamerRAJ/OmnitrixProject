#1000 port scanner input ip address only. Output - Long List of port open or closed only.

#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

host = raw_input("[#] Enter IP Address: ")


def portscanner(port):
	if sock.connect_ex((host,port)):
		print "[-] Port %d is closed."%(port)
	else:
		print "[+] Port %d is open."%(port)

for port in range(1,1000):
	portscanner(port)

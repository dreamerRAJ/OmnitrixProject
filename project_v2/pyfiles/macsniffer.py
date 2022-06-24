#!/usr/bin/python

import socket
from struct import *

class tcolors:
	DEST_C = '\033[92m' #GREEN
	SRC_C = '\033[93m' #YELLOW
	PRO_C = "\033[36m" #CYAN
    	RESET = '\033[0m' #RESET COLOR
    	BOLD = "\033[1m"  #BOLD


def eth_addr(a):
	b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
	return b

try:
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
	print("ERROR ON CREATING SOCKET OBJECT")
	exit(0)

while True:
	packet = s.recvfrom(65535)
	packet = packet[0]

	eth_length = 14
	eth_header = packet[:eth_length]

	eth = unpack('!6s6sH',eth_header)
	eth_protocol = socket.ntohs(eth[2])
#	print("\n[+] Destination MAC: {}\t[+] Source MAC: {}\t[+] Protocol: {}".format(eth_addr(packet[0:6]), eth_addr(packet[6:12]), eth_protocol))
	print(tcolors.BOLD + tcolors.DEST_C +"\n[+] Destination MAC: {}  |".format(eth_addr(packet[0:6])) + tcolors.RESET + tcolors.BOLD + tcolors.SRC_C +"  [+] Source MAC: {}  |".format(eth_addr(packet[6:12])) + tcolors.RESET + tcolors.BOLD + tcolors.PRO_C + "  [+] Protocol: {}".format(eth_protocol) + tcolors.RESET)

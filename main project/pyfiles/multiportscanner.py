#!/usr/bin/python3

from socket import *
import os
from threading import *
from termcolor import colored, cprint
from pynput.keyboard import Key, Controller

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
	tgtHost = input(colored("|> Enter IP Address: ",'yellow',attrs=['bold']))
	tgtPorts = input(colored("|> Port Numbers For Scanning (separate using comma ','): ",'yellow',attrs=['bold'])).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		exit(0)
	portScan(tgtHost,tgtPorts)
	keyboard = Controller()
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	menu()

def menu():
	option = int(input(colored("\nDo you want to:\n[1] Scan Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 multiportscanner.py && cd ..')

	elif option == 2:
		os.system('python3 networkscanner.py && cd ..')

	elif option == 3:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 4:
		os.system('echo "Good Bye! Have A Great Day . . ." | lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{#} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

#if __name__ == '__main__':
#	main()
main()
menu()

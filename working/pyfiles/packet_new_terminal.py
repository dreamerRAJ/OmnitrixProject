#!/usr/bin/python3

import subprocess
import os
from termcolor import colored, cprint

cprint("WARNING: DO NOT CLOSE USING 'CTRL+Z' OR 'CTRL+C', ONLY CLOSE USING CROSS (x) ON TERMINAL WINDOW",'red',attrs=['bold'])
os.system('echo "PROCESSING . . ."|lolcat -a -i -d 50 -F 0.5')

subprocess.call(['xterm', '-e', 'python packet_sniffer.py'])
os.system('echo "\n\nCLOSING . . ."|lolcat -a -i -d 50 -F 0.5')

menu()


def menu():
	option = int(input(colored("\n\nDo you want to:\n[1] Analyze Again\n[2] Main Menu\n[0] Exit\n\n>>>Select Your Choice: ",'yellow', attrs=['bold'])))
	if option == 1:
		os.system('python3 packet_new_terminal.py && cd ..')

	elif option == 2:
		os.system('cd .. && python3 omnitrix.py')

	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."| lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("\n[!] Error! Select Correct Option","red", attrs=['bold', 'blink']))
		input(colored("\n{|>} Press Key To Continue . . .","green"))
		os.system("clear")
		menu()

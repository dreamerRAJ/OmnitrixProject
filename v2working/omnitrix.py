import os
from termcolor import colored


def banner():
	os.system("figlet -f Poison 'OMNITRIX'|lolcat -a -d 2 -F 0.5")
#	os.system('echo "\t\t\t\t\t\t\t\tv2.0"|lolcat -a -d 1 -F 1.5')
#os.system("figlet -f Digital '						COMBO OF PEN-TESTING TOOLS' | lolcat -a -d 1")
#	os.system("figlet -f threepoint ' Created By: Rajnish Kumar' | lolcat -a -d 1 -F 0.3")
	execute()

def execute():
	os.system('echo "         ╔──────────────────────────────────────────────╗" | lolcat -a -d 1 -F 0.2')
	os.system('echo "         |  OMNITRIX - COMBO OF PEN-TESTING TOOLS v2.0  |" | lolcat -a -d 1 -F 0.5')
	os.system('echo "         |           CREATED BY \xa9 RAJNISH KUMAR         |" | lolcat -a -d 1 -F 0.5')
	os.system('echo "         ┖──────────────────────────────────────────────┙" | lolcat -a -d 1 -F 0.2')

	os.system('echo "\n[1] INFORMATION GATHERING\n[2] OPEN SOURCE INFORMATION GATHERING\n[3] NETWORK SCANNER\n[4] SSH LOGIN\n[5] FTP LOGIN\n[6] HASH CRACKER\n[7] NETWORK ANALYZER\n[8] SNIFFERS & SPOOFERS\n[9] BRUTEFORCERS\n[10] METASPLOIT\n\n[0] EXIT" |lolcat -a -d 1 -F 0.5')

	option = int(input(colored("\n|> Select Your Option: ",'yellow',attrs=['bold'])))
	if option == 1:
		os.system('cd pyfiles && python3 ig.py && cd ..')

	elif option == 2:
		os.system('cd pyfiles && python3 open_source.py && cd ..')

	elif option == 3:
		os.system('cd pyfiles && python3 networkscanner.py && cd ..')

	elif option == 4:
		os.system('cd pyfiles && python3 loginwithssh.py && cd ..')

	elif option == 5:
		os.system('cd pyfiles && python3 ftpscript.py && cd ..')

	elif option == 6:
		os.system('cd pyfiles && python3 hashscript.py && cd ..')

	elif option == 7:
		os.system("cd pyfiles && python3 packet_new_terminal.py && cd ..")

	elif option == 8:
		os.system("cd pyfiles && python3 spooferscript.py && cd ..")
		
	elif option == 9:
		os.system("cd pyfiles && python3 bruteforce_script.py && cd ..")		

	elif option == 0:
		os.system('echo "\nGood Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("[-] Error! Select Correct Option","red"))
		input(colored("{#} Press Key To Continue . . .","green"))
		os.system("clear")
		execute()

os.system("clear")
banner()

#coded & created by rajnish

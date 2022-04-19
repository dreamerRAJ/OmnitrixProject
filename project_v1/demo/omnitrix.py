import os
from termcolor import colored


def banner():
	os.system("figlet -f Poison 'OMNITRIX'|lolcat -a -d 2 -F 0.5")
	os.system("figlet -f Digital '						COMBO OF PEN-TESTING TOOLS' | lolcat -a -d 1")
	os.system("figlet -f threepoint ' Created By: Rajnish Kumar' | lolcat -a -d 1 -F 0.3")
	execute()


def execute():
	os.system('echo "       ╔───────────────────────────────────────────────╗" | lolcat -a -d 1 -F 0.2')
	os.system('echo "       |      OMNITRIX - COMBO OF PEN-TESTING TOOLS    |" | lolcat -a -d 1 -F 0.2')
	os.system('echo "       |            Created By: Rajnish Kumar          |" | lolcat -a -d 1 -F 0.2')
	os.system('echo "       ┖───────────────────────────────────────────────┙" | lolcat -a -d 1 -F 0.2')

	os.system('echo "[1] NETWORK SCANNER \n[2] SSH LOGIN \n[3] FTP LOGIN\n[4] HASH CRACKER\n[5] TOOL 5\n\n[0] Exit" |lolcat -a -d 1 -F 0.5')

	option = int(input(colored("\n|> Select Your Option: ",'yellow',attrs=['bold'])))
	if option == 1:
		os.system('cd pyfiles && python3 networkscanner.py && cd ..')

	elif option == 2:
		os.system('cd pyfiles && python3 loginwithssh.py && cd ..')

	elif option == 3:
		os.system('cd pyfiles && python3 ftpscript.py && cd ..')

	elif option == 4:
		os.system('cd pyfiles && python3 hashscript.py && cd ..')

	elif option == 5:
		os.system('echo "[~] Work in Progress . . ."|lolcat -a -d 1 -F 0.7')
		input(colored("Press Any Key To Continue . . .",'red', attrs=['bold']))
		os.system("clear")
		execute()
		
	elif option == 0:
		os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
		exit()
	else:
		print(colored("[-] Error! Select Correct Option","red"))
		input(colored("{#} Press Key To Continue . . .","green"))
		os.system("clear")
		execute()


os.system("clear")
banner()

#coded & created by rajnish

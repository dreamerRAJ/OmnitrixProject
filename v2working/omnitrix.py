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

	os.system('echo "\n[1] INFORMATION GATHERING\n[2] NETWORK SCANNER\n[3] SSH LOGIN\n[4] FTP LOGIN\n[5] HASH CRACKER\n[6] NETWORK ANALYZER\n\n[0] EXIT" |lolcat -a -d 1 -F 0.5')


	option = int(input(colored("\n|> Select Your Option: ",'yellow',attrs=['bold'])))
	if option == 1:
		os.system('cd pyfiles && python3 ig.py && cd ..')
	
	elif option == 2:
		os.system('cd pyfiles && python3 networkscanner.py && cd ..')

	elif option == 3:
		os.system('cd pyfiles && python3 loginwithssh.py && cd ..')

	elif option == 4:
		os.system('cd pyfiles && python3 ftpscript.py && cd ..')

	elif option == 5:
		os.system('cd pyfiles && python3 hashscript.py && cd ..')

	elif option == 6:
		os.system("cd pyfiles && python3 packet_new_terminal.py && cd ..")

		#os.system('echo "[~] Work in Progress . . ."|lolcat -a -d 1 -F 0.7')
		#input(colored("Press Any Key To Continue . . .",'red', attrs=['bold']))
		#os.system("clear")
		#execute()

	#elif option == 99:
	#	os.system('cd pyfiles && python3 safe_mode.py && cd ..')

	elif option == 0:
#		os.system("echo '\n[+] Restoring IP Address'| lolcat -a -i -d 1 -F 0.5")
#		os.system("anonsurf stop")
#		os.system("echo '[+] Restoring MAC Address'| lolcat -a -i -d 1 -F 0.5")
#		os.system("macchanger -p eth0")
		#os.system("macchanger -p eth0 || macchanger -p wlan0")
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

import os
from termcolor import colored

os.system("clear")
os.system("figlet -f Rectangles '=> SAFE MODE'|lolcat -a -d 1 -F 0.5")
os.system('echo "	     ╔──────────────────────────────────────────────────╗" | lolcat -a -d 1 -F 0.2')
os.system('echo "	     | CREATING SAFE HACKING ENVIRONMENT TO USE OMNITRIX|" | lolcat -a -d 1 -F 0.2')
os.system('echo "	     |             Created By: Rajnish Kumar            |" | lolcat -a -d 1 -F 0.2')
os.system('echo "	     ┖──────────────────────────────────────────────────┙" | lolcat -a -d 1 -F 0.2')

def ipchange():
	print(colored("[*] Changing IP Address . . .\n","red", attrs=['bold', 'blink']))
	os.system("anonsurf start")
	print(colored("{#} Your Current IP Address:","cyan", attrs=['bold']))
	os.system("curl ifconfig.me")
	print(colored("\n\n[+] IP Address Changed Successfully\n","green", attrs=['bold', 'underline']))

def macchange():
	os.system("macchanger -r {}".format(mac_device))
	print("\nDETAILS OF DEVICE")
	os.system("ifconfig {}".format(mac_device))
	print(colored("[+] MAC Address Changed Successfully","green", attrs=['bold', 'underline']))


change_ip = str(input(colored("\n>>> Do You Want To Change IP Address?(y/n): ",'yellow', attrs=['bold'])))
if change_ip == 'y' or change_ip == 'Y':
	ipchange()
elif change_ip == 'n'or change_ip == 'N':
	print("\n")
	print(colored("!!!Alert!!!",'white','on_red',attrs=['bold']))
	print(colored("\n[NOT SAFE] No Change In IP Address",'red', attrs=['bold']))

mac_device=str(input(colored("\n>>> Enter The Device Name To Change MAC Address(e.g., eth0, wlan0, etc.){case sensitive}: ","yellow", attrs=['bold'])))
macchange()
input(colored("\n{#} Press Key To Continue . . .","green",attrs=['bold']))
os.system("echo '\n~> Redirecting You To OMNITRIX' | lolcat -a -i -d 50 -F 0.4")
os.system("clear")

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
		os.system("echo '\n[+} Restoring IP Address'| lolcat -a -i -d 1 -F 0.5")
		os.system("anonsurf stop")
		os.system("echo '[+} Restoring MAC Address'| lolcat -a -i -d 1 -F 0.5")
		os.system("macchanger -p {}".format(mac_device))
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

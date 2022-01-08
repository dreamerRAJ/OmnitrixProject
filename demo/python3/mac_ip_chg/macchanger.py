import os
from termcolor import colored


def ipchange():
	print(colored("Changing IP Address . . .","red", attrs=['bold', 'blink']))
	os.system("anonsurf start")
	print(colored("\nIP Address Changed Successfully\n","red", attrs=['bold', 'underline']))

def macchange():
	os.system("macchanger -r {}".format(mac_device))
	print("\n")
	os.system("ifconfig {}".format(mac_device))
	print(colored("IP & MAC Address Changed Successfully","red", attrs=['bold', 'underline']))
	os.system("echo 'Redirecting You To OMNITRIX' | lolcat -a -i -d 30 -F 0.4")
#os.system("macchanger -p eth0")
#print("Original MAC Address Restored Successfully...")

print(colored("⁂CREATING A SAFE ENVIRONMENT⁂" , "cyan", attrs=['bold']))

change_ip = str(input(colored("\n>>> Do You Want To Change IP Address?(y/n): ",'yellow', attrs=['bold'])))
if change_ip == 'y' or change_ip == 'Y':
	ipchange()
elif change_ip == 'n'or change_ip == 'N':
	print("\n")
	print(colored("!!!Alert!!!",'white','on_red',attrs=['bold']))
	print(colored("\n[NOT SAFE] No Change In IP Address",'red', attrs=['bold']))

mac_device=str(input(colored("\n>>> Enter The Device Name To Change MAC Address(e.g., eth0, wlan0, etc.): ","yellow", attrs=['bold'])))
macchange()

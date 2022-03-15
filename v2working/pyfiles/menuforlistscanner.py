import os
from termcolor import colored, cprint

option = int(input(colored("\n\n=> Do you want to:\n[1] Scan Again\n[2] Go Back\n[3] Main Menu\n[4] Exit\n\n>>>Select Your Choice: ",'yellow',attrs=['bold'])))
if option == 1:
	os.system("./list_scanner.sh | lolcat -F 0.3 && cd ..")

elif option == 2:
	os.system('python3 networkscanner.py && cd ..')

elif option == 3:
	os.system('cd .. && python3 omnitrix.py')

elif option == 4:
	os.system('echo "Good Bye! Have A Great Day . . ."|lolcat -a -i -d 50 -F 0.5')
	exit()

else:
	cprint("\n[!] Error! Select Correct Option","red", attrs=['bold','blink'])
	#print(colored("\n[!!!] Error! Select Correct Option","red"))
	input(colored("{#} Press Key To Continue . . .","green"))
	os.system("clear")
	menu()

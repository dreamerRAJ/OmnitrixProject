#!/usr/bin/python

import requests
from termcolor import colored

def request(url):
	try:
		return requests.get("http://"+url)
	except requests.exceptions.ConnectionError:
		pass

target_url = raw_input(colored("=> Enter Target URL: ","blue",attrs=['bold']))

dir_file = raw_input(colored("=> Enter The Path Of File: ",'blue',attrs=['bold']))
file = open(dir_file,"rb")

for line in file:
	word = line.strip()
	full_url = target_url + "/" + word
	response = request(full_url)
	if response:
		print(colored("[+] Discovered Directory At This Link: " + full_url, "green"))

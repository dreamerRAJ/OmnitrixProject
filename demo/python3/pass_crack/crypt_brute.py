
#!/usr/bin/python

import crypt
from termcolor import colored

def crackpass(cryptWord):
	salt = cryptWord[0:2]
	dict = open("dict.txt",'r')
	for word in dict.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word, salt)
		if (cryptWord == cryptPass):
			print(colored("[+] Found Password: "+word,'green'))
			return
#	print("[-] Password Not Found!")
#	return

def main():
	passFile=open('cry_pass.txt','r')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptWord = line.split(":")[1].strip(' ').strip('\n')
			print(colored("[*] Cracking Password For: " + user,'red'))
			crackpass(cryptWord)

main()

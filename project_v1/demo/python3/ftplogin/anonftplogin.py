#!/usr/bin/python

import ftplib
import os


def anonlogin(hostname):
	try:
		os.system("ftp {}".format(hostname))
		ftp=ftplib.FTP(hostname)
		ftp.login('anonymous','anonymous')
		print("[+] {} FTP Anonymous Login Succeeded".format(hostname))
		print(ftp.getwelcome())
		ftp.quit()
		return True
	except(Exception, e):
		print("[-] {} FTP Anonymous Login Failed".format(hostname))


host=input("Enter the IP Address: ")
anonlogin(host)

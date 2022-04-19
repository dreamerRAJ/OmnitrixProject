#!/usr/bin/python

import ftplib

def anonlogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login('anonymous','anonymous')
		print "[*] " + hostname + " FTP Anonymous Login Succeeded."
		ftp.quit()
		return True
	except Exception, e:
		print "[-] " + hostname + "FTP Anonymous Login Failed."

host=raw_input("Enter the IP Address: ")
anonlogin(host)

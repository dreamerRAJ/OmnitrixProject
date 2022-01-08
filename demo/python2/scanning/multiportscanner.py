#!/usr/bin/python

from socket import *
import optparse
from threading import *



def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print "[+] %d/tcp Open" %tgtPort
	except:
		print "[-] %d/tcp Closed" %tgtPort
	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "Can't Resolve the hostname %s" %tgtHost
	try:
		tgtName = gethostbyaddr(tgtIP)
		print "[+] Scan Results For: " + tgtName[0]
	except:
		print "[+] Scan Results For: " + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	tgtHost = raw_input("Enter Ip: ")
	tgtPorts = raw_input("Ports: ").split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost,tgtPorts)


if __name__ == '__main__':
	main()

#USAGE:
#python portscanneradv.py -h <ip address> -p <port number>

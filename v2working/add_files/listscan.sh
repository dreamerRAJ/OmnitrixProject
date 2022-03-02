#!/usr/bin/bash

bold=$(tput bold)
normal=$(tput sgr0)


figlet -f amc3line 'LIST SCAN WITH NMAP' | lolcat -a -d 2 -F 0.5
sleep 1
read -p "${bold}|> Enter Your IP's List Path : ${normal}" ip_addr 
sleep 1
while read ip; do
echo -e "\e[101m [+] Testing IP : $ip\e[0m" && nmap -v -sV -d -A -p1-65535 --script vuln,default -T4 -Pn $ip
done < $ip_addr

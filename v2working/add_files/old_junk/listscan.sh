#!/bin/bash

bold=$(tput bold)
normal=$(tput sgr0)

figlet -f amc3line 'LIST SCAN WITH NMAP' | lolcat -a -d 2 -F 0.5
sleep 1
echo -e "${bold}\e[93m{*} FOLLOWING TASKS WILL BE PERFORMED: \e[0m${normal}"
echo -e "${bold}\e[93m      1. VERBOSE SCAN \e[0m${normal}"
echo -e "${bold}\e[93m      2. SERVICE SCAN \e[0m${normal}"
echo -e "${bold}\e[93m      3. AGRESSIVE SCAN \e[0m${normal}"
echo -e "${bold}\e[93m      4. NMAP SCRIPT ENGINER SCANNING \e[0m${normal}"
echo -e "${bold}\e[93m      5. OUTPUT FILE GENERATION \e[0m${normal}"
echo -e "${bold}\e[91m{!!!} THIS MAY TAKE A WHILE TO SCAN THE LIST, IF YOU WANT TO CANCEL USE 'Ctrl+Z' IT WILL TERMINATE THE WHOLE TOOL\e[91m${normal}"
sleep 1
read -p "${bold}|> Enter IP's List Path : ${normal}" ip_addr
echo
sleep 1
echo -e "\e[5m\e[1m\e[91mSCANNING STARTED... \e[92mKEEP PATIENCE..!!!\e[0m"
sleep 1
echo
while read ip; do
echo -e "\e[101m [+] Testing IP : $ip \e[0m" && nmap -v -sV -d -A -p1-65535 --script vuln,default -T4 -Pn $ip
done < $ip_addr
sleep 1
echo -e "\e[5m\e[1m\e[91mSCANNING COMPLETED...\e[92m\e[0m"


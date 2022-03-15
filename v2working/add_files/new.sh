bold=$(tput bold)
normal=$(tput sgr0)

figlet -f amc3line 'LIST SCAN WITH NMAP' | lolcat -a -d 2 -F 0.5
echo "	    ╔───────────────────────────────────────────────╗"
echo "            |           Created By: Rajnish Kumar           |"
echo "	    ┖───────────────────────────────────────────────┙"
sleep 1
echo "${bold}\e[93m{*} FOLLOWING TASKS WILL BE PERFORMED: \e[0m${normal}"
echo "${bold}\e[93m      1. VERBOSE SCAN \e[0m${normal}"
echo "${bold}\e[93m      2. SERVICE SCAN \e[0m${normal}"
echo "${bold}\e[93m      3. AGRESSIVE SCAN \e[0m${normal}"
echo "${bold}\e[93m      4. NMAP SCRIPT ENGINER SCANNING \e[0m${normal}"
echo "${bold}\e[93m      5. OUTPUT FILE GENERATION \e[0m${normal}"
echo "${bold}\e[91m{!!!} THIS MAY TAKE A WHILE TO SCAN THE LIST, IF YOU WANT TO CANCEL USE 'Ctrl+Z' IT WILL TERMINATE THE WHOLE TOOL\e[91m${normal}"
sleep 1
read -p "${bold}|> Enter IP's List Path : ${normal}" ip_addr
sleep 1
read -p "${bold}|> Enter Your Output Folder Name : ${normal}" output
mkdir $output
echo
sleep 1
echo "\e[5m\e[1m\e[91mSCANNING STARTED... \e[92mKEEP PATIENCE.. IT WILL TAKE A WHILE!!!\e[0m"
sleep 1
while read ip; do
echo "\e[101m \n[+] Testing IP : $ip \e[0m" && nmap -v -sV -d -A -p1-65535 --script all,auth,discovery,vuln,malware,default,safe -T4 -Pn $ip -oA $ip
#echo "\e[101m \n[+] Testing IP : $ip \e[0m" && nmap -sV $ip -oA $ip
mkdir "$ip scan"
mv $ip.* "$ip scan"
mv "$ip scan" $output
done < $ip_addr
sleep 1
mv $output ~/Desktop/
echo
echo "\e[1m[#] \e[4mYour Output Is Stored In The Folder Name $output at Your Desktop\e[0m"
sleep 1
echo "SCANNING COMPLETED. . ."

#Requirements Installations

bold=$(tput bold)
normal=$(tput sgr0)


#apt-get update && apt upgrade
apt-get install lolcat

echo "${bold}[+] Installing Python3 . . .${normal}" | lolcat -i -F 0.5
apt-get install python3

echo "${bold}[+] Installing Figlet . . .${normal}" | lolcat -i -F 0.5
apt-get install figlet
cd /usr/share/figlet

echo "${bold}[+] Installing Figlet-Fonts . . .${normal}" | lolcat -i -F 0.5
git clone https://github.com/dreamer1eh/figlet-fonts
cd figlet-fonts
mv * /usr/share/figlet
cd ..
rm -r figlet-fonts
cd ~

echo "${bold}[+] Installing Python-pip Module. . .${normal}" | lolcat -i -F 0.5
apt-get install python3-pip

echo "${bold}[+] Installing Python-nmap Module. . .${normal}" | lolcat -i -F 0.5
pip3 install python-nmap

echo "${bold}[+] Installing Pynput Module. . .${normal}" | lolcat -i -F 0.5
pip3 install pynput

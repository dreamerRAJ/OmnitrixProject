import subprocess

print("I AM SPOOFER... UNDER PROGRESS !!!")
interface = "wlan0"
before_change = subprocess.check_output(["ifconfig ether",interface])
print(before_change)

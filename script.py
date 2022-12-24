import subprocess

# Variables
interface = "wlan0"
new_mac = "00:11:22:33:44:55"

# Output Text
print("[+] Changing MAC Address for " + interface + " to " + new_mac)

# Mac Changer Script
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
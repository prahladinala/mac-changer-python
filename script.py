import subprocess

# Variables
interface = input("Enter Interface > ")
new_mac = input("Enter New MAC Address > ")
## NOTE: input() or raw_input() is used to get user input

# Output Text
print("[+] Changing MAC Address for " + interface + " to " + new_mac)

# Mac Changer Script
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

# Mac Changer Script (Additional Security)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
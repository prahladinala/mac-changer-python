import subprocess
import optparse

# Options - Optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

# Variables
interface = options.interface
new_mac = options.new_mac
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
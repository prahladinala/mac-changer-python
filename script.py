import subprocess
import optparse

# Function for MAC Changer
def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    # Mac Changer Script (Additional Security)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Options - Optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

# Variables
# interface = options.interface
# new_mac = options.new_mac
## NOTE: input() or raw_input() is used to get user input

# Calling Mac Changer Function
change_mac(options.interface, options.new_mac)
import subprocess
import optparse

# Function for Getting Arguments
def get_arguments():
    # Options - Optparse
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

# Function for MAC Changer
def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    # Mac Changer Script (Additional Security)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Calling Get Arguments Function
(options, arguments) = get_arguments()
# Calling Mac Changer Function
change_mac(options.interface, options.new_mac)
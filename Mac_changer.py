import subprocess
import optparse
import re
import pyfiglet

ascii_banner = pyfiglet.figlet_format("ProGod04")
print(ascii_banner)

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="MAC Address you want to change to")
    (options, arguments)=parser.parse_args()
    if not options.interface:
        parser.error("ENTER THE INTERFACE, use --help for more information")
    elif not options.new_mac:
        parser.error("ENTER THE MAC Address, use --help for more information")
    else:
        return options

def change_mac(interface,new_mac):
    print("[+]Changing the MAC of "+ interface + " to "+ new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str (ifconfig_result))
    if mac_output:
        return mac_output.group(0)
    else:
        print("[-]COULD NOT READ MAC ADDRESS")
        
#arguments variable is not really used but we need it to store the value
options=get_args()
cur_mac = get_current_mac(options.interface)

print("Current mac is " + str (cur_mac))
change_mac(options.interface,options.new_mac)

cur_mac=get_current_mac(options.interface)
if cur_mac == options.new_mac:
    print("[+] MAC Address was changed to " + cur_mac)
else:
    print("[+]MAC NOT CHANGED")

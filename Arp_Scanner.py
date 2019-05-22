

# arp scanner written with scapy ..

import sys , os 
from scapy.all import *

interface = raw_input("Network interface here ...")
ip_range = raw_input("Enter ip range in exact CIDR format...")
broadcastMac = "ff:ff:ff:ff:ff:ff"

# verbosity equals to 0 here... 
conf.verb = 0
ans, unans = srp(Ether(dst=broadcastMac)/ARP(pdst = ip_rage), timeout =2, iface=interface, inter=0.1)

for send,recive in ans:
	print (recive.sprintf(r"%Ether.src% - %ARP.psrc%"))

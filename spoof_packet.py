
# python code for spoofing the ip packet 
# this is a prerequiste teqnique or initial step used by the attackers before performing the cyber attacks mainly to hide their identity 

import sys
from scapy.all import send, IP, ICMP

if len(sys.argv) < 3:
    print sys.argv[0] + " <src_ip> <dst_ip>"
    sys.exit(1)

packet = IP(src=sys.argv[1], dst=sys.argv[2]) / ICMP()

if not packet:
    print("error crafting ip packet")
    sys.exit(1)
    
else:
    result = send(packet)

if result:
    result.show()
    
   # you can use any network packet analyser to verify the injection of the spoofed ip packet to the network 
   # ends 

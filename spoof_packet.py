
# python code for spoofing the ip packet 

import sys
from scapy.all import send, IP, ICMP

if len(sys.argv) < 3:
    print sys.argv[0] + " <src_ip> <dst_ip>"
    sys.exit(1)

packet = IP(src=sys.argv[1], dst=sys.argv[2]) / ICMP()
result = send(packet)

if result:
    result.show()
    
    # ends 

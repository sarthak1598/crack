
# program for reading and processing the packet capture or pcap file for analysis purpose 

import time 
import sys 
import os 

from scapy.all import *
a = " " # empty string variable declaration for storing the pcap file data

data = raw_input("enter the pcap file name")

curtime = datetime.datetime.now()
os.system("tshark  -T fields  -e frame.time -e  data.data -w Eavesdrop_Data.pcap > Eavesdrop_Data.txt -F pcap -c 1000")

a = rdpcap(data) # reading the pcap data 
sessions = a.sessions()

for session in sessions:
    print("Showing the sessions in the file......")
    print sessions

# end 

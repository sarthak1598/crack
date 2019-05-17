
import os 
import time 

from sys import argv
from scapy.all import rdpcap, IP

def help_method():
    print("Usage: python get_devices.py path_to_pcap")
    sys.exit(1)


def extract_machines(pcap):
    machines = []
    packets = rdpcap(pcap)
    for i in range(len(packets)):
    
             if packets[i][IP].src not in machines:
             
                 machines.append(packets[i][IP].src)
                 print(len(machines), packets[i][IP].src)
             elif packets[i][IP].dst not in machines:
             
                 machines.append(packets[i][IP].dst)
                 print(len(machines), packets[i][IP].dst)
    return machines

if __name__ == '__main__':

    pcap = argv[1]
    if len(argv) < 2:
        help_method()
        # prited the all of machie ames preset i the pcap file 
        
    print("\n All the machines in pcap are =>", extract_machines(pcap),end="\n\n")
    # termiated ../

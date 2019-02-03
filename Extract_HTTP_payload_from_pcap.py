

#  This is python code to read a packet captire file and extract the http payload information 
#  Using tshark as a packet anyliser tool for capturing and traffic analysis 


from scapy.all import *
import time
import sys 
import os 

data = "raw_input("pcap file ")

pcap_data = rdpcap(data)

os.system("tshark -r Eavesdrop_Data.pcap -Y http -w Eavesdrop_Data_http.pcap")

sessions = pcap_data.sessions()
i = 1
for session in sessions:
    http_payload = ""
    
    for packet in sessions[session]:
        
            if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                print packet[TCP].payload
    
# progrsm ends 

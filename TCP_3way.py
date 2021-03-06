

# this code performs the initial 3 way TCP handshake to initiate a further http connection 

# scapy module for self crafting the tcp/ip packet

#!/usr/bin/env python


import scapy
import sys

get='GET / HTTP/1.0\n\n'  # get request 

dst = raw_input("enter the destination ip")

ip=IP(dst) # destination server ip address

port=RandNum(1024,65535)  # randomising the source port nunber 


SYN=ip/TCP(sport=port, dport=80, flags="S", seq=33)

                   # Send SYN and receive SYN,ACK
SYNACK=sr1(SYN)

# Creating ACK with GET request

ACK=ip/TCP(sport=SYNACK.dport, dport=80, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1) / get

reply,error=sr(ACK)  # sending the ack-get request
print reply.show()

# tcp handshake completed done !!
# ends

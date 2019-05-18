
# Python hotspotconverter for Unix based systems 
# this script makes the linux machine into the packet forwarding machine to act as a access point for other device to connect to the networ\
# using ssid/password provided by the user 


import os
import sys
import datetime 

#def pyhotspot(hotspotname,ssid,password):

def info():
	
	os.system("clear")
	print "#############################"
	print "#        Python$tuff   #"
	print "#############################"
	print "# Welcome To PyHotspot #"
	print "#############################"

	hotspotname = raw_input ("\nHotspot connection-name : ")
	ssid = raw_input ("Type ssid : ")
	
	passw = raw_input ("type wiffi password : ")
	
	current_time = datetime.now()
	os.system("sudo iptables -F INPUT") # flushed iptable rules 
	
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward") # os system commad to enbale the kernal ip forwarding temporarily.
	# data type conversion as string 
	
        os.system("nmcli device wifi hotspot con-name linuxhotspot ssid "  +  str(ssid) + " str(password) " + str(passw))
	
	final_time = datetime.now()
	exec_time = final_time - current_time 
	print(exec_time)
# function ends 

def main():
# counter = input ("How many packets do you want to send : ")
	info()	
main()

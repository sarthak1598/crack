
# The purpose for which i made this script was to gather the basic information of operating system 
# basic information about the target system after the remote exploitation of machine by running this small piece of code 
# This is very simple code but can be prooved as a time saver 


#!/usr/bin/env python   

import sys
import os

import time

usernumber = os.getuid()

processnumber = os.getpid()
presentdir = os.getcwd()
sysinfo = os.uname()
usedinfo = os.times()
now = time.time()

means = time.ctime(now)

print "User Number :",usernumber
print "Process ID :",processnumber
print "Current Directory :",presentdir
print "System Information :",sysinfo
print "System Information :",usedinfo

print "\nTime is now",now
print "Which interprets as",means

# program ends 
# But this script is i think mainly useful after the system compromise 
# As it can give instantly the nessecory information of the os and processor to the attacker
# happy hacking 

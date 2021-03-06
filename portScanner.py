

# improved port scanner written in python 

import socket
import subprocess
import datetime

import os
import sys

os.system("clear")  # returns the clear terminal screen on every execution of the script 


destname = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remotename) #getting server IP

print "Please wait, scanning remote host", remoteServerIP

t1 = datetime.now()  # current time 

try:
    for port in range(1,80):  # cheking ports of the well known services at transport layer 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()
        

except KeyboardInterrupt:
    print "Process terminated by the user"
    sys.exit(0)
    

except socket.gaierror:
    print 'Hostname cannot be resolved'
    sys.exit(0)
    

except socket.error:
    print "Server is probably down , cannot connect .....Exiting"
    sys.exit(0)
    
t2 = datetime.now() # final time value after total execution 

total = t2 - t1 # total time taken by the script 

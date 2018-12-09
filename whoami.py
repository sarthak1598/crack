
#Python socket script for instant basic enumeration of local machine 
import socket 
import uuid  #module for extracting machine's MAC information 

# Function to display system basic information 
# IP address 
# Hostname 
# Mac Address

def my_sysIPinfo(): 

    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP is : ",host_ip) 
        print (hex(uuid.getnode())) # extracting the mac address of the machine 

my_sysIPinfo() # calling the above defined function 
    except: 
        print("Unable to get Hostname and IP") 
  

my_sysIPinfo() # calling the above defined function 

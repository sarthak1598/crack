
# This is another handy script i used to make while learning the pentesting with python for unix/linux.
# This code actually ping the whole network or subnet defined by the user.

# Works as directed by the network id entered by the user 

# 789sk.gupta@gmail.com 
# New modules used 
#ipaddress 

import subprocess # to handle the unix system commands
import ipaddress  # for digging into the network 

network_address = input("Enter the network address in CIDR FORMAT")
format(EX.192.168.1.0/24): ")

# getting into the network 
ipnetwork = ipaddress.ip_networ(network_address)

hostlists = list(ipnetwork.hosts()) # all the host are stored or binded in a list dats structure



# pinging the complete subnet with all of his hosts 

for i in range(len(hostslist)):
    # subprocess module system command to execute the os shell command and piping purpose
    output = subprocess.Popen(['ping','-n','1','-w', '500', str(hostslist[i])] , stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    if "Destination host unreachable" in output.decode('utf-8'):  # string pattern matching by decoding the command output stored in output variable
        
        print(str(hostslist[i])) , "is Offline") 
    elif "Request timed out" in output.decode(utf-8)
        print(str(hostslist[i])) , "is Online")
        
    else:
        print(str(hostslist[i]) , "is Online")

# program ends
# happy hacking 

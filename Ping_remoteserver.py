#importing the python socket module 

import socket
import sys  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creating  a TCP/IP socket
server_ip = raw_input(‘Enter IP of the server : ‘)
rep = os.system(‘ping ‘ + server_ip)   #os shell command to ping.
if rep == 0: 
print ‘n n server is alive n n’
else:
print ‘server is seems to be down’



# code to extract possible server banner of the website/server to extract the information ...
import os
import socket

# as the http server is hosted on port 80 
http_sock = socket.socket(socket.AF_INET ,socke.SOCK_STREAM) # TCP SOCKET
host = str(raw_input("Please enter the host name: "))
port=80

http_Sock.connect(host,port)
http_sock.send('GET HTTP/1.1 \r\n')

# returned the banner info in retuen variable 
return = http_sock.recv(1024)

print '[+]' + str(return)
# ends ../.../

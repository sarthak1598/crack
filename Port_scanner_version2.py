# another port scanner based on pre -coded list of some common services running in most of the application over the internet 

import os
import sys 

import socket 
os.system('clear')

host = raw_input("Domain of the host")
ip = socket.gethostbyname(host)

open_ports = [] # taking the ports list 
# set  to be checket for.....open /closed ports 

common_ports = { 21, 22, 23, 25, 53, 69, 80, 88, 109, 110, 
                 123, 137, 138, 139, 143, 156, 161, 389, 443, 
                 445, 500, 546, 547, 587, 660, 995, 993, 2086, 
                 2087, 2082, 2083, 3306, 8443, 10000 
                }

def probe_port(host, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((host, port))	
		if r == 0:
			result = r
		sock.close()
	except Exception, e:
		print e;
		pass

	return result

for p in sorted(common_ports):
	sys.stdout.flush()
	print p
	response = probe_port(host, p)
	if response == 0:
     # append in the open_port list if function returns 0 ./
		open_ports.append(p)
#  printing open_ports list if it contains some values .... 	
if open_ports:
	print "Open Ports are..."
	print sorted(open_ports)
  
else:
	print "No..., ports found open, or they may be filtered by the firewall"

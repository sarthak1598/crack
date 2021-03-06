
# python oop based sniffer thread based 

from scapy.all import*
from threading import Thread
from time import sleep

class Sniffer(Thread):
    interface=raw_input("put your active netwrok interface")
    
    def  __init__(self, interface):
        super().__init__()

        self.interface = interface

    def run(self):
        sniff(iface=self.interface, filter="ip", prn=self.print_packet)

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

sniffer = Sniffer()

print(" Start sniffing..")
sniffer.start()

try:
    while True:
        sleep(50)
    # user intrrupt --->>>> on pressing ctrl+c key combination 
    
except KeyboardInterrupt:
    print("[*] Stop sniffing")
    sniffer.join()

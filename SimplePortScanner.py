

# this code is written to perform a basic port scannig by manually entering the port number to verify the state of port

# 789sk.gupta@gmail.com 

import socket 
import os

import sys
ip = raw_input("Enter the ip address : ")

port= input("enter the port number: ")

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
        print "Port" , port , "is closed"
else:
        print "Port" , port , "is open"

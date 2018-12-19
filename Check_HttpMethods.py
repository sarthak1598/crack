
# Python script to enumerate the opened http-methods of web server/domain
# The initial step of the web server enumeration 
# I wrote this script for testing 4 main http methods 
# which can be useful in reconnaissance process

import sys
import os
import requests

host = input("Please enter the full domain you want to enumerate")

# host = 'http://www.udemy.com' 
reqget = requests.get(host)


reqpost = requests.post(host)
reqput = requests.put(host)
reqdelete = requests.delete(host)
#reqtrace = requests.trace(host)

print("The available Http methods and their status_codes are : ")
print "GET METHOD"
print reqget.status_code 
print "POST METHOD"
print reqpost.status_code
print "PUT METHOD"
print reqput.status_code 
print "DELETE METHOD"
print reqdelete.status_code 
#print("TRACE METHOD"+  reqtrace.status_code )

# happy hacking

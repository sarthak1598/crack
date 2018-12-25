

# python script for mapping and extracting the geoloactin data :)) can be very much useful 
# This program extract the data of ip addresses mapped with the physical location

# importing the pygeoip module for mapping 

# FOR CORRELATING THE IP TO LOCATION DATA USING THE WORLD WIDE DATABASE AVAILABLE  NAMED:
# GeoLiteCity.dat

# pip install pygeoip for installation of the module 

import pygeoip

gip = pygeoip.GeoIP('GeoLiteCity.dat') # gip variable loading data from the GeoLiteCity database 


def printRecord(ip):  # driver function 
   
  ip = raw_input("Please enter the ip address to geolocate")
	rec = gip.record_by_name(ip) 
	city = rec['city']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
  
  # printing the geolocaion info of ip address 
  
	print '[+] Address: '  + ip + ' Geo-located ' 
	print '[+] ' +str(city)+ ', '+str(country)
	print '[+] Latitude: ' +str(lat)+ ', Longitude: '+ str(long)


printRecord(ip)  # calling driver function 

# program ends

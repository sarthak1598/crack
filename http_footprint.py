
# another approach to footprint application layer with python 


import time 
import requests 

method_list = ['GET' , 'POST' , 'PUT' ,'DELETE' ,'OPTIONS','TRACE','TEST' ]


time = datetime.datetime.nowI()

for method in method_list:
	
	req = requests.request(method , 'Enter the URL')
	print (method, req.status_code, req.reason)
	
	
	if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
			print ('Cross Site Tracing(XST) is possible')
      
     # ends 

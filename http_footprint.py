
# another approach to footprint application layer with python 

import sys 
import time 
import requests 

method_list = ['GET' , 'POST' , 'PUT' ,'DELETE' ,'OPTIONS','TRACE','TEST' ]


time1 = time.time()

for method in method_list:
	
	req = requests.request(method , 'Enter the URL')
	print (method, req.status_code, req.reason)
	
	
	if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
			print ('Cross Site Tracing(XST) is possible')
			
			
	elif method == 'PUT' or 'DELETE' and req.status_code == '200':
			print('May be vulnerable to shell upload and resource temperment vulnerbility .')
       
time2 = time.time()
final_time = time2 - time1   
# ends 


# This is other simple python code which ca help scanning some hacks with google in faster and time saving manner 

# the script recieves an input argument from the user and displays the important information regarding the hacks to the user 
# can be found usefull in some cases

import re  # regex --regular expression operation handling library in python....USED HERE FOR THE PATTERN MATCHING HIGHLY NEEDED HERE!!!

import sys
import google
import urllib2

if len(sys.argv) < 2:  # argument count validation supplied by the user 

    print sys.argv[0] + ": <dict>"
    sys.exit(2)

fo = open(sys.argv[1])

for word in fo.readlines():
    print "\n searching the " + word.strip()
    result = google.search(word.strip())

    try:
        for implink in results:
            if re.search("youtube", implink) == None: print  implink
    
    
    except urllib2.HTTPError, e:
    
    
        print "Search not found : " + str(e)
        
   # program ends
   # happy hacking :)

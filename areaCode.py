#!/usr/bin/python
import re
phone = "602-343-8747"
match = re.search(r'^\d{3}', phone)
print "The area code is: " + match.group() 

# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1969901.xml (Sum ends with 38)

#You are to look through all the <comment> tags and find the <count> values sum the numbers. 
#The closest sample code that shows how to parse XML is geoxml.py. 
#But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

adress = input('Enter location: ')
if len(adress)< 1:
    adress = 'http://py4e-data.dr-chuck.net/comments_42.xml' 

count= 0

#Read de XML file as a string for Python
print('Retrieving ',adress)
xml_file = urllib.request.urlopen(adress, context = ctx).read()
print('Retrieved ',len(xml_file),'characters')

#Transform into an element tree the file
comments = ET.fromstring(xml_file)
#List of the comments
lst = comments.findall('.//count')
print ('Count: ', len(lst))
for tag in lst:
    
    count = count + int(tag.text)

print('Sum: ',count)


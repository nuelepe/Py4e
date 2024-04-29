#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
#compute the sum of the numbers in the file and enter the sum below:

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1969902.json (Sum ends with 18)

import urllib.request, urllib.parse
import ssl, json

url = input('Enter location: ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving ',url)
#Open the irl and get the urlhandler
handler = urllib.request.urlopen(url, context=ctx)
#Read the file inside the url and decode it from UTF-8
data = handler.read().decode()
#Transfer the information into a json dictionary
json_data = json.loads(data)


print('Retrieved ', len(json_data), ' characters')

count = 0
total = 0

#Scan the dictionary for each user inside comments, and extract the count parameter
for usr in json_data['comments']:
    count = count + 1
    total = total + int(usr['count'])

print('Count: ',count)
print('Sum: ',total)

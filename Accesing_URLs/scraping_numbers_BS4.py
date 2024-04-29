#Scraping Numbers from HTML using BeautifulSoup

#Python programm that uses urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the  sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1969899.html (Sum ends with 24)

#Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.
#https://www.py4e.com/code3/urllink2.py?PHPSESSID=9ee84069a65f5b2e13978bd60c4e916a

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Ask for the url, read it and parse it from html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#initialize a counter
count=0
acc = 0

#Retrieve a list of the span tags
tags = soup('span')
for tag in tags:
    acc = acc + (int(tag.contents[0]))
    count = count+1

print('Count ',count)
print('Sum ',acc)
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah

#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Divya.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: H

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Ask for the url, read it and parse it from html
url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for i in range(count+1):
    print('Retrieving: ',url)
    url = tags[position-1].get('href',None)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    

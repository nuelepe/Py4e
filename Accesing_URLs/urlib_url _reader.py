import urllib.request, urllib.parse, urllib.error

#open the url
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

#Create a dictionary to count the words
counts = dict()


for line in fhand:
    words =line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1


    print(line.decode().strip())
print (counts)
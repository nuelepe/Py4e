#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours_dic=dict()

#Read the text file lines and separate first into words then the time into digits and store the hours counts in the hours_dic
for line in handle:
    if line.startswith("From "):
        line.rstrip()
        words = line.split()
        time = words[5]
        time = time.split(":")
        hour = time[0]
        
        hours_dic[hour]=hours_dic.get(hour,0)+1
        
hours_dic=sorted(hours_dic.items())

for hours,count in hours_dic:
    print (hours,count)
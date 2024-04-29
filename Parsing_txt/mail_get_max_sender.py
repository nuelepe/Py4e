#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those 
#lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dic = dict()

for line in handle:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        address = words[1]
        dic[address] = dic.get(address,0)+1

max_sender = 0
max_times = 0

for sender,times in dic.items():
    if max_sender is None or times > max_times:
        max_sender = sender
        max_times = times

print(max_sender ,max_times)
    
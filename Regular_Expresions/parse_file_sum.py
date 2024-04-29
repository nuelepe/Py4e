#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re

fname=input("File name: ")
if len(fname)<1:
    fname="regex_sum_42.txt"

#I researched and the eval() function allows to change the strings to integers.
#list_numbers = sum([eval(number) for number in re.findall("[0-9]+",open(fname).read())])

list_numbers = re.findall("[0-9]+",open(fname).read())

acc = 0
for number in list_numbers:
    acc = acc + int(number)

print(len(list_numbers))
print(acc)
import re

#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

print(sum([(num) for num in re.findall("[0-9]+",open("regex_sum_42.txt").read())]))
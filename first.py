#brings in regular expression library
import re

#user types in file name they would like to parse through
fname = input('Enter file name: ')
#opens file name, and applies "hand" variable to handle
hand = open(fname)
#creating list to store parsed data
numlist = list()
#for every line in the file
for line in hand:
    #x is going to give you a list per line. If a line has 0 numbers it will create an empty list.  If I line has 10 different numbers, there will be 10 numbers in the list.
    x = re.findall('\d+', line)
    #we want to skip any empty lists
    if len(x) == 0:
        continue
    #i iterates through the items in each x list
    for i in x:
        #turns the individual i strings into num integers
        num = int(i)
        #adds num to the current list of data, back to top
        numlist.append(num)

#prints the sum of all the list items
print(sum(numlist))

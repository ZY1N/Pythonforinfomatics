#Exercise 11.2 Write a program to look for lines of the form
#New Revision: 39772
#And extract the number from each of the lines using a regular expression and
#the findall() method. Compute the average of the numbers and print out the
#average.
#Enter file:mbox.txt
#38549.7949721
#Enter file:mbox-short.txt
#39756.9259259

import re

fname = raw_input("Enter file: ")
handle = open(fname)
total = 0
count = 0

for line in handle:
    line = line.rstrip()
    x = re.findall('New Revision:\s([0-9]+)', line)
    if len(x) > 0:
         number = x[0]
         number = float(number)
         total = total + number
         count = count + 1

print total/count



string = str()

for line2 in handle:
    string = string + line2

print string
y = re.findall('New Revision:\s([0-9]+)', string)

print y


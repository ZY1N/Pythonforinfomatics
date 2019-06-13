#Exercise 11.1 Write a simple program to simulate the operation of the the grep
#command on UNIX. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re

fname = open('mbox.txt')

rexp = raw_input("Enter a regular expression : ")

count = 0

for line in fname:
    line = line.rstrip()
    x = re.findall(rexp, line)
    if len(x) > 0:
        count = count + 1

print "mbox.txt had %d lines that matched %s" % (count, rexp)

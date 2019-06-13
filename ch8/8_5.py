#Exercise 8.5 Write a program to read through the mail box data and when you
#find line that starts with From, you will split the line into words using the split
#function. We are interested in who sent the message which is the second word on
#the From line.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

fname = open("blank.txt")
count = 0

for line in fname:
    try:
        lcopy = line.split()
    except:
        continue
    if len(lcopy) == 0 :
        continue
    if lcopy[0] == 'From':
       print lcopy[1]
       count = count + 1

print "There were %d lines in the file with From as the first word" % count

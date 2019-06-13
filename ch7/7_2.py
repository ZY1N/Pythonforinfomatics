#Exercise 7.2 Write a program to prompt for a file name, and then read through
#the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with X-DSPAM-Confidence: pull apart
#the line to extract the floating point number on the line. Count these lines and the
#compute the total of the spam confidence values from these lines. When you reach
#the end of the file, print out the average spam confidence.

fname = raw_input("Enter the file name: ")
handle = open(fname)

count = None
total = 0

for line in handle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        if count == None:
            count = 0
        strnumber = line.find(':') + 1
        number = float(line[strnumber:])
        total = total + number
        count = count + 1
print 'Average spam confidence :', total/count

#Exercise 7.1 Write a program to read through a file and print the contents of the
#file (line by line) all in upper case. Executing the program will look as follows:


fname = raw_input("Enter a file name:")
try:
    handle = open(fname)
except:
    print 'File cannot be opened: ', fname
    exit()

for line in handle:
    line = line.rstrip()
    print line

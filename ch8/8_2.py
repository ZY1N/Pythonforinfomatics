#Exercise 8.2 Figure out which line of the above program is still not properly
#guarded. See if you can construct a text file which causes the program to
#fail and then modify the program so that the line is properly guarded and
#test it to make sure it handles your new text file.

try:
    fhand = open('blank.txt', 'r')
except:
    print "Doesn't exist, try again"
    exit()
    
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) > 2:
        print words[2]

#2 mistakes, one if the text opened doesnt exits
# two, if the number of words after From is less than 3

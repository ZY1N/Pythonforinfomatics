#Exercise 8.3 Rewrite the guardian code in the above example without two
#if statements. Instead use a compound logical expression using the and
#logical operator with a single if statement.

try:
    fhand = open('blank.txt', 'r')
except:
    print "Doesn't exist, try again"
    exit()

count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words

    if len(words) != 0 and words[0] == 'From' and len(words) > 2 :
        print words[2]
    continue

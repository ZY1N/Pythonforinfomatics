#Exercise 7.3 Sometimes when programmers get bored or want to have a bit of fun,
#they add a harmless Easter Egg to their program (en.wikipedia.org/wiki/
#Easter_egg_(media)). Modify the program that prompts the user for the file
#name so that it prints a funny message when the user types in the exact file name
#na na boo boo. The program should behave normally for all other files which
#exist and dont exist. Here is a sample execution of the program:

fname = raw_input('Enter the file name: ')

if fname == 'na na boo boo':
    print 'NA NA BOO BOO TO YOU - You have been punk\'d'
    exit()

try:
    handle = open(fname)
except:
    print "file cannot be opened: ", fname
    exit()

count = 0
for line in handle:
    count = count + 1
print 'There were %d, subject lines in %s' % (count, fname)

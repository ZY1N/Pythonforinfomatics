#Exercise 9.5 This program records the domain name (instead of the address)
#where the message was sent from instead of who the mail came from (i.e. the
#whole e-mail address). At the end of the program print out the contents of your
#dictionary.

fname = raw_input("Enter a file name: ")
try:
    name = open(fname)
except:
    print "invalid file name"
    exit()

dictionary = dict()

for line in name:
    if line.startswith('From '): 
        line = line.split()
        email = line[1] 
        addressnum = email.find('@')
        addressnum = email.find('@') + 1
        dictionary[email[addressnum :]] = dictionary.get(email[addressnum :], 0) + 1

print dictionary

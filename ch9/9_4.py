#Exercise 9.4 Write a program to read through a mail log, and figure out who had
#the most messages in the file. The program looks for From lines and takes the
#second parameter on those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the senders address to the total
#number of messages for that person.
#After all the data has been read the program looks through the dictionary using
#a maximum loop (see Section 5.7.2) to find who has the most messages and how
#many messages the person has.

fname = raw_input("Enter a file name : ")
handle = open(fname)
dictionary = dict()

for line in handle:
    words = line.split()
    if "From" in words:
        dictionary[words[1]] = dictionary.get(words[1], 0) + 1

largest = None
for element in dictionary:
    if largest == None or element > largest:
        largest = element
        print largest

print 'Largest :', largest, dictionary [largest]

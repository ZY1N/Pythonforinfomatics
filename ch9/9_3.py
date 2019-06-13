#Exercise 9.3 Write a program that categorizes each mail message by which day of
#the week the commit was done. To do this look for lines which start with From,
#then look for the third word and then keep a running count of each of the days
#of the week. At the end of the program print out the contents of your dictionary
#(order does not matter).

fname = raw_input("Enter a file name : ")
handle = open(fname)
dictionary = dict()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        word = line[2]
        dictionary[word] = dictionary.get(word, 0) + 1
print dictionary

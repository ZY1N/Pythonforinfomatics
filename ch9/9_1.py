#Exercise 9.1 Write a function that reads the words in words.txt and stores them
#as keys in a dictionary. It doesnt matter what the values are. Then you can use
#the in operator as a fast way to check whether a string is in the dictionary.

fname = open("words.txt")

dictionary = dict()
count = 0

for line in fname:
    nline = line.split()
    for word in nline:
        if word in dictionary:
            continue
        else:
            dictionary[word] = count
            count = count + 1

print dictionary

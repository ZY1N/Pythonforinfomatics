#Exercise 8.4 Download a copy of the file from www.py4inf.com/code/romeo.txt
#Write a program to open the file romeo.txt and read it line by line. For each line,
#split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the word is not in the
#list, add it to the list.
#When the program completes, sort and print the resulting words in alphabetical
#order.


fname = raw_input("Enter file name : ")
handle = open(fname)
wordlist = []

for line in handle:
    splited = line.split() 
    for word in splited:
        if word is wordlist:
            continue
        wordlist.append(word)
    wordlist.sort()

print wordlist

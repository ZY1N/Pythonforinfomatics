#Exercise 10.3 Write a function called most_frequent that takes a string and
#prints the letters in decreasing order of frequency. Find text samples from
#several different languages and see how letter frequency varies between languages. Compare your results with the tables at wikipedia.org/wiki/Letter_
#frequencies.

import string

def most_frequent(s):
    total = 0
    import string
    dictionary = dict()
    s = s.translate(None, string.punctuation) #gets rid of punctuation
    s = s.translate(None, string.digits)
    s = s.lower() #turns all to lower clase
    s = s.split() #splits the string into array of words
    for word in s: #cycle through each of word in s
        letter = list(word)
        for char in letter:
            dictionary[char] = dictionary.get(char, 0) + 1
    lst = list()
    for x, y in dictionary.items():
        total = total + float(y)
        lst.append((y, x))
    lst.sort(reverse=True)
    for x,y in lst:
        print ("%c %.2f%%" % (y, (x/total* 100)))
    print len(dictionary)
    


fname = open("frequency.txt")

string = str()
for line in fname:
    string = string + line
most_frequent(string)


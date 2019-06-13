#Exercise 12.3 Use urllib to replicate the previous exercise of (1) retrieving the
#document from a URL, (2) displaying up to 3000 characters, and (3) counting the
#overall number of characters in the document. Dont worry about the headers for
#this exercise, simply show the first 3000 characters of the document contents.

import urllib

address = raw_input("Enter an URL :")

try:
    url = urllib.urlopen(address)
except:
    print "Error invalid file"

string = str()
total = 0
for line in url:
    for letter in line:
        if total == 3000:
            break
        string = string + letter
        total = total + 1
    if total == 3000:
        break

print string
print total

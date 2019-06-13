#Exercise 10.1 Revise a previous program as follows: Read and parse the From
#lines and pull out the addresses from the line. Count the number of messages from
#each person using a dictionary.
#After all the data has been read print the person with the most commits by creating
#a list of (count, email) tuples from the dictionary and then sorting the list in reverse
#order and print out the person who has the most commits.

fname = raw_input("Enter a file name: ")

try:
    hand = open(fname)
except:
    print "file name is not valid"
    exit()

dictionary = dict()

for line in hand:
    if line.startswith("From "):
        line = line.split()
        dictionary [line[1]] = dictionary.get(line[1], 0) + 1

listoftuples = dictionary.items()


lstup = []
for x, y in listoftuples:
    lstup.append((y, x))

lstup.sort(reverse=True)

print lstup[:1]

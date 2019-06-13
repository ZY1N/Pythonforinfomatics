
fname = raw_input("Enter a file name : ")
handle = open(fname)

dictionary = dict()

for line in handle:
    if line.startswith("From: "):
        line = line.split()
        word = line[1].split('@')
        dictionary[word[1]] = dictionary.get(word[1], 0) + 1
print dictionary

#Exercise 10.2 This program counts the distribution of the hour of the day for
#each of the messages. You can pull the hour from the From line by finding the
#time string and then splitting that string into parts using the colon character. Once
#you have accumulated the counts for each hour, print out the counts, one per line,
#sorted by hour as shown below.

fname = raw_input('Enter a file name : ')
handle = open(fname)

dictionary = dict()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        time = time.split(':')
        hour = time[0]
        dictionary[hour] = dictionary.get(hour, 0) + 1

lst = list()

for x, y in dictionary.items():
    lst.append((x, y))

lst.sort()

for x, y in lst:
    print x, y

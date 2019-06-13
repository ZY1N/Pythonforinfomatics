import re

handle = open("mbox.txt")

string = str()

for line2 in handle:
    string = string + line2

y = re.findall('New Revision:\s([0-9]+)', string)

total = 0
for x in y:
    x = int(x)
    total = total + x

print (float(total)/(len(y)))

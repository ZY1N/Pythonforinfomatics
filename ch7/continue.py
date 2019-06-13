fhand = open ('mbox.txt')
for line in fhand:
    line = line.rstrip()
    #skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    #print the interesting line
    print line

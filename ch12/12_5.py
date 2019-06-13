#Exercise 12.5 (Advanced) Change the socket program so that it only shows data
#after the headers and a blank line have been received. Remember that recv is
#receiving characters (newlines and all) - not lines.

import socket
import re


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

string = str()

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    string = string + data

noheader = re.findall("<.*>", string)

for line in noheader:
    print line
mysock.close()

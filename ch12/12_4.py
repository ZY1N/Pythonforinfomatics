#Exercise 12.4 Change the urllinks.py program to extract and count paragraph
#(p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text - only
#count them. Test your program on several small web pages as well as some larger
#web pages.

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('p')

print len(tags)

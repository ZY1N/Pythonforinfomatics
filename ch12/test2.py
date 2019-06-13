import re
import urllib


name = raw_input("Enter URL : ")
html = urllib.urlopen(name).read()

listofhtml = re.findall('href="(http://.*?)"', html)


print listofhtml

for line in listofhtml:
    print line



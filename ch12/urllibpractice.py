import urllib
import re

name = raw_input("Enter URL Address :")

html = urllib.urlopen(name).read()

links = re.findall('href="(http://.*?)"', html)

for line in links:
    print line

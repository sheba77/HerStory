import re
from urllib.request import urlopen

f = open("links", "r")
links = []
newLinks = []

for x in f:
    links.append(x)

f.close()

for myLink in links:
    blue = re.split(r"/", myLink)
    names = blue[-1]
    stripedname = names.rstrip("\n\r").strip(",") + '/'
    result = stripedname + names.rstrip("\n\r") + '-0.txt'
    newLinks.append(myLink.replace(names, result))

for lo in newLinks:
    print(lo)


import re
from urllib.request import urlopen

##
# Opens a file called links which contains links to books in https://www.gutenberg.org/
# and access the txt version of the books wanted.
#
##


def books_scraper():
    # open file
    f = open("links", "r")
    links = []
    newLinks = []

    # appends all links from file into list
    for x in f:
        links.append(x)

    # close file
    f.close()

    # go through each link and transform the link info the link that will lead straight into the txt file
    for myLink in links:
        blue = re.split(r"/", myLink)
        names = blue[-1]
        stripedname = names.rstrip("\n\r").strip(",") + '/'
        result = stripedname + names.rstrip("\n\r") + '-0.txt'
        newLinks.append(myLink.replace(names, result))

    # print files 
    for lo in newLinks:
        print(lo)


import urllib.request as ur
from bs4 import *

website = input('Type in URL: ')
repeat = int(input('How many times would you like to repeat this: '))
position = int(input('Enter the position: ')) - 1
urllist = list()
urllist.append(website)

print ('Retrieving: ', urllist[0])

tag_list = list()
for i in range(repeat):
    opening = ur.urlopen(urllist[-1]).read()
    soup = BeautifulSoup(opening,"lxml")
    tags = soup('a')
    tag_list = list()
    for tag in tags:
        tag_list.append(tag)
    url = tag_list[position].get('href', None)
    print ('Retrieving: ', url)
    urllist.append(url)



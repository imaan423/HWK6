import urllib.request as ur
from bs4 import *

url = input('Enter URL: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Alesha.html"
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1
taglist = list()
urllist = list()
urllist.append(url)

print ('Retrieving: ', urllist[0])


for i in range(count):
    html = ur.urlopen(urllist[-1]).read()
    soup = BeautifulSoup(html,"lxml")
    tags = soup('a')
    taglist = list()
    for tag in tags:
        taglist.append(tag)
    url = taglist[pos].get('href', None)
    print ('Retrieving: ', url)
    urllist.append(url)



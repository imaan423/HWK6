import urllib.request as ur
import re
from bs4 import *

website = 'http://py4e-data.dr-chuck.net/comments_37795.html'
html = ur.urlopen(website).read()

soup = BeautifulSoup(html,"html.parser")
sum=0


finding = soup('span')
for tag in finding:
    y=str(tag)
    total= re.findall("[0-9]+",y)
    for i in total:
        i=int(i)
        sum=sum+i
print (sum)

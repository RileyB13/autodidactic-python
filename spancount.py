from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span elements
tags = soup('span')
numlist = list()
count = 0
for tag in tags:
    numlist.append(int(tag.contents[0]))
    count = count + 1

print(count)
print(sum(numlist))

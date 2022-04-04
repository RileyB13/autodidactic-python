from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor elements
tags = soup('a')
count = int(input('Enter Count: '))
position = int(input('Enter position: '))
pos = position - 1
while count > 0:
    tags = soup('a')
    newrl = tags[pos].get('href', None)
    html = urlopen(newrl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count - 1
    print(newrl)

print(tags[pos].contents)

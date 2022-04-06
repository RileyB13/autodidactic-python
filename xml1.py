import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst = list()
lst = tree.findall('comments/comment/count')
print("Count: ", len(lst))
counts = list()
for item in lst:
    counts.append(item.text)
counts = [int(x) for x in counts]
print("Sum: ", sum(counts))

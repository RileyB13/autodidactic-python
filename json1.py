import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
info = json.loads(data)
lst = info['comments']
print("Retrieved ", len(data), "characters")
count = list()
counts = 0
for item in lst:
    count.append(item['count'])
    counts = counts + 1
print("Count: ", counts)
print("Sum: ", sum(count))

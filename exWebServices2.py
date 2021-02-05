import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
#print(json.dumps(js, indent=2))
numlst = []

for i in js['comments']:
    numlst.append(i['count'])

print(sum(numlst))

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

uh = urllib.request.urlopen(url)
data = uh.read().decode()
xml = ET.fromstring(data)
countlst = xml.findall('.//count')
#print(countlst)
numlst = []
for c in countlst:
    c = int(c.text)
    numlst.append(c)

print(sum(numlst))
# from strCount import *
"""
word = 'Vanana'
if word < 'banana':
	print('your word, ' + word + ', comes before banana.')
elif word > 'banana':
	print('your word, ' + word + ', comes after banana.')
else:
	print('all right, bananas.')	
"""
"""
greet = 'Hello Bob'
zap = greet.lower()
print(zap)	
print(greet)	
print('Hi There'.lower())
x = None
print(dir(x))
"""
"""
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)
"""
"""
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)
"""
"""
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'x')
print(nstr)
"""
"""
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1 : sppos]
print(host)
"""
"""
fhand = open('mbox-short.txt')
print(fhand)
"""
"""
stuff = 'Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
print(len(stuff))
"""
"""
xfile = open('mbox-short.txt')
for cheese in xfile:
	print(cheese)
"""
"""
fhand =  open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:21])
"""
#Chapter: Lists
"""
print([1,[5, 6], 7])

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
	print('Happy New Year:', friend)
print('Done!')
"""
"""
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
"""
"""
fruit = 'Banana'
#fruit[0] = 'b'
x = fruit.lower()
print(x)
"""
"""
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)
"""
"""
greet = 'Hello Bob'
print(len(greet))
"""
"""
x = [1, 2, [5, 6, 7], 'joe', 99]
print(len(x))
"""
"""
#print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
#print(len(friends))
#print(range(len(friends)))
for i in range(len(friends)):
	friend = friends[i]
	print('Happy New Year:', friend)
"""
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)
"""
"""
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
"""
"""
x = list()
print(type(x))
print(dir(x))
"""
"""
stuff = list()
stuff.append('book')
stuff.append('99')
print(stuff)
stuff.append('cookie')
print(stuff)
stuff.sort()
print(stuff)
"""
"""
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)
"""
"""
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])
"""
"""
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
"""
"""
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
	print(w)
"""
"""
line = 'A lot 	  	    of spaces'
etc = line.split()
print(etc)
"""
"""
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))
"""
"""
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From '):
		continue
	words = line.split()
	print(words[2])
"""
"""
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
print(pieces[1])
"""
"""
x = list(range(5))
print(x)
"""

#Chapter: Dictionaries

"""
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)
"""
"""
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)
"""
"""
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)
"""
"""
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
"""
"""
ccc = dict()
#print(ccc['csev'])
print('csev' in ccc)
"""
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print(counts)

if name in counts:
	x = counts[name]
else:
	x = 0

x = counts.get(name, 0)
print(x)
"""
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
	counts[name] = counts.get(name, 0) + 1
print(counts)
"""
"""
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
	counts[word] = counts.get(word, 0) + 1
print('Counts', counts)
"""
"""
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
	print(key, counts[key])
"""
"""
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())
"""
"""
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():
	print(aaa, bbb)
"""

#Chapter: Tuples
"""
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))
for iter in y:
	print(iter)
"""
"""
x = [9, 8, 7]
x[2] = 6 
print(x)
"""
"""
y = 'ABC'
y[2] = 'D'
print(y)
"""
"""
z = (5, 4, 3)
z[2] = 0
print(z)
"""
"""
x = (3, 2, 1)
#x.sort()
#x.append(5)
#x.reverse()
print(x)
"""
"""
x = 'Bad'
#x.append('a')
print(dir(x))
"""
"""
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)
"""
"""
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
	print(k, v)

tups = d.items()
print(tups)
"""
"""
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))
"""
"""
d = {'a': 20, 'd': 130, 'c': 22}
print('a', d.items())
print(sorted(d.items()))
"""
"""
d = {'b':10, 'a':1, 'c':22}
t = sorted(d.items())
print(t)

for k,v in sorted(d.items()):
	print(k, v)
"""
"""
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
	tmp.append((v, k))

print(tmp)
tmp = sorted(tmp)
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)
"""
"""
#from top10CommonWords import *

c = {'a':10, 'b':1, 'c':22}
print(sorted([(v, k) for k,v in c.items()]))
print(sorted([(v, k) for k,v in c.items()], reverse = True))
"""
#Chapter: Regular Expressions

"""
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:') >= 0:
		print(line)
"""
"""
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line):
		print(line)
"""
"""
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)
"""
"""
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:', line):
		print(line)
"""
"""
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^X.*:', line):
		print(line)
"""
"""
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^X-.\S+:', line):
		print(line)
"""
"""
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+', x)
print(y)
"""
"""
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
"""
"""
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
"""
"""
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
"""
"""
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)
"""
"""
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print(y)
"""
"""
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)
"""
"""
import re
hand = open('mbox-short.txt')
numlist  = list()
for line in hand:
	line = line.rstrip()
	#print(line)
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	#print(stuff)
	if len(stuff) != 1 : continue
	num = float(stuff[0])
	numlist.append(num)
	#print('a', numlist)
print('Maximum:', max(numlist))
"""
"""
import re 
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
"""
#Chapter: Network Programming
"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
"""
"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	print(data.decode())
mysock.close()
"""
"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode()
    print(data.decode(),end='')
mysock.close()
"""
"""
print(ord('H'))
print(ord('e'))
print(ord('\n'))
"""
"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	line = line.decode().strip()
	print(line)
"""
"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
for k, v in counts.items():
	print(v, k)
"""
"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
	print(line.decode().strip())
"""
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)
for tag in tags:
	print(tag.get('href', None))
"""
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))
"""
#Chapter: Web Services

"""
import xml.etree.ElementTree as ET

data = '''
<person>
	<name>Chuck</name>
	<phone type="intl">
		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
"""

"""
import xml.etree.ElementTree as ET

input = '''
<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(lst)
print('User count:', len(lst))

for item in lst:
	print('Name', item.find('name').text)
	print('Id', item.find('id').text)
	print('Attribute', item.get("x"))
"""

"""
import json
data = '''{
	"name" : "Chuck",
	"phone" : {
		"type" : "intl",
		"number" : "+1 734 303 4456"
	},
	"email" : {
		"hide" : "yes"
	}
}'''

info = json.loads(data)
print(info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
"""

"""
import json
input = '''[
	{ "id" : "001",
	  "x" : "2",
	  "name" : "Chuck"
	} ,
	{ "id" : "009",
	  "x" : "7",
	  "name" : "Chuck"
	}
]'''

info = json.loads(input)
print(info)

print('User count: ', len(info))
for item in info:
	print('Name', item['name'])
	print('Id', item['id'])
	print('Attribute', item['x'])
"""

'''
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print('Dump', json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
'''

'''
import urllib.request, urllib.parse, urllib.error
import twurl
import json

<<<<<<< HEAD
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
=======
TWITTER_URL = 'https://api.twitter.com/1.1.friends/list.json'
>>>>>>> 13382388d6aa4d29709f573b0f1054046f42667d

while True:
	print('')
	acct = input('Enter Twitter Account:')
	if (len(acct) < 1): break
	url = twurl.augment(TWITTER_URL,
						{'screen_name': acct, 'count': '5'})
	print('Retrieving', url)
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
	headers = dict(connection.getheaders())
	print('Remaining', headers['x-rate-limit-remaining'])
	js = json.loads(data)
<<<<<<< HEAD
	#print(json.dumps(js, indent=4))

	for u in js['users']:
		print(u['screen_name'])
		if 'status' not in u:
			print('   * No status found')
			continue
		s = u['status']['text']
		print('  ', s[:50])
'''
=======
	print(json.dumps(js, indent=4))

	for u in js['users']:
		print(u['screen_name'])
		s = u['status']['text']
		print('	', s[:50])
'''		

>>>>>>> 13382388d6aa4d29709f573b0f1054046f42667d
#chapter: OOP

'''
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()

#PartyAnimal.party(PartyAnimal)

print('Type', type(an))
print('Dir', dir(an))
'''

'''
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
'''

'''
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
'''

<<<<<<< HEAD

		
=======
'''
class PartyAnimal:
	x = 0
	name = ''
	def __init__(self, nam):
		self.name = nam
		print(self.name, 'constructed')

	def party(self):
		self.x = self.x + 1
		print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal):
	points = 0
	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()
'''
>>>>>>> 13382388d6aa4d29709f573b0f1054046f42667d

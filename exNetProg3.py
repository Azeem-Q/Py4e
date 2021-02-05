"""
Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Adil.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
"""
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
urllst = []
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

taglst = []
namelst = []
tags = soup('a')
for tag in tags:

	#tag = str(tag)
	#taglst.append(tag)
#print(type(tags))
#tags = str(tags)
#print(tags)
#print(tags[2].find('a'))
#namelst.append(tags[2].find('>'))
#print(taglst[2][65:])
"""

#Test Sample
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#count = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
namepos = url.find('_')
dotpos = url.find('.html')
namelst = []
namelst.append(url[namepos + 4:dotpos])
for i in range(4):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	tag = str(tags[2])
	qpos = tag.find('"')
	cbrpos = tag.find('>')
	url = tag[qpos + 1:cbrpos - 1]
	print(url)
	namepos = url.find('_')
	#print(namepos)
	dotpos = url.find('.html')
	#print(dotpos)
	namelst.append(url[namepos + 4:dotpos])
	continue

print(namelst)
"""

#Actual Problem

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Adil.html'
namepos = url.find('_')
dotpos = url.find('.html')
namelst = []
namelst.append(url[namepos + 4:dotpos])
for i in range(7):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	tag = str(tags[17])
	qpos = tag.find('"')
	cbrpos = tag.find('>')
	url = tag[qpos + 1:cbrpos - 1]
	print(url)
	namepos = url.find('_')
	#print(namepos)
	dotpos = url.find('.html')
	#print(dotpos)
	namelst.append(url[namepos + 4:dotpos])
	continue

print(namelst)
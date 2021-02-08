"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = {}
lst = []

for line in handle:
	if line.startswith('From '):
		colp = line.find(':')
		hrs = line[colp - 2:colp]
		counts[hrs] = counts.get(hrs, 0) + 1

for k, v in counts.items():
	lst.append((k, v))

lst.sort()
for k, v in lst:
	print(k, v)
	#print(*i, sep=' ')
#print(sorted(lst))
		#print(line)
#print(lst)

#for items in lst:

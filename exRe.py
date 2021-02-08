"""
name = input('Enter Filename:')
if len(name) < 1: name = 'regex_sum_42.txt'
handle = open(name)
lst = []
import re
x = re.findall('[0-9]+', handle.read())
for i in x:
	i = int(i)
	lst.append(i)
print(sum(lst))
"""

#Method 2
import re
print( sum( [int(i) for i in re.findall('[0-9]+',open('regex_sum_1039254.txt').read()) ] ) )

"""
import re
print( sum( [ ****** for i in re.findall('[0-9]+'),regex_sum_1039254.txt.read()) ] ) )
"""
#print(sum(lst))
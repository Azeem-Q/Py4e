# Use the file name mbox-short.txt as the file name
"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

Answer = Average spam confidence: 0.7507185185185187
"""
fname = input("Enter file name: ")
avgList = []
fh = open(fname)
for line in fh:
		if not line.startswith("X-DSPAM-Confidence:"):
			continue
		avgn = float(line[20:])
		avgList.append(avgn) 
		#for numbers in avgn:
			#avg = 0 + avgn
avgs = 0.0
count = 0
for number in avgList:
	avgs = avgs + number
for number in avgList:
	count = count + 1
avg = avgs / count
print('Average spam confidence:', avg)
largest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
	if largest is None:
		largest = value
	elif value > largest:
		largest = value
	print(largest, value)
print('After', largest)

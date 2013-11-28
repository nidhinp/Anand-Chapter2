""" Write a function group(list, size) that takes a list and splits
    into smaller lists of given size.
"""

def group(x, size):
	count = len(x) / size
	start = 0
	end = size
	b = []
	while count > 0:
		b.append(x[start:end])
		start += size
		end += size
		count -= 1
	end -= size
	b.append(x[end:])
	return b
print group(range(20), 3)

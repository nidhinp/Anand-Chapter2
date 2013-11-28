""" Write a function enumerate that takes a list and returns a list
    of tuples containing (index, item) for each item in the list.
"""

def enumerate(lists):
	return [(i, lists[i]) for i in range(len(lists))]

for index, value in enumerate(['a','b', 'c']):
	print index, value

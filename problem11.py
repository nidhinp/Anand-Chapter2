""" Write a function duplicate to find all duplicates in the list.
"""

def duplicates(x):
	return list(set([a for a in x if x.count(a) > 1]))
print duplicates([1, 1, 1, 2, 2 , 8, 2, 3, ])

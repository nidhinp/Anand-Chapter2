""" Reimplement the unique function implemented in the earlier example using sets.
"""

def unique(x):
	return list(set(x))

print unique([1, 2, 3, 3, 2, 8, 9])

""" Python has built-in functions min and max to compute minimum and maximum
    of a list. Provide an implementation for these functions.
"""

def my_min(x):
	min = x[0]
	for i in x:
		if i <= min:
			min = i
	return min
def my_max(x):
	max = x[0]
	for i in x:
		if i >= max:
			max = i
	return max
print my_min([6, 5, 1, 3, 2])
print my_max([2, 1, 6, 8])

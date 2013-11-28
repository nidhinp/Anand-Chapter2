""" Python has a built-in function sum to find sum of all elements
    of a list. Provide an implementation for sum.
"""

def my_sum(x):
	sum = 0
	for i in x:
		sum += i
	return sum
print my_sum([1, 2, 3, 4])


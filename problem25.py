""" Python provides a built-in function map that applies a function to
    each element of a list. Provide an implementation for map using list
    comprehensions.
"""

def square(x):
	return x * x

def my_map(function, lists):
	return [function(i) for i in lists]

print my_map(square, range(5))

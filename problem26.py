""" Python provides a built-in function filter(f, a) that returns items of
    the list a for which f(item) returns true. Provide an implementation for
    filter using list comprehensions.
"""

def even(x): 
	return x % 2 == 0

def my_filter(function, list):
	return [x for x in list if function(x)]

print my_filter(even, range(10))

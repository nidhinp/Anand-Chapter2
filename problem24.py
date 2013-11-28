""" Provide an implementation for zip function using list comprehensions.
"""

def my_zip(list1, list2):
	return [(list1[i], list2[i]) for i in range(min(len(list1),len(list2)))]
print my_zip([1, 2, 3], ['a', 'b', 'c'])

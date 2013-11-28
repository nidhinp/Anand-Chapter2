""" Write a function invertdict to interchange keys and values in a
    dictionary. For simplicity assume all values are unique.
"""

def invertdict(dictionary):
	a = {}
	for x in dictionary:
		a.update({dictionary[x]:x})
	print a

invertdict({'x':1, 'y':2, 'z':3})

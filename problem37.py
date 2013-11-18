import operator
def valuesort(dictionary):
	a = []
	for key, value in sorted(dictionary.iteritems(), key = operator.itemgetter(0)):
		a.append(value)
	print a	

valuesort({'x':1, 'y':2, 'a':3})

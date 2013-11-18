def even(x): 
	return x % 2 == 0

def my_filter(function, list):
	return [x for x in list if function(x)]

print my_filter(even, range(10))

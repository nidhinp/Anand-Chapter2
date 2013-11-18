def square(x):
	return x * x

def my_map(function, lists):
	return [function(i) for i in lists]

print my_map(square, range(5))

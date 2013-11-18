def my_reverse(x):
	a = []
	for i in x:
		a.insert(0, i)
	return a
print my_reverse(range(3))
print my_reverse(my_reverse(range(3)))

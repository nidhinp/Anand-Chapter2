def unique(x):
	a = []
	for i in x:
		if i not in a:
			a.append(i)
	return a
print unique([1, 2, 1, 3, 2, 5])
	

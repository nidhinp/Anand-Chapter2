def extsort(x):
	return sorted(x, key = lambda i: i.split('.')[1])
print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

def enumerate(lists):
	return [(i, lists[i]) for i in range(len(lists))]

for index, value in enumerate(['a','b', 'c']):
	print index, value

def unique(x, key):
	a = []
	for i in [key(i) for i in x]:
		if i not in a:
			a.append(i)
	return a

print unique(['python', 'java', 'Python', 'Java'], key = lambda s: s.lower())

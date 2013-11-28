""" Improve the unique function written in previous problems to take an
    optional key function as argument and use return value of the key
    function to check for uniqueness.
"""

def unique(x, key):
	a = []
	for i in [key(i) for i in x]:
		if i not in a:
			a.append(i)
	return a

print unique(['python', 'java', 'Python', 'Java'], key = lambda s: s.lower())

""" Sum function that works for a list of string as well
"""

def my_sum(x):
	sum = x[0]
	for i in x:
		if i == x[0]:
			continue
		else:
			sum += i
	return sum
print my_sum([1, 2, 3, 4])
print my_sum(['c', 'java', 'python'])

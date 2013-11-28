""" Write a function cumulative product to compute cumulative product of
    a list of numbers.
"""

def product(lists):
	product = 1
	for x in lists:
		product *= x
	return product
def cumulative_product(lists):
	a = []
	for x in lists:
		position = lists.index(x)
		if position == len(lists):
			a.append(product(lists))
		else:
			a.append(product(lists[:position+1]))
	return a
print cumulative_product([1, 2, 3, 4])
print cumulative_product([4, 3, 2, 1])

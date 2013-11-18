def my_product(x):
	product = 1
	for i in x:
		product = product * i
	return product
print my_product([1, 2, 3, 4])

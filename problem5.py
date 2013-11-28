""" Write a function factorial to compute factorial of a number.
"""

def factorial(x):
	if x == 0:
		return 1
	if x == 1:
		return 1
	else:
		return x * factorial(x - 1)
print factorial(5)

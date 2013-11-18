def triplets(number):
	return [(a, b, c) for a in range(1, number) for b in range(1, number) for c in range(1, number) if a + b == c]
print triplets(5)

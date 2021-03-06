""" Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
    Write a function cumulative_sum to compute sum of a list.
"""

def cumulative_sum(lists):
	a = []
	for x in lists:
		position = lists.index(x)
		if position == len(lists):
			a.append(sum(lists))
		else:
			a.append(sum(lists[:position+1]))
	return a
print cumulative_sum([1, 2, 3, 4])
print cumulative_sum([4, 3, 2, 1])

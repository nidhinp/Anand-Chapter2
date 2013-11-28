""" Print the words in the descending order of the number of occurances.
"""

import operator

def wordcount_descending(filename):
	frequency = {}
	for word in open(filename).read().split():
		frequency[word] = frequency.get(word, 0) + 1
	for key, value in sorted(frequency.iteritems(), key = operator.itemgetter(1), reverse = True):
		print key, value

wordcount_descending('she.txt')

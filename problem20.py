import sys

def grep(filename, word):
	for f in open(filename):
		if word in f:
			print f

if len(sys.argv) < 3:
	print 'usage: grep.py filename word'
else:
	grep(sys.argv[1], sys.argv[2])

	

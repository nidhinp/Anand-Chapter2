""" Implement a unix command grep. The grep command takes a string and a file 
    as arguments and prints all lines in the file which contains the specified
    string.
"""

import sys

def grep(filename, word):
	for f in open(filename):
		if word in f:
			print f

if len(sys.argv) < 3:
	print 'usage: grep.py filename word'
else:
	grep(sys.argv[1], sys.argv[2])

	

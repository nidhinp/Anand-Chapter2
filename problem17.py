""" Write a program to print lines of a file in reverse order.
"""

import sys

def line_reverse(filename):
	f = open(filename)
	list_of_lines = f.readlines()
	for i in list_of_lines[::-1]:
		print i

if len(sys.argv) < 2:
	print 'usage: python problem17.py filename'
else:
	line_reverse(sys.argv[1])

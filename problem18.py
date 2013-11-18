import sys

def each_line_reverse(filename):
	f = open(filename)
	list_of_lines = f.readlines()
	for x in list_of_lines:
		print x[::-1]

if len(sys.argv) < 2:
	print 'usage: python problem18.py filename'
else:
	each_line_reverse(sys.argv[1])

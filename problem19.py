import sys

def head_and_tail(filename):
	f = open(filename)
	list_of_lines = f.readlines()
	print 'head 10 lines.....'
	for x in list_of_lines[0:10]:
		print x
	print 'tail 10 lines.....'
	for x in list_of_lines[-10:-1]:
		print x

if len(sys.argv) < 2:
	print 'usage: python problem19.py filename'
else:
	head_and_tail('help.txt')
		

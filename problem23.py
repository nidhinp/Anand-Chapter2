import sys

def longest_line(filename):
	longest = 0
	for line in open(filename):
		if len(line) > longest:
			longest = len(line)
	return longest

def generate_space(number):
	return ' ' * number

def append_with_spaces(line):
	difference = longest_line(sys.argv[1]) - len(line)
	if difference % 2 == 0:
		return generate_space(difference / 2) +line+ generate_space(difference / 2)
	else:
		return generate_space((difference / 2) + 1) +line+ generate_space(difference / 2)

def center_align(filename):
	for line in open(filename):
		if len(line) == longest_line(filename):
			print line
		else:
			print append_with_spaces(line)

if len(sys.argv) < 2:
	print 'usage: python problem23.py filename'
else:
	center_align(sys.argv[1])

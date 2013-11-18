import sys
def file_line(filename):
	line_list = []
	for f in open(filename):
		line_list.append(f)
	return line_list

def wordwrap(filename, width):
	line_list = file_line(filename)
	for line in line_list:
		line.strip()
		if line[width - 1] == ' ':
			print line[:width - 1].strip()
			print line[width - 1:].strip()
		else:
			while line[width] == ' ':
				width += 1
			else:
				print line[:width - 1].strip()
				print line[width- 1:].strip()					
if len(sys.argv) < 2:
	print 'usage python problem22.py filename width'
else:
	wordwrap(sys.argv[1], int(sys.argv[2]))

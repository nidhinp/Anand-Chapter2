import sys

def wrapline(files, width):
	for x in open(files).readlines():
		if len(x) < width:
			print x
		else:
			print x[:width]
			print x[width:]
			
			
if len(sys.argv) < 3:
	print 'usage: wrapline_2_21.py filename width'
else:
	wrapline(sys.argv[1], int(sys.argv[2]))

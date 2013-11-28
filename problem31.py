""" Generalize csv parser to support any delimiter and comments.
"""

def parser_generalized(filename, delimiter, comments):
	return [line.split()[0].split(delimiter) for line in open(filename) if line[0] <> comments]

print parser_generalized('a.txt', '!', '#')

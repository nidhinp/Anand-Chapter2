""" Write a python function parse_csv to parse csv files.
"""

def parse_csv(file):
	return [line.split()[0].split(',') for line in open(file)]

print parse_csv('a.csv')

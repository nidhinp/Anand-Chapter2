def parse_csv(file):
	return [line.split()[0].split(',') for line in open(file)]

print parse_csv('a.csv')

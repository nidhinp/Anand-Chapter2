""" Write a program to count frequency of characters in a given file.
"""

def countcharacter(filename):
	frequency = {}
	for character in open(filename).read():
		frequency[character] = frequency.get(character, 0) + 1
	for key, value in frequency.items():
		print key, value

countcharacter('she.txt')

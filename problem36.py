def sorted_characters_of_word(word):
	b = sorted(word)
	c = ''
	for character in b:
		c += character
	return c
def anagram(list_of_words):
	a = {}
	for word in list_of_words:
		sorted_word = sorted_characters_of_word(word)
		if sorted_word not in a:
			d = []
			d.append(word)
			a[sorted_word] = d
		else:	
			d = a[sorted_word]
			d.append(word)
			a.update({sorted_word:d})
	print a.values()
	

anagram(['eat', 'ate', 'done', 'tea', 'soup', 'node'])		

""" Write a function array to create an 2-dimensional array. The function 
    should take both dimensions as arguments. Value of element can be
    initialized to None:
"""

def array(oneD, twoD):
	return [[None for x in range(twoD)] for x in range(oneD)]
	
a = array(2, 3)
print 'None initialized array'
print a
a[0][0] = 5
print 'Modified array'
print a

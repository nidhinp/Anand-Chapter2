def array(oneD, twoD):
	return [[None for x in range(twoD)] for x in range(oneD)]
	
a = array(2, 3)
print 'None initialized array'
print a
a[0][0] = 5
print 'Modified array'
print a

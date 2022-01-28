# O(nlogn + mlogm) | O(1) space
def smallestdifference(array1,array2):
	array1.sort()
	array2.sort()
	idxone = 0
	idxtwo = 0
	smallest = float('inf')
	current = float('inf')
	smallestpair = []
	while idxone < len(array1) and idxtwo < len(array2):
		firstnum = array1[idxone]
		secondnum = array2[idxtwo]
		if  firstnum < secondnum:
			current = secondnum - firstnum
			idxone += 1
		elif secondnum < firstnum:
			current = firstnum - secondnum
			idxtwo += 1
		else:
			return [firstnum,secondnum]
		if smallest > current:
			smallest = current
			smallestpair = [firstnum,secondnum]
	return smallestpair

print(smallestdifference([20,51,45,78,98],[50,48,96,85,23,14,58,100]))
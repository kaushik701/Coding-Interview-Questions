# O(n^2) time | O(n^2) space
def SameBSTs(arrayOne,arrayTwo):
	if len(arrayOne) != len(arrayTwo):
		return False
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	if arrayOne[0] != arrayTwo[0]:
		return False
	leftOne = getSmaller(arrayOne)
	leftTwo = getSmaller(arrayTwo)
	rightOne = getBiggerOrEqual(arrayOne)
	rightTwo = getBiggerOrEqual(arrayTwo)
	return SameBSTs(leftOne,leftTwo) and SameBSTs(rightOne,rightTwo)

def getSmaller(array):
	smaller = []
	for i in range(1,len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])
	return smaller

def getBiggerOrEqual(array):
	biggerOrEqual = []
	for i in range(1,len(array)):
		if array[i] >= array[0]:
			biggerOrEqual.append(array[i])
	return biggerOrEqual

print(SameBSTs([10,5,8,2,14,15,11,95,84],[10,5,8,2,14,15,11,95,84]))
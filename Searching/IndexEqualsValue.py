# O(n) time | O(1) space
def IndexEqualsValue(array):
	for index in range(len(array)):
		value = array[index]
		if index == value:
			return index
	return -1

# O(log(n)) time | O(log(n)) space
def IndexEqualsValue1(array):
	return IndexEqualsValueHelper(array,0, len(array)-1)

def IndexEqualsValueHelper(array, leftIndex, rightIndex):
	if leftIndex > rightIndex:
		return -1

	middleIndex = leftIndex + (rightIndex - leftIndex) // 2
	middleValue = array[middleIndex]

	if middleValue < middleIndex:
		return IndexEqualsValueHelper(array, middleIndex+1, rightIndex)
	elif middleValue == middleIndex and middleIndex == 0:
		return middleIndex
	elif middleValue == middleIndex and array[middleIndex-1] < middleIndex-1:
		return middleIndex
	else:
		return IndexEqualsValueHelper(array, leftIndex,middleIndex-1)

# O(log(n)) time | O(1) space
def IndexEqualsValue2(array):
	leftIndex = 0
	rightIndex = len(array) - 1

	while leftIndex <= rightIndex:
		middleIndex = leftIndex + (rightIndex - leftIndex) // 2
		middleIndex = array[middleIndex]

		if middleValue < middleIndex:
			leftIndex = middleIndex + 1
		elif middleValue == middleIndex and middleIndex == 0:
			return middleIndex
		elif middleValue == middleIndex and array[middleIndex-1] < middleIndex -1:
			return middleIndex
		else:
			rightIndex = middleIndex - 1
	return -1

print(IndexEqualsValue([-5,-3,0,4,5,5,9]))
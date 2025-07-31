# Leetcode #977: https://youtu.be/z0InhrjK3es?si=o9XSr-p398ITaZF7
# O(n) time | O(n) space
array = list(map(int,input('Enter the Numbers: ').split()))
def SortedSquaredArray(array):
	result = [0 for _ in array]
	left = 0
	right = len(array)-1
	for i in reversed(range(len(array))):
		if abs(array[left]) > array[right]:
			result[i] = array[left] * array[left]
			left += 1
		else:
			result[i] = array[right] * array[right]
			right -= 1
	return result

# O(nlog(n)) time | O(n) space
def SortedSquaredArray1(array):
	if len(array) == None:
		return None

	sortedSquares = [0 for _ in array]
	left = 0
	right = len(array) - 1
	for idx in range(len(array)):
		value = array[idx]
		sortedSquares[idx] = value * value
	sortedSquares.sort()
	return sortedSquares

# O(n) time | O(n) space
def SortedSquaredArray2(array):
	sortedSquares = [0 for _ in array]
	smallestValueIdx = 0
	largerValueIdx = len(array) - 1
	for idx in reversed(range(len(array))):
		smallerValue = array[smallestValueIdx]
		largerValue = array[largerValueIdx]

		if abs(smallerValue) > abs(largerValue):
			sortedSquares[idx] = smallerValue*smallerValue
			smallestValueIdx += 1
		else:
			sortedSquares[idx] = largerValue*largerValue
			largerValueIdx -= 1
	return sortedSquares

print(SortedSquaredArray(array))
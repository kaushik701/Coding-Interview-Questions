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

print(SortedSquaredArray(array))
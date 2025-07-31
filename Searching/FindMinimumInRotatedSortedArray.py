# Leetcode #153: https://youtu.be/nIVW4P8b1VA?si=7FWEKrVY6lIflFad
# O(log(n)) time | O(n) space
def MinimumInRotatedSortedArray(array):
	result = array[0]
	left, right = 0, len(array)-1
	while left <= right:
		if array[left] < array[right]:
			result  =  min(result,array[left])
			break

		middle = (left+right) // 2
		result = min(result,array[middle])
		if array[middle] >= array[left]:
			left = middle + 1
		else:
			right = middle - 1

	return result
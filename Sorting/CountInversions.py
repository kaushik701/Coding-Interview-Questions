# O(nlogn) time | O(n) space
def CountInversions(array):
	if len(array) == 0:
		return 0
	return CountSubArrayInversions(array, 0, len(array))

def CountSubArrayInversions(array, start, end):
	if end - start <= 1:
		return 0
	middle = start + (end - start) // 2
	leftInversions = CountSubArrayInversions(array, start, middle)
	rightInversions = CountSubArrayInversions(array, middle, end)
	mergedArrayInversions = mergeSortAndCountInversions(array, start, middle, end)
	return leftInversions + rightInversions + mergedArrayInversions

def mergeSortAndCountInversions(array,start, middle, end):
	sortedArray = []
	left = start
	right = middle
	inversions = 0

	while left < middle and right < end:
		if array[left] <= array[right]:
			sortedArray.append(array[left])
			left += 1
		else:
			inversions += middle - left
			sortedArray.append(array[right])
			right += 1
	sortedArray += array[left:middle] + array[right:end]
	for idx, num in enumerate(sortedArray):
		array[start+idx] = num
	return inversions

print(CountInversions([2,3,3,1,9,5,6]))
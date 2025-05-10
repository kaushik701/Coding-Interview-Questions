# O(2^n * n) time | O(2^n * n) space
def PowerSet(array):
	subsets = [[]]
	for element in array:
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [element])
	return subsets

# O(n * 2^n) time | O(n * 2^n) space
def PowerSet2(array, idx = None):
	if idx is None:
		idx = len(array)-1
	elif idx < 0:
		return [[]]
	element = array[idx]
	subsets = PowerSet2(array,idx-1)
	for i in range(len(subsets)):
		currentSubset = subsets[i]
		subsets.append(currentSubset+[element])
	return subsets
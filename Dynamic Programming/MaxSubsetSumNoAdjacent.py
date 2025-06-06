# O(n) time | O(n) space
def MaxSubsetSumNoAdjacent(array):
	if not len(array):
		return False
	elif len(array) == 1:
		return array[0]
	maxSums = array[:]
	maxSums[1] = max(array[0],array[1])
	for i in range(2,len(array)):
		maxSums[i] = max(maxSums[i-1],maxSums[i-2]+array[i])
	return maxSums[-1]

# O(n) time | O(1) space
def MaxSubsetSumNoAdjacent2(array):
	if not len(array):
		return False
	elif len(array) == 1:
		return array[0]
	second = array[0]
	first = max(array[0],array[1])
	for i in range(2,len(array)):
		current = max(first,second+array[i])
		second = first
		first = current
	return first

print(MaxSubsetSumNoAdjacent([1,2,3,5,7,25]))
print(MaxSubsetSumNoAdjacent2([7,10,12,7,9,14]))
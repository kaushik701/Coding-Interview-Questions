# O(n) time | O(1) space
array = list(map(int,input('Enter the Number: ').split()))
def subarraysort(array):
	minOutofOrder = float('inf')
	maxOutofOrder = float('-inf')
	for i in range(len(array)):
		num = array[i]
		if isOutofOrder(i,num,array):
			minOutofOrder = min(minOutofOrder,num)
			maxOutofOrder = max(maxOutofOrder,num)
	if minOutofOrder == float('inf'):
		return [-1,-1]
	subarrayLeftIdx = 0
	while minOutofOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1
	subarrayRightIdx = len(array) - 1
	while maxOutofOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	return [subarrayLeftIdx,subarrayRightIdx]

def isOutofOrder(i,num,array):
	if i == 0:
		return num > array[i+1]
	if i == len(array) -1:
		return num < array[i-1]
	return num > array[i+1] or num < array[i-1]

print(subarraysort(array))

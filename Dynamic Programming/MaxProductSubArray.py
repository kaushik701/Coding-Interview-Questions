# Leetcode #152: https://youtu.be/lXVy6YWFcRM?si=v1DNMFMij8xEsv4R
# O(n) time | O(1) space
def MaxProductSubArray(array):
	result = max(array)
	currentMin, currentMax = 1,1
	for i in array:
		if i == 0:
			currentMin, currentMax = 1,1
			continue
		temp = currentMax*i
		currentMax = max(i*currentMax,i*currentMin,i)
		currentMin = min(temp,i*currentMin,i)
		result = max(result,currentMax)
	return result

print(MaxProductSubArray([2,3,-2,4]))
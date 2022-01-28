#O(n^2) time | O(n) space
def ThreeNumberSum(array,targetSum):
	array.sort()
	triplets = []
	for i in range(len(array)-2):
		left = i+1
		right = len(array)-1
		while left < right:
			currentsum = array[i] + array[left] + array[right]
			if currentsum == targetSum:
				triplets.append([array[i],array[left],array[right]])
				left += 1
				right -= 1
			elif currentsum < targetSum:
				left += 1
			elif currentsum > targetSum:
				right -= 1
	return triplets

a = ThreeNumberSum([-8,1,2,3,6,9,8,7,4],20)
print(a)
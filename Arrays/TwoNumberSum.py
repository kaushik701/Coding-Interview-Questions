#O(n^2) time | O(1) space
def Twonumbersum(array,targetSum):
	for i in range(len(array)-1):
		firstnum = array[i]
		for j in range(i+1,len(array)):
			secondnum = array[j]
			if firstnum+secondnum == targetSum:
				return [firstnum,secondnum]
	return []

a = Twonumbersum([1,2,3,4,5,6,9,-10,8],15)
print(a)

#O(n) time | O(n) space
def Twonumbersum1(array,targetSum):
	nums = {}
	for num in array:
		potenialmatch = targetSum - num
		if potenialmatch in nums:
			return [potenialmatch,num]
		else:
			nums[num] = True
	return []

b = Twonumbersum1([2,4,5,6,9,8,7],20)
print(b)

#O(nlogn) | O(1) space
def Twonumbersum2(array,targetSum):
	array.sort()
	left = 0
	right = len(array)-1
	while left < right:
		currentsum = array[left] + array[right]
		if currentsum == targetSum:
			return [array[left],array[right]]
		elif currentsum < targetSum:
			left += 1
		elif currentsum > targetSum:
			right -= 1
	return []

c = Twonumbersum2([9,8,7,1,4,6,5,-7],-1)
print(c)
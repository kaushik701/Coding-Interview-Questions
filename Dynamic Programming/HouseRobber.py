# Leetcode #198: https://youtu.be/73r3KWiEvyk?si=aTbR_U-QVeLxro9V
# O(n) time | O(1) space
def HouseRobber(nums):
	rob1, rob2 = 0,0
	for i in nums:
		temp = max(i+rob1,rob2)
		rob1 = rob2
		rob2 = temp
	return rob2

# Leetcode #213: https://youtu.be/rWAJCfYYOvM?si=XkxiY3YwPysjGHZt
# O(n) time | O(1) space
def HouseRobber2(nums):
	return max(nums[0], HouseRobber(nums[1:]),HouseRobber(nums[:-1]))

print(HouseRobber([1,2,4,3]))
print(HouseRobber2([2,3,2]))
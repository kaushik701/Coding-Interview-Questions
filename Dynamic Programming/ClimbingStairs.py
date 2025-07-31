# Leetcode: #70: https://youtu.be/Y0lT9Fck7qI?si=Ee89ZjDZ5IeZsUHQ
# O(n) time | O(n) space
def ClimbingStairs(n):
	one, two = 1,1
	for i in range(n-1):
	 	temp = one
	 	one = one + two
	 	two = temp
	return one

print(ClimbingStairs(5))
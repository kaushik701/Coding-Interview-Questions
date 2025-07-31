# Leetcode: #110: https://youtu.be/QfJsau0ItOY?si=t6BOxRMgsUnoyVJ4
# O(n) time | O(n) space
class BinaryTree:
	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right

def BalancedBinaryTree(root):
	DepthFirstSearch(root)[0]

def DepthFirstSearch(root):
	if not root:
		return [True,0]
	left = DepthFirstSearch(root.left)
	right = DepthFirstSearch(root.right)
	balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
	return [balance,1+max(left[1],right[1])]
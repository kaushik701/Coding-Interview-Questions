# O(n) time | O(n) space
class BinaryTree:
	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right

def BalancedBinaryTree(root):
	DFS(root)[0]

def DFS(root):
	if not root:
		return [True,0]
	left = DFS(root.left)
	right = DFS(root.right)
	balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
	return [balance,1,max(left[1],right[1])]
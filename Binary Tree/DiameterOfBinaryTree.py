# O(n) time | O(h) space
class BinaryTree:
	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right
def DiameterOfBinaryTree(root):
	res = [0]
	DFS(root)
	return res[0]

def DFS(root):
	if root is None:
		return -1
	left = DFS(root.left)
	right = DFS(root.right)
	res[0] = max(res[0],(left+right+2))
	return max(left,right) + 1
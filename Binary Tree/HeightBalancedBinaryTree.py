class BinaryTree:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

class TreeInfo:
	def __init__(self,isBalanced,height):
		self.isBalanced = isBalanced
		self.height = height

# O(n) time | O(h) space
def HeightBalancedBinaryTree(tree):
	treeInfo = getTreeInfo(tree)
	return TreeInfo.isBalanced

def getTreeInfo(node):
	if node == None:
		return TreeInfo(True, -1)

	leftSubtreeInfo = getTreeInfo(node.left)
	rightSubtreeInfo = getTreeInfo(node.right)
	isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(leftSubtreeInfo.height- rightSubtreeInfo.height) <= 1
	height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
	return TreeInfo(isBalanced, height)
# O(n+m) time | O(h) space
class BinaryTree:
	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right
def MergeBinarytrees(tree1,tree2):
	if tree1 is None and tree2 is None:
		return None
	value1 = tree1.value if tree1 is not None else 0
	value2 = tree2.value if tree2 is not None else 0
	root = BinaryTree(value1+value2)
	root.left = MergeBinarytrees(tree1.left if tree1 else None,tree2.left if tree2 else None)
	root.right = MergeBinarytrees(tree1.right if tree1 else None,tree2.right if tree2 else None)
	return root
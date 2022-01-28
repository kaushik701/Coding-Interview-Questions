# O(n) time | O(n) space
def InvertBinaryTree(tree):
	queue = [tree]
	while len(queue):
		currentNode = queue.pop(0)
		if currentNode is None:
			continue
		swapLeftAndRight(currentNode)
		queue.append(currentNode.left)
		queue.append(currentNode.right)

def swapLeftAndRight(tree):
	tree.left,tree.right = tree.right,tree.left

# O(n) time | O(d) space d-depth of tree
def InvertBinaryTree1(tree):
	if tree is None:
		return
	swapLeftAndRight1(tree)
	InvertBinaryTree1(tree.left)
	InvertBinaryTree1(tree.right)

def swapLeftAndRight1(tree):
	tree.left,tree.right = tree.right,tree.left
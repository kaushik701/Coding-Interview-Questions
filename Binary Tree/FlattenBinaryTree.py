# O(n) time | O(n) space
def FlattenBinaryTree(root):
	inOrderNodes = getNodesInOrder(root,[])
	for i in range(0,len(inOrderNodes)-1):
		leftNode = inOrderNodes[i]
		rightNode = inOrderNodes[i+1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return inOrderNodes[0]

def getNodesInOrder(tree,array):
	if tree is not None:
		getNodesInOrder(tree.left,array)
		array.append(tree)
		getNodesInOrder(tree.right,array)
	return array

# O(n) time | O(d) space
def FlattenBinaryTree1(root):
	leftMost, _ = flattenTree(root)
	return leftMost

def flattenTree(node):
	if node.left is None:
		leftMost = node
	else:
		leftSubtreeLeftMost,leftSubtreeRightMost = flattenTree(node.left)
		connectNodes(leftSubtreeRightMost,node)
		leftMost = leftSubtreeLeftMost
	if node.right is None:
		rightMost = node
	else:
		rightSubtreeLeftMost,rightSubtreeRightMost = flattenTree(node.right)
		connectNodes(node,rightSubtreeLeftMost)
		rightMost = rightSubtreeRightMost
	return [leftMost,rightMost]

def connectNodes(left,right):
	left.right = right
	right.left = left
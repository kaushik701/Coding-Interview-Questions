# O(log(n)) avg time: O(n) worst time | O(log(n)) avg space: O(n) worst space
def FindClosestValueInBST(tree,target):
	return FindClosestValueInBSTHelper(tree,target,float('inf'))

def FindClosestValueInBSTHelper(tree,target,closest):
	if tree is None:
		return closest
	if abs(target-closest) > abs(target-tree.value):
		closest = tree.value
	if target < tree.value:
		return FindClosestValueInBSTHelper(tree.left,target,closest)
	elif target >  tree.value:
		return FindClosestValueInBSTHelper(tree.right,target,closest)
	else:
		return closest

# O(log(n))avg time: O(n) worst time | O(1) avg space: O(1) worst space
def FindClosestValueInBST1(tree,target):
	return FindClosestValueInBSTHelper1(tree,target,float('inf'))

def FindClosestValueInBSTHelper1(tree,target,closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target-closest) > abs(target-currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target >  tree.value:
			currentNode = currentNode.right
		else:
			break
	return closest
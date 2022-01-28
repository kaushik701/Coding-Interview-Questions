# O(n) time | O(d) space n:-number of nodes of tree, 
#d:-depth f the tree
def ValidateBST(tree):
	return ValidateBSTHelper(tree,float('-inf'),float('inf'))

def ValidateBSTHelper(tree,minValue,maxValue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftIsvalid = ValidateBSTHelper(tree.left,minValue,tree.value)
	return leftIsvalid and ValidateBSTHelper(tree.right,tree.value,maxValue)
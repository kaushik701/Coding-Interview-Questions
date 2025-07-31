class BinarySearchTree:
	def __init__(self,value=0,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

class TreeInfo:
	def __init__(self,rootIdx):
		self.rootIdx = rootIdx

# O(n^2) time | O(h) space
def ReconstructBST(preOrderTraversalValues):
	if len(preOrderTraversalValues) == 0:
		return None

	currentValue = preOrderTraversalValues[0]
	rightSubtreeRootIdx = len(preOrderTraversalValues)

	for idx in range(1, len(preOrderTraversalValues)):
		value = preOrderTraversalValues[idx]
		if value >= currentValue:
			rightSubtreeRootIdx = idx
			break

	leftSubtree = ReconstructBST(preOrderTraversalValues[1:rightSubtreeRootIdx])
	rightSubtree = ReconstructBST(preOrderTraversalValues[rightSubtreeRootIdx:])
	return BinarySearchTree(currentValue, leftSubtree, rightSubtree)

# O(n) time | O(h) space
def ReconstructBST1(preOrderTraversalValues):
	treeInfo = TreeInfo(0)
	return ReconstructBSTFromRange(float('-inf'), float('-inf'), preOrderTraversalValues, treeInfo)

def ReconstructBSTFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
	if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
		return None

	rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	currentSubtreeInfo.rootIdx += 1
	leftSubtree = ReconstructBSTFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
	rightSubtree = ReconstructBSTFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)

	return BinarySearchTree(rootValue, leftSubtree, rightSubtree)
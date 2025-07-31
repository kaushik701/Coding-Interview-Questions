class BinarySearchTree:
	def __init__(self,value=0,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

class TreeInfo:
	def __init__(self,numberOfNodesVisited,latestVisitedNodeValue):
		self.numberOfNodesVisited = numberOfNodesVisited 
		self.latestVisitedNodeValue = latestVisitedNodeValue 

# O(n) time | O(n) space
def KthLargestValueInBST(tree,k):
	sortedNodeValues = []
	inOrderTraverse(tree, sortedNodeValues)
	return sortedNodeValues[len(sortedNodeValues)-k]

def inOrderTraverse(node, sortedNodeValues):
	if node == None:
		return 

	inOrderTraverse(node.left, sortedNodeValues)
	sortedNodeValues.append(node.value)
	inOrderTraverse(node.right, sortedNodeValues)


# O(h+k) time | O(h) space
def KthLargestValueInBST1(tree,k):
	treeInfo = TreeInfo(0, None)
	reverseInOrderTraverse(tree, k, treeInfo)
	return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
	if node == None or treeInfo.numberOfNodesVisited >= k:
		return

	reverseInOrderTraverse(node.right, k, treeInfo)
	if treeInfo.numberOfNodesVisited < k:
		treeInfo.numberOfNodesVisited += 1
		treeInfo.latestVisitedNodeValue = node.value
		reverseInOrderTraverse(node.left, k,treeInfo)
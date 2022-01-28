# O(nlog(n)) time | O(h) space, h- height of binary tree
def AllNodeDepths(root):
	sumOfAllDepths = 0
	stack = [root]
	while len(stack) > 0:
		node = stack.pop()
		if node is None:
			continue
		sumOfAllDepths += NodeDepths(node)
		stack.append(node.left)
		stack.append(node.right)
	return sumOfAllDepths

def NodeDepths(node,depth=0):
	if node is None:
		return 0
	return depth + NodeDepths(node.left,depth+1) + NodeDepths(node.right,depth+1)

# O(nlog(n)) time | O(h) space
def AllNodeDepths1(root):
	if root is None: return 0
	return AllNodeDepths1(root.left) + AllNodeDepths1(root.right) + NodeDepths1(root)

def NodeDepths1(node,depth=0):
	if node is None:
		return 0
	return depth + NodeDepths1(node.left,depth+1) + NodeDepths1(node.right,depth+1)

# O(n) time | O(n) space
def AllNodeDepths2(root):
	nodeCounts = {}
	AddNodeCounts(root,nodeCounts)
	nodeDepths = {}
	AddNodeDepths(root,nodeDepths,nodeCounts)
	return sumAllNodeDepths(root,nodeDepths)

def AddNodeCounts(node,nodeCounts):
	nodeCounts[node] = 1
	if node.left is not None:
		AddNodeCounts(node.left,nodeCounts)
		nodeCounts[node] += nodeCounts[node.left]
	if node.right is not None:
		AddNodeCounts(node.right,nodeCounts)
		nodeCounts[node] += nodeCounts[node.right]

def AddNodeDepths(node,nodeDepths,nodeCounts):
	nodeCounts[node] = 0
	if node.left is not None:
		AddNodeDepths(node.left,nodeDepths,nodeCounts)
		nodeCounts[node] += nodeDepths[node.left] + nodeCounts[node.left]
	if node.right is not None:
		AddNodeDepths(node.right,nodeDepths,nodeCounts)
		nodeCounts[node] += nodeDepths[node.right] + nodeCounts[node.right]

def sumAllNodeDepths(node,nodeDepths):
	if node is None:
		return 0
	return sumAllNodeDepths(node.left,nodeDepths) + sumAllNodeDepths(node.right,nodeDepths) + nodeDepths[node]

# O(n) time | O(h) space
def AllNodeDepths3(root):
	return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0,0)
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
	sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree
	
	numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
	sumOfDepths = sumOfLeftDepths + sumOfRightDepths
	sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths
	return TreeInfo(numNodesInTree,sumOfDepths,sumOfAllDepths)

class TreeInfo:
	def __init__(self,numNodesInTree,sumOfDepths,sumOfAllDepths):
		self.numNodesInTree = numNodesInTree
		self.sumOfDepths = sumOfDepths
		self.sumOfAllDepths = sumOfAllDepths
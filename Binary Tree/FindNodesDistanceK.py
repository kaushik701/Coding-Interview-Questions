class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

# O(n) time | O(n) space
def FindNodesDistanceK(tree, target, k):
	nodesToParents = {}
	populateNodesToParents(tree, nodesToParents)
	targetNode = getNodeFromValue(target, tree, nodesToParents)

	return breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)

def breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
	queue = [(targetNode,0)]
	seen = {targetNode.value}
	while len(queue) > 0:
		currentNode, distanceFromTarget= queue.pop(0)
		if distanceFromTarget == k:
			nodesDistanceK = [node.value for node, _ in queue]
			nodesDistanceK.append(currentNode.value)
			return nodesDistanceK

		connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
		for node in connectedNodes:
			if node is None:
				continue

			if node.value in seen:
				continue

			seen.add(node.value)
			queue.append((node, distanceFromTarget+1))
	return []

def getNodeFromValue(value, tree, nodesToParents):
	if tree.value == value:
		return tree

	nodeParent = nodesToParents[value]
	if nodeParent.left and nodeParent.left.value == value:
		return nodeParent.left

	return nodeParent.right

def populateNodesToParents(node,nodesToParents, parent=None):
	if node:
		nodesToParents[node.value] = parent
		populateNodesToParents(node.left, nodesToParents, node)
		populateNodesToParents(node.right, nodesToParents, node)

# O(n) time | O(n) space
def FindNodesDistanceK1(tree, target, k):
	nodesDistanceK = []
	findDistanceFromNodetoTarget(tree, target, k, nodesDistanceK)
	return nodesDistanceK

def findDistanceFromNodetoTarget(node, target, k,nodesDistanceK):
	if node is None:
		return -1

	if node.value == target:
		addSubtreenodesAtDistanceK(node,0,k,nodesDistanceK)
		return 1
	
	leftDistance = findDistanceFromNodetoTarget(node.left, target, k, nodesDistanceK)
	rightDistance = findDistanceFromNodetoTarget(node.right,target,k,nodesDistanceK)

	if leftDistance == k or rightDistance == k:
		nodesDistanceK.append(node.value)

	if leftDistance != -1:
		addSubtreenodesAtDistanceK(node.right, leftDistance+1, k, nodesDistanceK)
		return leftDistance + 1

	if rightDistance != -1:
		addSubtreenodesAtDistanceK(node.left, rightDistance+1, k, nodesDistanceK)
		return rightDistance + 1

	return -1

def addSubtreenodesAtDistanceK(node, distance, k, nodesDistanceK):
	if node is None:
		return

	if distance == k:
		nodesDistanceK.append(node.value)
	else:
		addSubtreenodesAtDistanceK(node.left, distance+1, k, nodesDistanceK)
		addSubtreenodesAtDistanceK(node.right, distance+1, k, nodesDistanceK)


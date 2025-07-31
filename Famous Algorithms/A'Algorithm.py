# O(w*h*log(w*h)) time | O(w*h) space
class Node:
	def __init__(self, row, col, value):
		self.id = str(row) + '-' + str(col)
		self.row = row
		self.col = col
		self.value = value
		self.distanceFromStart = float('inf') #G
		self.estimatedDistanceToEnd = float('inf') #H 
		self.cameFrom = None

def AstarAlgorithm(startRow, startCol, endRow, endCol, graph):
	nodes = initializeNodes(graph)

	startNode = nodes[startRow][startCol]
	endNode = nodes[endRow][endCol]

	startNode.distanceFromStart = 0
	startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)

	nodesToVisit = MinHeap([startNode])

	while not nodesToVisit.isEmpty():
		currentMinDistanceNode = nodesToVisit.remove()

		if currentMinDistance == endNode:
			break

		neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)
		for neighbor in neighbors:
			if neighbor.value == 1:
				continue

			tentativeDistanceToNeighbor = currentMinDistance.distanceFromStart+1

			if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
				continue

			neighbor.cameFrom = currentMinDistanceNode
			neighbor.distanceFromStart = tentativeDistanceToNeighbor
			neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(neighbor, endNode)

			if not nodesToVisit.contains(neighbor):
				nodesToVisit.insert(neighbor)
			else:
				nodesToVisit.update(neighbor)

	return reConstructPath(endNode)

def initializeNodes(graph):
	nodes = []

	for i, row in enumerate(graph):
		nodes.append([])
		for j, value in enumerate(row):
			nodes[i].append(Node(i,j,value))
	return nodes

def calculateManhattanDistance(currentNode, endNode):
	currentRow = currentNode.row
	currentCol = currentNode.col
	endRow = endNode.row
	endCol = endNode.col

	return abs(currentRow-endRow) + abs(currentCol-endCol)  

def getNeighboringNodes(node, nodes):
	neighbors = []
	numRows = len(nodes)
	numCols = len(nodes[0])

	row = node.row
	col = node.col

	if row < numRows - 1: #DOWN
		neighbors.append(nodes[row+1][col])

	if row > 0: #UP
		neighbors.append(nodes[row-1][col])

	if col < numCols - 1: #RIGHT
		neighbors.append(nodes[row][col+1])

	if col > 0: #LEFT
		neighbors.append(nodes[row][col-1])

	return neighbors

def reConstructPath(endNode):
	if not endNode.cameFrom:
		return []

	currentNode = endNode
	path = []
	while currentNode:
		path.append([currentNode.row, currentNode.col])
		currentNode = currentNode.cameFrom

	return path[::-1]

class MinHeap:
	def __init__(self,comparisonFunc,array):
		self.heap = self.buildHeap(array)
		self.comparisonFunc = comparisonFunc
		self.length = len(self.heap)
		self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)}

	# O(n) time  | O(1) space	
	def buildHeap(self,array):
		firstParentIdx = (len(array)-2) // 2
		for currentIdx in reversed(range(firstParentIdx)):
			self.shiftdown(currentIdx,len(array)-1, array)
		return array

	# O(log(n)) time | O(1) space
	def shiftDown(self,currentIdx,endIdx,heap):
		childOneIdx = currentIdx*2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != 1:
				if self.comparisonFunc(heap[childTwoIdx].estimatedDistanceToEnd,heap[childOneIdx].estimatedDistanceToEnd):
					idxToSwap = childTwoIdx
				else:
					idxToSwap = childOneIdx
			else:
				idxToSwap = childOneIdx
			if self.comparisonFunc(heap[idxToSwap],estimatedDistanceToEnd,heap[currentIdx].estimatedDistanceToEnd):
				self.swap(currentIdx,idxToSwap,heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				break

	# O(log(n)) time | O(1) space
	def shiftUp(self,currentIdx,heap):
		parentIdx = (currentIdx-1) // 2
		while currentIdx > 0:
			if self.comparisonFunc(heap[currentIdx].estimatedDistanceToEnd,heap[parentIdx].estimatedDistanceToEnd):
				self.swap(currentIdx,parentIdx,heap)
				currentIdx = parentIdx
				parentIdx = (currentIdx-1) // 2
			else:
				return

	# O(1) time | O(1) space
	def peek(self):
		return self.heap[0]

	def isEmpty(self):
		return self.length == 0

	# O(log(n)) time | O(n) space
	def remove(self):
		swap(0, self.length-1,self.heap)
		valueToRemove = self.heap.pop(0)
		del self.nodePositionsInHeap[node.id] 
		self.shiftDown(0,self.length - 1, self.heap)
		return valueToRemove

	# O(log(n)) time | O(1) space
	def insert(self,value):
		self.heap.append(value)
		self.nodePositionsInHeap[node.id] = len(self.heap)-1
		self.shiftUp(self.length-1,self.heap)

	def swap(self,i,j,heap):
		self.nodePositionsInHeap[heap[i].id] = j
		self.nodePositionsInHeap[heap[j].id] = i
		heap[i],heap[j] = heap[j],heap[i]

	def contains(self, node):
		return node.id in self.nodePositionsInHeap

	def update(self, node):
		self.shiftUp(self.nodePositionsInHeap[node.id], self.heap)
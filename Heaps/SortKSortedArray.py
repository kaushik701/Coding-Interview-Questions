# O(nlog(k)) time | O(k) space
def SortKSortedArray(array,k):
	result = [0] * len(array)
	initialElements = array[:min(k+1,len(array))]
	minHeap = MinHeap(lambda a,b: a<b, initialElements)
	index = 0
	for i in range(k+1,len(array)):
		result[index] = minHeap.remove()
		index += 1
		minHeap.insert(array[i])

	while not minHeap.isEmpty():
		result[index] = minHeap.remove()
		index += 1
	return result


class MinHeap:
	def __init__(self,comparisonFunc,array):
		self.heap = self.buildHeap(array)
		self.comparisonFunc = comparisonFunc
		self.length = len(self.heap)

	# O(n) time  | O(1) space	
	def buildHeap(self,array):
		firstParentIdx = (len(array)-2) // 2
		for currentIdx in reversed(range(firstParentIdx)):
			self.shiftdown(currentIdx,len(array)-1, array)
		return array

	# O(log(n)) time | O(n) space
	def shiftDown(self,currentIdx,endIdx,heap):
		childOneIdx = currentIdx*2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != 1:
				if self.comparisonFunc(heap[childTwoIdx],heap[childOneIdx]):
					idxToSwap = childTwoIdx
				else:
					idxToSwap = childOneIdx
			else:
				idxToSwap = childOneIdx
			if self.comparisonFunc(heap[idxToSwap],heap[currentIdx]):
				self.swap(currentIdx,idxToSwap,heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				break

	# O(log(n)) time | O(n) space
	def shiftUp(self,currentIdx,heap):
		parentIdx = (currentIdx-1) // 2
		while currentIdx > 0:
			if self.comparisonFunc(heap[currentIdx],heap[parentIdx]):
				self.swap(currentIdx,parentIdx,heap)
				currentIdx = parentIdx
				parentIdx = (currentIdx-1) // 2
			else:
				return

	# O(1) time | O(1) space
	def peek(self):
		return self.heap[0]

	# O(log(n)) time | O(n) space
	def remove(self):
		swap(0, self.length-1,self.heap)
		valueToRemove = self.heap.pop(0)
		self.length -= 1
		self.shiftDown(0,self.length - 1, self.heap)
		return valueToRemove

	# O(log(n)) time | O(n) space
	def insert(self,value):
		self.heap.append(value)
		self.length += 1
		self.shiftUp(self.length-1,self.heap)

	def swap(self,i,j,heap):
		heap[i],heap[j] = heap[j],heap[i]

	def isEmpty(self):
        return self.length == 0


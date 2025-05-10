# O(nk) time | O(n+k) space
def mergeSortedArrays(arrays):
	sortedList = []
	elementIdxs = [0 for array in arrays]
	while True:
		smallestItems = []
		for arrayIdx in range(len(arrays)):
			relevantArray = arrays[arrayIdx]
			elementIdx = elementIdxs[arrayIdx]
			if elementIdx == len(relevantArray):
				continue
			smallestItems.append({"arrayIdx":arrayIdx, "num":relevantArray[elementIdx]})
		if len(smallestItems) == 0:
			break
		nextItem = getMinValue(smallestItems)
		sortedList.append(nextItem["num"])
		elementIdxs[nextItem["arrayIdx"]] += 1
	return sortedList

def getMinValue(items):
	minValueIdx = 0
	for i in range(1,len(items)):
		if items[i]["num"] <  items[minValueIdx]["num"]:
			minValueIdx  = i
	return items[minValueIdx]

# O(nlog(k)+k) time | O(n+k) space
def mergeSortedArrays2(arrays):
	sortedList = []
	smallestItems = []
	for arrayIdx in range(len(arrays)):
		smallestItems.append({"arrayIdx":arrayIdx,"elementIdx":0,"num":arrays[arrayIdx][0]})
	minHeap = MinHeap(smallestItems)
	while not minHeap.isEmpty():
		smallestItem = minHeap.remove()
		arrayIdx,elementIdx,num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"]
		sortedList.append(num)
		if elementIdx == len(arrays[arrayIdx]) - 1:
			continue
		minHeap.insert({"arrayIdx":arrayIdx,"elementIdx":elementIdx+1,"num":arrays[arrayIdx][elementIdx+1]})
	return sortedList

class MinHeap:
	def __init__(self,comparisonFunc,array):
		self.heap = self.buildHeap(array)
		self.comparisonFunc = comparisonFunc
		self.length = len(self.heap)

	# O(1) time | O(1) space
	def isEmpty(self):
		return length == 0

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
				if self.comparisonFunc(heap[childTwoIdx]["num"],heap[childOneIdx]["num"]):
					idxToSwap = childTwoIdx
				else:
					idxToSwap = childOneIdx
			else:
				idxToSwap = childOneIdx
			if self.comparisonFunc(heap[idxToSwap]["num"],heap[currentIdx]["num"]):
				self.swap(currentIdx,idxToSwap,heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				break

	# O(log(n)) time | O(n) space
	def shiftUp(self,currentIdx,heap):
		parentIdx = (currentIdx-1) // 2
		while currentIdx > 0:
			if self.comparisonFunc(heap[currentIdx]["num"],heap[parentIdx]["num"]):
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
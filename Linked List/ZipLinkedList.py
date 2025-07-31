# O(n) time | O(1) space
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

def ZipLinkedList(linkedList):
	if linkedList.next == None or linkedList.next.next == None:
		return linkedList

	firstHalfHead = linkedList
	secondHalfHead = SplitLinkedList(linkedList)

	reversedSecondHalfHead = ReverseLinkedList(secondHalfHead)

	return interweaveLinkedLists(firstHalfHead, reversedSecondHalfHead)

def SplitLinkedList(linkedList):
	slowIterator = linkedList
	fastIterator = linkedList
	while fastIterator is not None ad fastIterator.next is not None:
		slowIterator = slowIterator.next
		fastIterator = fastIterator.next.next

	secondHalfHead = slowIterator.next
	slowIterator.next = None
	return secondHalfHead

def interweaveLinkedLists(linkedList1, linkedList1):
	linkedList1Iterator = linkedList1
	linkedList2Iterator = linkedList2
	while linkedList2Iterator is not None:
		linkedList1IteratorNext = linkedList1Iterator.next
		linkedList2IteratorNext = linkedList2Iterator.next

		linkedList1Iterator.next = linkedList2Iterator
		linkedList2Iterator.next = linkedList1IteratorNext
		
		linkedList1Iterator = linkedList1IteratorNext
		linkedList2Iterator = linkedList2IteratorNext

	return linkedList1

def ReverseLinkedList(linkedList):
	previousNode,currentNode = None,linkedList
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode
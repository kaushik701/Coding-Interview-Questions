# O(n) time | O(n) space
def LinkedListPalindrome(head):
	isPalindromeResults = isPalindrome(head, head)
	return isPalindromeResults.outerNodesAreEqual

def isPalindrome(leftNode, rightNode):

	if rightNode is None:
		return LinkedListInfo(True, leftNode)
	results = isPalindrome(leftNode, rightNode.next)
	outerNodesAreEqual = results.outerNodesAreEqual

	resultIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value
	nextMatchingNextNode = leftNodeToCompare.next

	return LinkedListInfo(resultIsEqual, nextMatchingNextNode)


class LinkedListInfo:
	def __init__(self, outerNodesAreEqual, leftNodeToCompare):
		self.outerNodesAreEqual = outerNodesAreEqual
		self.leftNodeToCompare = leftNodeToCompare

# O(n) time | O(1) space
def LinkedListPalindrome1(head):
	slowNode = head
	fastNode = head
	while fastNode is not None and fastNode.next is not None:
		slowNode = slowNode.next
		fastNode = fastNode.next.next

	reversedSecondHalfNode = ReverseLinkedList(slowNode)
	firstHalfNode = head

	while reversedSecondHalfNode is not None:
		if reversedSecondHalfNode.value != firstHalfNode.value:
			return False
		reversedSecondHalfNode = reversedSecondHalfNode.next
		firstHalfNode = firstHalfNode.next
	return True

def ReverseLinkedList(head):
	previousNode,currentNode = None,head
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode
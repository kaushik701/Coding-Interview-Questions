# Leetcode #230: https://youtu.be/5LUXSvjmGCw?si=Vtvvf8cYjdW2H8_q
# O(n) time | O(h) space
class BinaryTree:
	def __init__(self,value=0,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

def KthSmallestValueInBST(root,k):
	n = 0
	stack = []
	currentNode = root
	while currentNode and stack:
		while currentNode:
			stack.append(currentNode)
			currentNode = currentNode.left
		currentNode = stack.pop()
		n += 1
		if n == k:
			return currentNode.value
		currentNode = currentNode.right